let readline = require("readline");

let count = 0;
let testcasesCount = null;
let choice = null;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const switchCase = function (choice, inputs) {
  switch (choice) {
    case 1:
      return Math.PI * inputs[0] * inputs[0];
    case 2:
      return inputs[0] * inputs[1];
    default:
      return "Choice should be either 1 or 2";
  }
};

rl.on("line", (data) => {
  if (testcasesCount === null) {
    testcasesCount = parseInt(data);
  } else {
    if (choice === null) {
      count++;
      if (data == 1 || data == 2) {
        choice = parseInt(data);
      } else {
        console.log("Choice should be either 1 or 2");
      }
    } else {
      console.log(switchCase(choice, data.split(" ")));
      choice = null;
    }
    if (choice === null && count === testcasesCount) {
      rl.close();
    }
  }
});
