from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/start', methods = ['GET', 'POST'])
def start():
    if request.method == 'POST':
        file = request.form.get('filename')
        filefullname = file + ".html"
        fo = open(filefullname, "a")
    return render_template('start.html')

@app.route('/editor', methods = ['GET', 'POST'])
def editor():
    if request.method == 'POST':
        file = request.form.get('filename')
        f = open(file, "a")
        code = request.form.get('code')
        f.write(code)
    return render_template('Editor.html')

@app.route('/terminal', methods = ['GET', 'POST'])
def terminal():
    if request.method == "POST":
        path = request.form.get("path")
        # fullpath = "node"+ " " +'"' + path + '"'
        # f = open("run.bat", "w")
        # f.write(fullpath)
        path = request.form.get("path")
    return render_template('terminal.html')

app.run()
