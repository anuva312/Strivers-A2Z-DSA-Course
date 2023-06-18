let readline = require("readline");

let count = 0;
let testcasesCount = null;

const getReverse = function (x) {
  let num = Math.abs(x);
  let isNegative = x < 0;
  let reversedNum = 0;
  let flag = false;
  while (num > 0) {
    reversedNum = reversedNum * 10 + (num % 10);
    num = Math.floor(num / 10);
    if (reversedNum > 0x7fffffff) {
      flag = true;
      break;
    }
  }
  return flag ? 0 : isNegative ? -reversedNum : reversedNum;
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (data) => {
  if (testcasesCount === null) {
    testcasesCount = parseInt(data);
  } else {
    count++;
    console.log(getReverse(data));
    if (count === testcasesCount) {
      rl.close();
    }
  }
});
