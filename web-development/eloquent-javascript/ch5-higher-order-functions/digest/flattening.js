const flatten = (array) => {
 return array.reduce((acc, [first, ... rest]) => acc.concat([first, ... rest]), []); 
};

console.log(flatten([[1,2], [3, 4], [5, 6], [7, 8]])); 