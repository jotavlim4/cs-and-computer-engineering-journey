/* minha solução */

function range(start, end, step = 1){
    let result = [];
    if(start < end){
        for(let i = start; i <= end; i += step)
            result.push(i);
    } 
    else if(start > end){
        for(let i = start; i >= end; i += (step > 0 ? -step : step))
            result.push(i);
    }
    else
        result.push(start);
    
    return result;
}

sum = (arr) => arr.reduce((acc, curr) => acc + curr, 0);

console.log(range(5, 2, -1));
console.log(sum(range(1, 10)));

/* solução do livro */

function range(start, end, step = start < end ? 1 : -1) {
  let array = [];

  if (step > 0) {
    for (let i = start; i <= end; i += step) array.push(i);
  } else {
    for (let i = start; i >= end; i += step) array.push(i);
  }
  return array;
}

function sum(array) {
  let total = 0;
  for (let value of array) {
    total += value;
  }
  return total;
}