#!/usr/bin/node
const array = process.argv;
const convertedNum = parseInt(array[2], 10);
if (isNaN(convertedNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convertedNum; i++) {
    console.log('C is fun');
  }
}
