#!/usr/bin/node
// returns number of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;

  for (let i = 0; i < list.length; i++) {
    occur = (list[i] === searchElement ? occur + 1 : occur);
  }

  return occur;
};
