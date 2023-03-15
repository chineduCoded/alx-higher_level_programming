#!/usr/bin/node
exports.converter = function (base) {
  function convert(number, base) {
    if (number < base) {
      return number.toString();
    }
    let remainder = number % base;
    let quotient = Math.floor(number / base);
    return convert(quotient, base) + remainder.toString();
  }
  return convert;
}
