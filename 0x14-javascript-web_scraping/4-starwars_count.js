#!/usr/bin/node
// Prints number of movies Wedge Antilles appeared in

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports request module to make http call
// https://swapi-api.hbtn.io/api/films/ will be the argument passed
const request = require('request');
const url = myArgs[0];
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    let elmt = 0;
    let links;
    const list = body.results;
    for (; elmt < list.length; elmt++) {
      if (list[elmt].characters) {
        for (links of list[elmt].characters) {
          if (links.includes('18')) {
            count++;
          }
        }
      }
    }
    console.log(count);
  }
});
