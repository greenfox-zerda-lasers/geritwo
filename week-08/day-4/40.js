'use strict'

var aj = 'kuty'
// write a function that gets a string as an input
// and appends an 'a' character to its end and returns a new string

function appendA(input) {
  var output = input + 'a'
  return output
}

console.log(appendA(aj))

module.exports = appendA;
