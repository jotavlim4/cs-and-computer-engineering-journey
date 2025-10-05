function minus(a, b){
    if(b === undefined) return -a;
    else return a - b;
}
console.log(minus(10));
console.log(minus(10, 5));


const arrowMinus = (a, b) => {
    if(b === undefined) return -a;
    else return a - b;
}

console.log(arrowMinus(10));
console.log(arrowMinus(10, 5));