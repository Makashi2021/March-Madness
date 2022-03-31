const express = require('express');
const http = require('http');
const app = express();
const server = http.createServer(app);
const fetch = require('node-fetch');

console.log('Server started');


app.get('/winner/:team&:team2', (req, res) => {
    const team = req.params.team;
    const team2 = req.params.team2;
    fetch("http://127.0.0.1:5000/basketball/" + team + "&" + team2)
        .then(res => res.json())
        .then(json => {
            res.send(json);
        });
    console.log(team + " " + team2);


});



server.listen(5500)