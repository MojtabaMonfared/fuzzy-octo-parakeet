import pytvmaze
import json
import requests

tvm = pytvmaze.TVMaze('meirona', 'vNPdjTax7m9iwsuhnUSanNVrjcjBsT6y')

def search_by_name(name):
    return tvm.get_show(show_name=name)

def show_episode_and_season(name,ep,se):
    show = tvm.get_show(show_name=name, embed='episodes')
    return show[int(ep)][int(se)]


def episodes(name):
    episodes_ = tvm.get_show(show_name=name, embed='episodes')
    for episode in episodes_.episodes:
        print episode
        

def search_by_imdb(code):
    return tvm.get_show(imdb_id=code)

def get_info(name):
    show = tvm.get_show(show_name=name)
    return show.summary

def get_original_cover(name):
    show = tvm.get_show(show_name=name)
    return show.image['original']

def get_medium_cover(name):
    show = tvm.get_show(show_name=name)
    return show.image['medium']


def get_status(name):
    show = tvm.get_show(name)
    return show.status
