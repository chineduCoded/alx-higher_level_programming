#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is not positive, create an empty object
      return {};
    } else {
      // Initialize the instance attributes width and height
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
