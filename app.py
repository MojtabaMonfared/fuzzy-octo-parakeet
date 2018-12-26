# -*- coding: utf-8 -*-
# @author: Meirona

from flask import Flask, render_template
from api import *

app = Flask(__name__)

@app.route('/')
def index():
    cover_ = get_original_cover('breaking bad')
    title_ = search_by_name('breaking bad')
    info_ = get_info('breaking bad')
    return render_template('test.html', cover=cover_,title=title_,info=info_[:80])


if __name__ == '__main__':
    app.run(port=2333) 