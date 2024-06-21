#!/usr/bin/node
// exports.converter = function(base) {
//	return base.toString(base);
//};

const converter = (base) => {
  const convertFromDecimal = (decimal) => {
    return decimal.toString(base);
  };

  const convertToDecimal = (number) => {
    return parseInt(number, base);
  };

  const setBase = (newBase) => {
    base = newBase;
  };

  return {
    convertFromDecimal,
    convertToDecimal,
    setBase
  };
};

module.exports = { converter };

