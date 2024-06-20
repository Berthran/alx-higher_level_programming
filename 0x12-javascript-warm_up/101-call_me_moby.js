#!/usr/bin/node
exports.callMeMoby = function (a, func) {
  let i = 0;
  for (i = 0; i < a; i++) {
    func();
  }
};
