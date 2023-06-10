from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/start', methods = ['GET', 'POST'])
def start():
    return render_template('start.html')

@app.route('/editor', methods = ['GET', 'POST'])
def editor():
    if request.method == 'POST':
        file = request.form.get('filename')
        code = request.form.get('code')
        fo = open(file + ".js", "w")
    return render_template('Editor.html')

app.run(debug=True)
