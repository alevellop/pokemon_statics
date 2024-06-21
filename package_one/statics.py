import logging
from multiprocessing import Pool

import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from package_one import data_base as db
from package_one.models import EggGroup, Pokemon
def generate_statics_for_group(egg_group_name):
    session =  db.get_session()
    subquery = (
        session.query(
            EggGroup.name,
            func.avg(Pokemon.height).label("average_height"),
            func.avg(Pokemon.weight).label("average_weight")
        )
        .join(EggGroup.pokemons)
        .filter(EggGroup.name == egg_group_name)
        .group_by(EggGroup.name)
        .subquery()
    )

    result = session.query(
        subquery.c.name.label("egg_group"),
        subquery.c.average_height,
        subquery.c.average_weight
    ).one()

    return result
def generate_statics(session) -> pd.DataFrame:
    egg_groups = db.get_all_egg_groups(session)

    with Pool() as pool:
        engine = session.bind
        new_session = sessionmaker(bind=engine)()
        results = pool.map(generate_statics_for_group, [egg_group.name for egg_group in egg_groups])

    logging.info(f"Static data generated.")
    return pd.DataFrame(results, columns=["egg_group", "average_height", "average_weight"])