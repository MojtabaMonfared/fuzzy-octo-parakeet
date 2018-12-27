# -*- coding: utf-8 -*-
# @author: Meirona

from flask import Flask, render_template, request
from api import *
import redis

app = Flask(__name__)
db = redis.Redis()


@app.route('/', methods=['GET'])
def index_GET():
    name = request.form.get('name')
    if not name:
        return render_template('index.html')

@app.route('/', methods=['POST'])
def index_POST():
    name = request.form.get('name')
    if name:
        title_ = search_by_name(str(name))
        cover_ = get_medium_cover(str(name))
        info_ = get_info(str(name))[:80]
        status_ = get_status(str(name))
        url_ = get_homepage(str(name))
        rating_ = get_rating(str(name))
        data_ = dict(title=title_, cover=cover_, info=info_, status=status_, url=url_, rate=rating_)
        print "%s searched.." % name
        return render_template('index.html', data=data_)
    else:
        print "no name written..."
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=1247) 