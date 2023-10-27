from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', title='Главная')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html', title='Одежда')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html', title='Обувь')


@app.route('/jackets/')
def jackets():
    return render_template('jackets.html', title='Куртки')


if __name__ == '__main__':
    app.run(debug=True)
