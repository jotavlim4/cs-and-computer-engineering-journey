/* minha solução */
function countChar(str, ch){
    let countCh = 0;
    for(let i = 0; i < str.length; ++i){
        if(str[i] === ch)
            countCh++;
    }  
    return countCh;
}

function countBs(str){
    return countChar(str, 'B');
}

console.log(countBs("BolaBolabola"));

/* solução do autor */
function countChar(string, ch) {
  let counted = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] == ch) {
      counted += 1;
    }
  }
  return counted;
}

function countBs(string) {
  return countChar(string, "B");
}
