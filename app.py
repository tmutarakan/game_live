from flask import Flask, render_template
from game_of_live import GameOfLife


app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(width=25, height=25)
    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    return render_template('live.html')


if __name__ == '__main__':
    app.run()
