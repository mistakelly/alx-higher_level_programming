const array = process.argv;
const convertedNum = parseInt(array[2], 10);
console.log(`My number: ${convertedNum}`);
if (isNaN(convertedNum)) {
  console.log('Not a number');
}
