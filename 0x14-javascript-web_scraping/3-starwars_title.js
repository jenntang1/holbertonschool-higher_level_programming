#!/usr/bin/node
// Prints title of a Star Wars movie from SWAPI

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports request module to make http call
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
request.get(url, { json: true }, function (error, response, body) {
  if (body) {
    console.log(body.title);
  } else {
    console.error(error);
  }
});
