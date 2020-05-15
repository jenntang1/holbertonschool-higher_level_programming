#!/usr/bin/node
// Adds element to a list

$(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
