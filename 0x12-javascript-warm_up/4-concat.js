#!/usr/bin/node
// If no arguments are passed, prints “undefined is undefined”
// If two arguments are passed, prints both concatenated by "is"

const myArgs = process.argv.slice(2);
const is = 'is';

console.log(myArgs[0] + ' ' + is + ' ' + myArgs[1]);
