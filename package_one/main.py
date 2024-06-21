import asyncio
from package_one import data_base as db, data_api as da, csv_writer as cw, statics as st

async def main():
    session = db.get_session()
    db.create_tables()
    pokemons_urls_list = await da.get_pokemon_urls()

    # get 100 pokemon's urls
    for pokemon_url in pokemons_urls_list:
        pokemon_data, species_urls_list = await da.get_pokemon_data(pokemon_url)
        egg_groups_name_list = await da.get_egg_group_by_specie(species_urls_list)
        egg_groups_list = [db.create_egg_group_if_not_exists(session, name) for name in egg_groups_name_list]
        pokemon = db.create_pokemon(session, pokemon_data)
        db.pokemon_add_egg_groups(session, pokemon, egg_groups_list)

    statics = st.generate_statics(session)
    session.commit()
    session.close()
    cw.generate_csv(statics)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())