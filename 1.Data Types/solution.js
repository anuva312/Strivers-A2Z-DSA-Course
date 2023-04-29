let readline = require("readline");

let inputs = [];
let count = 0;

const findDataTypeLength = function (datatype) {
  switch (datatype) {
    case "Character":
      return 1;
    case "Integer":
      return 2;
    case "Long":
    case "Float":
      return 4;
    case "Double":
      return 8;
    default:
      return 0;
  }
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (data) => {
  inputs.push(data);
  if (inputs.length > 1) {
    console.log(findDataTypeLength(inputs[++count]));
    if (count === parseInt(inputs[0])) {
      rl.close();
    }
  }
});
