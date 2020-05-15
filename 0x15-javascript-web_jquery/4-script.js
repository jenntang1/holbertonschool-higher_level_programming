#!/usr/bin/node
// Updates the text color of the HTML tag HEADER to red and back to green

$(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
