#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      process.stdout.write(row + '\n');
    }
  }
};
