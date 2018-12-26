# -*- coding: utf-8 -*-
# @author: Meirona

from flask import Flask, render_template
from api import *

app = Flask(__name__)

@app.route('/')
def index():
    cover_ = get_medium_cover('dexter')
    title_ = search_by_name('dexter')
    info_ = get_info('dexter')
    return render_template('test.html', cover=cover_,title=title_,info=info_[:80])


if __name__ == '__main__':
    app.run(port=5050) 