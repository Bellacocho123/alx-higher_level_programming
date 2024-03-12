#!/usr/bin/node

const numbers = [];

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    numbers.push(parseInt(process.argv[i]));
  }
  numbers.sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
}
