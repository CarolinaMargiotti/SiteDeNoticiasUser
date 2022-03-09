from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lefishe'

@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()