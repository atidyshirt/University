console.log("Start");

function g(input) {
  return input + 1;
}

let a_function = g;
console.log(a_function); // logs out [Function: g]
console.log("The result of g(2) is :", g(2));

async function f(input) {
  return input + 1;
}

let another_function = f;
console.log(another_function); // [Asyncfunction: f]
console.log("The result of f(2) is: ", f(2)); // returns Promise { 3 }

f(10).then(function(result) {
  console.log("The result of f() is: " + result); // returns 11
});

another_function(100).then(function(result) {
  console.log("The result of another_function (f()) is: " + result);
});
