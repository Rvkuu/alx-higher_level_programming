#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let l = 0; l < this.height; l++) {
      let s = '';
      for (let m = 0; m < this.width; m++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
