/* minha solução */

var initial = [1, 2, 3, 4];
var final = [];

function reverseArray(arr){
    let newArr = [];
    for(let value of arr)
        newArr.unshift(value);
    
    return newArr;
}

function reverseArrayInPlace(arr){
    let i, j;
    i = 0; j = arr.length - 1;
    while(i < j){
        let temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
        
        i++; j--;
    }
}


final = reverseArray(initial);
console.log(initial);
console.log(final);

console.log(initial);
reverseArrayInPlace(initial);
console.log(initial);

/* solução do livro */

function reverseArray(array) {
  let output = [];
  for (let i = array.length - 1; i >= 0; i--) {
    output.push(array[i]);
  }
  return output;
}

function reverseArrayInPlace(array) {
  for (let i = 0; i < Math.floor(array.length / 2); i++) {
    let old = array[i];
    array[i] = array[array.length - 1 - i];
    array[array.length - 1 - i] = old;
  }
  return array;
}