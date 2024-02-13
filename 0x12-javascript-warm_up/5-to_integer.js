#!/usr/bin/node
const array = process.argv;
const convertedNum = parseInt(array[2], 10);
if (isNaN(convertedNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertedNum}`);
}
