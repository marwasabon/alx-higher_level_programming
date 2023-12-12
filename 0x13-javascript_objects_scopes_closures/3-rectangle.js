#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (var i = 0; i < this.height; i++) {
      let s = '';
      for (var j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
