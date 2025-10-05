const everyWithFor = (array, test) => {
    for(let value of array){
        if(!test(value))
            return false;
    }    
    return true;
}

const everyWithSome = (array, test) => {
    return !array.some(a => test(a));   // ~(E(x) tal que P(x)) <=> (V(x) tal ~P(x))
}


console.log(everyWithFor([1, 2, 3, 4, -6], a => a > 0));
console.log(everyWithSome([1, 2, 3, 4, -6], a => a > 0));
