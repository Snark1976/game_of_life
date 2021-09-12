from flask import Flask
from flask import render_template
from game_of_life import GameOfLife
from flask import request

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        vert = int(request.form.get('vert'))
        horiz = int(request.form.get('horiz'))
        pts = int(request.form.get('pts'))
    else:
        vert = 25
        horiz = 30
        pts = 1
    GameOfLife(horiz, vert, pts=pts)
    return render_template('index.html', vert=vert, goriz=horiz, pts=pts)

@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
