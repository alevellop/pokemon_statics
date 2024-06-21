from package_two import gets_methods as gm

def test_get_egg_groups():
    response = gm.get_egg_groups()

    assert isinstance(response, list)
    assert len(response) == 13

def test_get_average_height():
    valid_group = "monster"
    invalid_group = "invalid_group"

    average_height = gm.get_average_height(valid_group)
    assert isinstance(average_height, float)

    invalid_average_height = gm.get_average_height(invalid_group)
    assert invalid_average_height is None

def test_get_average_weight():
    valid_group = "monster"
    invalid_group = "invalid_group"

    average_weight = gm.get_average_weight(valid_group)
    assert isinstance(average_weight, float)

    invalid_average_weight = gm.get_average_weight(invalid_group)
    assert invalid_average_weight is None