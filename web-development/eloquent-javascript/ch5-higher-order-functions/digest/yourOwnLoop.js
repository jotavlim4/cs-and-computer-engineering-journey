function loop(value, testFunction, updateFunction, bodyFunction){
    let current = value;
    while(testFunction(current)){
        bodyFunction(current);
        current = updateFunction(current);
    }
}
loop(3, n => n > 0, n => n - 1, console.log);