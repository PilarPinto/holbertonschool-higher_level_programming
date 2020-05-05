#!/usr/bin/node

exports.addMeMaybe = function (a, funct) {
  a = a + 1;
  return (funct(a));
};
