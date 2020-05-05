#!/usr/bin/node

exports.callMeMoby = function (a, funct) {
  let str = '';
  for (let ind = 0; ind < a; ind++) {
    str += funct();
  }
  return (str);
};
