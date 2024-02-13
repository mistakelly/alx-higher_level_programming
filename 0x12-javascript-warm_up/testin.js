const numbers = [87, 12, 56, 32, 9, 74, 21, 63, 45, 18,
  53, 28, 67, 37, 89, 14, 60, 25, 78, 42,
  6, 81, 49, 3, 70, 34, 95, 16, 72, 40];
numbers.sort(function (a, b) {
  return a - b;
});

const secondLargestNumber = numbers[numbers.length - 2];
console.log(secondLargestNumber);
