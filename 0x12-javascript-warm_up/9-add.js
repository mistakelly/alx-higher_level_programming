#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (num1, num2) {
  const arg1Number = parseInt(num1, 10);
  const arg2Number = parseInt(num2, 10);
  const sum = arg1Number + arg2Number;

  return sum;
}
const result = add(arg1, arg2);
console.log(result);
