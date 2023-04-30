let readline = require("readline");

let count = 0;
let testcasesCount = null;

const findDataTypeLength = function (datatype) {
  switch (datatype) {
    case "Character":
      return 1;
    case "Integer":
    case "Float":
      return 4;
    case "Long":
    case "Double":
      return 8;
    default:
      return -1;
  }
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
    console.log(findDataTypeLength(data));
    if (count === testcasesCount) {
      rl.close();
    }
  }
});
