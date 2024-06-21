#!/usr/bin/node
logCount = 0;
exports.logMe = function (item) {
  console.log(logCount++, ':', item);
};
