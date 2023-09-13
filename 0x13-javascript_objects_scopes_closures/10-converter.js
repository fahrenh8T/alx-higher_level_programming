#!/usr/bin/node
// converts nunber from base 10 to another base
exports.converter = function (base) {
  return num => num.toString(base);
};
