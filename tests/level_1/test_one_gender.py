from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('Доигрался!', 'Доигралась!', 'female') == 'Доигралась!'
    assert not genderalize('Доигрался!', 'Доигралась!', 'female') == 'Доигрался!'
