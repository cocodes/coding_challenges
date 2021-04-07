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

// Day 2 - IIFE

//1. What is an IIFE and why are they used?
//2. Code out an Example IIFE that functions properly

(function doubleNumber(num) {
  return num * 2;
})(10);

(function () {
  function getTotal(a, b) {
    return a + b;
  }

  var $ = "currency";

  if (true) console.log("hello world");
})();

// Day 3 - Button
// Refer to jsbin project to function

function createButtons() {
  for (var i = 1; i <= 5; i++) {
    var body = document.getElementsByTagName("BODY")[0];
    var button = document.createElement("BUTTON");
    button.innerHTML = "Button " + i;
    button.onclick = function () {
      alert("This is button " + i);
    };
    body.appendChild(button);
  }
}

createButtons();
