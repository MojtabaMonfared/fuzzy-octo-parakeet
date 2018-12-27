from api import *


def get_rating(name):
    show = tvm.get_show(show_name=name)
    return show.rating['average']

print get_rating('dexter')