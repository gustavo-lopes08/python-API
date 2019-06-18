from flask import Flask, render_template, g, request
import json, requests, sqlite3
from . import config

app = Flask(__name__)

def connect_db():
    print("Conectado")
    return sqlite3.connect(config.DATABASE_NAME)

@app.before_request
def before_request():
    g.db = connect_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pessoas/', methods=['POST', 'GET'])
def addpessoa():
    people = requests.get('https://swapi.co/api/people/1/')
    json_people = json.loads(people.content)

    for k, v in json_people.items():
        if k == 'name':
            nome = v

    if request.method == 'GET':
        return render_template('pessoas.html', nome=nome)

    elif request.method == 'POST':
        name = request.form['name']
        g.db.execute('INSERT INTO people (name) VALUES (?)', [name])
        g.db.commit()
        return render_template('pessoas.html', nome=name)