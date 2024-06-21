import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from package_one.models import EggGroup, Pokemon, Base

engine = create_engine('sqlite:///pokemon.sqlite')
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine, checkfirst=True)
    logging.info('Created database tables.')

def get_session():
    return Session()

def create_pokemon(session, data) -> Pokemon:
    pokemon = Pokemon(
        id=data["id"],
        name=data["name"],
        base_experience=data["base_experience"],
        height=data["height"],
        weight=data["weight"]
    )
    session.add(pokemon)
    session.commit()
    logging.info(f"Pokemon '{data['name']}' is created.")
    return pokemon

def get_all_pokemons(session) -> list:
    return session.query(Pokemon).all()

def get_pokemon_by_id(session, pokemon_id) -> Pokemon:
    return session.query(Pokemon).get(pokemon_id)

def delete_pokemon(session, pokemon_id):
    pokemon = session.query(Pokemon).get(pokemon_id)
    session.delete(pokemon)
    session.commit()

def delete_all_pokemons(session):
    pokemons_list = get_all_pokemons(session)

    if pokemons_list != []:
        for pokemon in pokemons_list:
            session.delete(pokemon)
            session.commit()

def delete_all_egg_groups(session):
    egg_groups_list = get_all_egg_groups(session)

    if egg_groups_list != []:
        for egg_group in egg_groups_list:
            session.delete(egg_group)
            session.commit()

def pokemon_add_egg_groups(session, pokemon, egg_groups_list):
    for egg_group in [eg for eg in egg_groups_list if eg is not None]:
            pokemon.egg_groups.append(egg_group)
            session.commit()
            logging.info(f"Egg_group '{egg_group.name}' is added to pokemon '{pokemon.name}'.")
    
def create_egg_group(session, egg_group_name):
    egg_group = EggGroup(name=egg_group_name)
    session.add(egg_group)
    session.commit()
    logging.info(f"Egg_group '{egg_group_name}' is created.")

def get_all_egg_groups(session) -> list:
    return session.query(EggGroup).all()

def get_egg_group_by_id(session, egg_group_id) -> EggGroup:
    return session.query(EggGroup).get(egg_group_id)

def create_egg_group_if_not_exists(session, egg_group_name) -> EggGroup:
    egg_group =  session.query(EggGroup).filter_by(name = egg_group_name).one_or_none()
    if egg_group is None:
        egg_group = create_egg_group(session, egg_group_name)
    return egg_group