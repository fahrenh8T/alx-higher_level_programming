#!/usr/bin/node
// prints the no. of arg and the new arg value
let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};
