#!/usr/bin/node
const args = process.argv;
const A = parseInt(args[2]);
const B = parseInt(args[3]);
if (typeof A === 'number' && typeof B === 'number') {
  console.log(add(A, B));
} else {
  console.log('NaN');
}

function add (a, b) {
  return (a + b);
}
