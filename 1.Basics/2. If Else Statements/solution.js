let readline = require("readline");

let count = 0;
let testcasesCount = null;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const ifElseStatment = function (inputs) {
  const [n, m] = [...inputs];
  if (n < m) {
    return "lesser";
  } else if (n > m) {
    return "greater";
  } else {
    return "equal";
  }
};

rl.on("line", (data) => {
  if (testcasesCount === null) {
    testcasesCount = parseInt(data);
  } else {
    count++;
    console.log(ifElseStatment(data.split(" ")));
    if (count === testcasesCount) {
      rl.close();
    }
  }
});
