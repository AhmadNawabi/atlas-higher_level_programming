#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w === 0 || !Number.isInteger(w) || h === 0 || !Number.isInteger(h)) {
      w = 0;
      h = 0;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    // Swap width and height using a temporary variable
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // Assign the doubled values back to width and height
    this.width *= 2;
    this.height *= 2;
  }
};
