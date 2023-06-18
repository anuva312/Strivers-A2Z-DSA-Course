let readline = require("readline");

let count = 0;
let testcasesCount = null;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const checkPrimeBruteForce = function (num) {
  if (num < 2) return "No";
  for (i = 2; i < n; i++) {
    if (num % i === 0) {
      return "No";
    }
  }
  return "Yes";
};

const checkPrime = function (num) {
  if (num < 2) return "No";
  for (i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return "No";
    }
  }
  return "Yes";
};

rl.on("line", (data) => {
  if (testcasesCount === null) {
    testcasesCount = parseInt(data);
  } else {
    count++;
    console.log(checkPrime(parseInt(data)));
    if (count === testcasesCount) {
      rl.close();
    }
  }
});
