#!/usr/bin/node
exports.esrever = function (list) {
  let i = 1;
  const lenList = list.length;
  const newList = [];
  while (i <= lenList) {
    newList.push(list[lenList - i]);
    ++i;
  }
  return (newList);
};
