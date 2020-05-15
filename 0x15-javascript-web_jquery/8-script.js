#!/usr/bin/node
// Fetches and lists the Star Wars movie titles

$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $.each(data.results, function (index, list) {
      $('UL#list_movies').append('<li>' + list.title + '</li>');
    });
  });
});
