function roundTo(n, step = 1){
    let remaider = n % step;
    return n - remaider + (remaider < step / 2 ? 0 : step);    
};

console.log(roundTo(4.5));