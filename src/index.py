from flask import Flask,render_template

app = Flask(__name__)

""" AQUI NUESTRAS ROUTAS DE NUESTRO CRUD-API """
""" HERE GET ROUTES CRUD-API """
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__== '__main__':
    app.run(debug=True)