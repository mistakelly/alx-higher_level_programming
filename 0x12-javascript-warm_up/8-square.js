#!/usr/bin/node
const args = process.argv[2];
const argsNumber = parseInt(args, 10);
if (isNaN(argsNumber)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argsNumber; i++) {
    let pattern = '';
    for (let j = 0; j < argsNumber; j++) {
      pattern += 'X';
    }
    console.log(pattern);
  }
}
