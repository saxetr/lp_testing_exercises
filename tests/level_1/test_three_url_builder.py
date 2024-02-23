from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('eurotruck@example.com', 'buy', {'color':'black', 'year':'2003'}) == 'eurotruck@example.com/buy?color=black&year=2003'
