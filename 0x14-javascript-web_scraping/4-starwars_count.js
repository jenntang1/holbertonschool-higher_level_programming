#!/usr/bin/node
// Prints number of movies Wedge Antilles appeared in

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports request module to make http call
// https://swapi-api.hbtn.io/api/films/ will be the argument passed
const request = require('request');
const url = myArgs[0].replace('films', 'people/18');
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (body.films) {
    console.log(body.films.length);
  } else {
    console.log(error);
  }
});
