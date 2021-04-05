// Day 1 - Triple Add
// Write a fucntion that returns total of all 3 numbers added together
// Curried version
function tripleAdd(num1) {
  return function (num2) {
    return function (num3) {
      return num1 + num2 + num3;
    };
  };
}

function tripleAdd1(num1, num2, num3) {
  return num1 + num2 + num3;
}

tripleAdd(10)(20)(30);
// returns total of all 3 numbers added together
tripleAdd1(10, 20, 30);
// returns total of all 3 numbers added together

function quadrupleAdd(num1) {
  return function (num2) {
    return function (num3, num4) {
      return num1 + num2 + num3 + num4;
    };
  };
}

quadrupleAdd(10)(20)(30, 40);

// Day 2 -
