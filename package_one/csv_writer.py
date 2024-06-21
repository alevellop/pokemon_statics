import logging
import os.path

def generate_csv(statics_data):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'stats.csv')
    statics_data.to_csv(csv_path, index=False)
    logging.info(f"Static data saved in '{csv_path}'.")
