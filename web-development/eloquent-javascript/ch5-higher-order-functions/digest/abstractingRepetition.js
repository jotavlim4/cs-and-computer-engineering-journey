/* um forma de imprimir um valor n vezes */
var n = 10;
for(let i = 0; i < n; i++)
    console.log(i);
    
/* poderiamos escrever uma função */
function printNtimes(n){
    for(let i = 0; i < n; i++)
        console.log(i);
}

/* se quisermos fazer outra N vezes que não seja imprimir os valores de 0 a 9? */
/* podemos então criar uma função mais geral, para isso ela precisará receber uma outra */
/* função como argumento */
function doNtimes(n, action){
    for(let i = 0; i < n; i++)
        action(i);
}

console.log('\n');

var arr = [];
doNtimes(n, i => arr.push(i*i));
console.log(arr);
console.log('\n');

arr = [];
doNtimes(n, i => arr.push(i+1));
console.log(arr);
console.log('\n');

/* note doNtimes se tornou uma função mais geral, que pedomos utilizar de diferentes maneiras. isso é abstrair repetição. */