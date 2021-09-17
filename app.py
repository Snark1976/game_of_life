from flask import Flask
from flask import render_template, request
from game_of_life import GameOfLife, WorldConfiguration

app = Flask(__name__)

start_configuration = WorldConfiguration(width=30,
                                         height=20,
                                         generation_per_second=0
                                         )


@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        start_configuration.width = int(request.form.get('width'))
        start_configuration.height = int(request.form.get('height'))
        start_configuration.generation_per_second = int(request.form.get('generation_per_second'))
        start_configuration.config_world = request.form.get('config_world') == 'on'
        if start_configuration.config_world:
            start_configuration.world = [[int(request.form.get(f'{i}:{j}') == 'on')
                                          for j in range(start_configuration.width)]
                                         for i in range(start_configuration.height)]

    GameOfLife(start_configuration)
    return render_template('index.html',
                           width=start_configuration.width,
                           height=start_configuration.height,
                           generation_per_second=start_configuration.generation_per_second,
                           config_world=start_configuration.config_world
                           )

@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
