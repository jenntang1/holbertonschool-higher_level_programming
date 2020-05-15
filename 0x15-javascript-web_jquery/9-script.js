#!/usr/bin/node
// Fetches and return 'Salut' (French for 'hi')

$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
