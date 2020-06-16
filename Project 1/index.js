const express = require("express");
const path = require("path");
const fs = require("fs");
const app = express();
const port = 80

app.use(express.urlencoded({ extended: true }));
// app.use(express.json());   
// Set the template engine as pug
app.set('view engine', 'pug');

//Set the views directory
app.set('views', path.join(__dirname, 'views'))

// Our pug demo endpoint
app.get("/", (req, res) => {
	const con = "jsdudhd";
	const params = { 'title': 'Diamond Gym', "content": con };
	res.render('index.pug', params);
})

app.post("/", (req, res) => {
	name = req.body.name;
	age = req.body.age;
	gender = req.body.gender;
	phone = req.body.phone;
	let output = `The details of client is ${name}, ${age} years old, ${gender}, contact no. is ${phone}`;
	fs.writeFileSync('output.txt', output)
	const params = { 'message': 'Your form has been submitted successfully' };
	res.render("index.pug", params);
})

app.listen(port, () => {
	console.log(`The application started successfully on port ${port}`);
}); 