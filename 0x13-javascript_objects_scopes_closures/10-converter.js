#!/usr/bin/bash
// converts nunber from base 10 to another base
exports.converter = function (base) {
  function myConverter (num) {
    return num.toString(base);
  }

  return myConverter;
};
