const express = require("express");
const http = require("http");
const app = express();
const server = http.createServer(app);
const fetch = require("node-fetch");

console.log("Server started");

//
app.set("views", "./views");
app.set("view engine", "ejs");

// Setting up files
app.use(express.static("public"));
app.use("/css", express.static(__dirname + "/public/css"));
app.use("/js", express.static(__dirname + "/public/js"));

app.post("/winner/:team&:team2", (req, res) => {
	const team = req.params.team;
	const team2 = req.params.team2;
	fetch("http://127.0.0.1:5000/basketball/" + team + "&" + team2)
		.then((res) => res.json())
		.then((json) => {
			res.send(json);
		});
	console.log(team + " " + team2);
});

app.get("/", (req, res) => {
	res.render("index");
});

server.listen(5500);
