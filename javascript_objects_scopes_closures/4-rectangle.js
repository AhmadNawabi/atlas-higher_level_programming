#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    // Swap width and height using a temporary variable
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Assign the doubled values back to width and height
    this.width *= 2;
    this.height *= 2;
  }
};
