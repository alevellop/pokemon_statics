from package_two import csv_reader as cr


def get_egg_groups() -> list:
    data = cr.read_csv()
    return data['egg_group'].to_list()

def get_average_height(egg_group_name) -> float:
    data = cr.read_csv()
    egg_group_data = data[data['egg_group'] == egg_group_name]
    if egg_group_data.empty:
        return None

    return egg_group_data['average_height'].iloc[0]

def get_average_weight(egg_group_name) -> float:
    data = cr.read_csv()
    egg_group_data = data[data['egg_group'] == egg_group_name]
    if egg_group_data.empty:
        return None

    return egg_group_data['average_weight'].iloc[0]