#!/usr/bin/node
// Updates text in header

$(function() {
    $('DIV#update_header').click(function() {
        $('header').text('New Header!!!');
    });
});