#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};

// let r1 = new Rectangle(-1, -1);
// console.log(r1);
// console.log(r1.width); // This will be undefined because the constructor didn't initialize the properties properly
// console.log(r1.height); // This will be undefined for the same reason
