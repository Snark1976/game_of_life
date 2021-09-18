from flask import Flask, render_template, request
from game_of_life import GameOfLife, WorldConfiguration

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        start_configuration = WorldConfiguration(width=int(request.form.get('width')),
                                                 height=int(request.form.get('height')),
                                                 generation_per_second=int(request.form.get('generation_per_second')),
                                                 config_world=request.form.get('config_world')
                                                 )
    else:
        start_configuration = WorldConfiguration(width=30,
                                                 height=20,
                                                 generation_per_second=1
                                                 )

    GameOfLife(start_configuration)
    return render_template('index.html', config=start_configuration)


@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
