#!/usr/bin/node

const lists = require('./100-data').list;

console.log(lists);
console.log(lists.map((x, index) => x * index));
