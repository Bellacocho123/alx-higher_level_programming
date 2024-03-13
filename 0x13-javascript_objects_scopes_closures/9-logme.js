#!/usr/bin/node

function logMe (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  console.log(this.count + ': ' + item);
  this.count++;
}

exports.logMe = logMe;
