from flask import Flask
from flask import render_template
from game_of_life import GameOfLife
from flask import request

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        width = int(request.form.get('width'))
        height = int(request.form.get('height'))
        generation_per_second = int(request.form.get('generation_per_second'))
        config_world = request.form.get('config_world') == 'on'
    else:
        width = 35
        height = 20
        generation_per_second = 1
        config_world = False
    GameOfLife(width, height, generation_per_second=generation_per_second)
    return render_template('index.html',
                           width=width,
                           height=height,
                           generation_per_second=generation_per_second,
                           config_world=config_world)

@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
