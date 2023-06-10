from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/start")
def start():
    return render_template('start.html')

@app.route("/editor")
def editor():
    return render_template('Editor.html')

app.run(debug=True)
