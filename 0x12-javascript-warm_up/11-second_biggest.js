#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('0');
} else if (args.length === 1) {
  console.log('0');
} else {
  const arg = [];
  for (let i = 0; i < args.length; i++) {
    const argNum = parseInt(args[i], 10);
    // copy the array into anther array
    arg.push(argNum);
  }
  // sort the element in asceding order
  arg.sort(function (a, b) {
    return a - b;
  });
  // get the length of the element
  const secLargestElement = arg[arg.length - 2];
  console.log(secLargestElement);
}
