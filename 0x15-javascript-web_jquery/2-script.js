#!/usr/bin/node
// Updates the text color of the HTML tag HEADER to red #FF0000 when the user clicks on div tag

$('DIV#red_header').click(function() {
    $('header').css('color', 'red');
});