// Code Wars challenges. 8Kyu difficutly
// Easy Challanges that I can solve in other languages as well

// Challenge 1 - Convert a Number to a String!
function numberToString(num) {
  const newString = num.toString();
  return newString;
}

console.log(numberToString(67));

// Challange 2 - Convert Boolean values to strings 'Yes' or 'No'.

function boolToWord(bool) {
  if (bool === true) {
    return "Yes";
  } else {
    return "No";
  }
}

console.log(boolToWord(true));
console.log(boolToWord(false));
