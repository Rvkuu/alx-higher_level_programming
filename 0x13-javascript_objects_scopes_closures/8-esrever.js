#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let h = 0;
  while ((len - h) > 0) {
    const aux = list[len];
    list[len] = list[h];
    list[h] = aux;
    h++;
    len--;
  }
  return list;
};
