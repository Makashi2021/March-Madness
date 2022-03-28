from flask import Flask, jsonify
import winner

app = Flask(__name__)




@app.route("/basketball/<team1>&<team2>")
def hello_world(team1, team2):
    return jsonify(winner.findWinner(team1, team2))