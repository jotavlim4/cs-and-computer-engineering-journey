/* my solution */

var size = 8;
for(let i = 0; i < size; ++i){
    let output = ""
    for(let j = 0, count = 0; j < size; ++j, ++count){
        if(i % 2 == 0)
            output += (count % 2 == 0 ? " " : "#"); 
        else
            output += (count % 2 == 0 ? "#" : " "); 
    }
    console.log(output);
}

/* book solution */

let size = 8;

let board = "";

for (let y = 0; y < size; y++) {
  for (let x = 0; x < size; x++) {
    if ((x + y) % 2 == 0) {
      board += " ";
    } else {
      board += "#";
    }
  }
  board += "\n";
}

console.log(board);