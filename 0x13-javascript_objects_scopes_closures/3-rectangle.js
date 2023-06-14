#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let l = 0; l < this.height; l++) {
      let s = '';
      for (let m = 0; j < this.width; m++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
