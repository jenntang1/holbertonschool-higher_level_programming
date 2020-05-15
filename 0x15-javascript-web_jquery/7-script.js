#!/usr/bin/node
// Fetches and replaces the Star Wars character name

$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
  });
});
