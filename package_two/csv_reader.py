import logging
import os

import pandas as pd


def read_csv() -> pd.DataFrame:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, '../package_one/stats.csv')
    logging.info(f"Getting statics from '{csv_path}'.")

    return pd.read_csv(csv_path)