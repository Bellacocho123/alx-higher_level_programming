#!/usr/bin/node

function convert (base) {
  return function (num) {
    return num.toString(base);
  };
}

exports.converter = convert;
