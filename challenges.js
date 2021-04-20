// JavaScript prep questions
// Question 1 - Triple Add Function
// Write a function that returns total of all 3 numbers added together
// Curried version

function tripleAdd(num1) {
  return function (num2) {
    return function (num3) {
      return num1 + num2 + num3;
    };
  };
}

console.log(tripleAdd(10)(20)(30)); // returns 60

// Day 2 - IIFE

//1. What is an IIFE and why are they used?
//2. Code out an Example IIFE that functions properly

// Day 3 - Button
// Refer to jsbin project to function
