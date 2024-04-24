#!/usr/bin/node

/**
 * Represents a rectangle.
 */
class Rectangle {
  /**
   * Creates a rectangle with positive width and height.
   * @param {number} w - The width of the rectangle.
   * @param {number} h - The height of the rectangle.
   */
  constructor(w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
}

module.exports = Rectangle;

