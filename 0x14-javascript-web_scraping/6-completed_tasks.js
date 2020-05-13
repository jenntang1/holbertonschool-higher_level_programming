#!/usr/bin/node
// Computes the number of tasks completed by a user

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports request module to make http call
const request = require('request');

// GET request
request.get(myArgs[0], { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const dict = {};
    const data = body;
    for (; count < data.length; count++) {
      if (data[count].completed) {
        if (!(data[count].userId in dict)) {
          dict[data[count].userId] = 0;
        }
        dict[data[count].userId] += 1;
      }
    }
    console.log(dict);
  }
});
