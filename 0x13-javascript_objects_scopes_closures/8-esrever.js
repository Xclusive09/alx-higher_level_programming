#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  const length = list.length;

  for (let i = length; i > 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;

}; 
