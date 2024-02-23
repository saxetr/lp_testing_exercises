from functions.level_1.two_date_parser import compose_datetime_from

import datetime

def test_compose_datetime_from():
    assert compose_datetime_from('tomorrow', '22:50') == datetime.datetime(datetime.date.today().year,
                                                                           datetime.date.today().month,
                                                                           datetime.date.today().day + 1,
                                                                           22, 50 )
    assert not compose_datetime_from('tomorrow', '22:50') == datetime.datetime(datetime.date.today().year,
                                                                           datetime.date.today().month,
                                                                           datetime.date.today().day,
                                                                           22, 50 )
