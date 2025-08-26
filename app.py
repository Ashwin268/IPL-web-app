from http.client import responses

from flask import Flask, render_template, request
import requests
app = Flask(__name__)
@app.route('/')
def index():
    responses = requests.get('http://127.0.0.1:5000/api/teams')
    teams = responses.json()['teams']
    return render_template('index.html', teams=sorted(teams))

@app.route('/teamvsteam')
def teamvsteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    responses = requests.get('http://127.0.0.1:5000/api/teams')
    teams = responses.json()['teams']

    responses1 = requests.get('http://127.0.0.1:5000/api/compareTeams?team1={}&team2={}'.format(team1, team2))
    return render_template('index.html', result = responses1.json(), teams=sorted(teams))


app.run(debug=True, port=7000)