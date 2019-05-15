import datetime


def get_ndays_later(days=7):
    return datetime.date.today() + datetime.timedelta(days=7)
