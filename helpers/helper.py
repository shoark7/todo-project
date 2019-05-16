import datetime


def get_ndays_later(days=7):
    return datetime.date.today() + datetime.timedelta(days=7)


def get_next_location(request):
    nxt_string = request.GET.get('next', '')
    return nxt_string[nxt_string.index('?'):]
