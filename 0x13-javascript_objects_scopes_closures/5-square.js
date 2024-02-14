#!/usr/bin/Node
/*
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

You must use the class notation for defining your class and extends
The constructor must take 1 argument: size
The constructor of Rectangle must be called (by using super())

 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let pattern = '';
      for (let j = 0; j < this.width; j++) {
        pattern += 'X';
      }
      console.log(pattern);
    }
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Pass size for both width and height
    this.size = size;
  }
}

module.exports = Square;
