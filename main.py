from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/about')
def About():
    return render_template('about.html', nome ="BNB DENTE")


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/booking')
def booking():
    return render_template('booking.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')


if __name__ == '__main__':
    app.run()
