/* my solution */

var output = "";

for(let i = 0; i < 7; ++i){
    for(let j = 0; j < i; ++j){
        output += "#";
    }
    console.log(output);
    output = "";
}

/* book solution */

for (let line = "#"; line.length < 8; line += "#")
  console.log(line);

