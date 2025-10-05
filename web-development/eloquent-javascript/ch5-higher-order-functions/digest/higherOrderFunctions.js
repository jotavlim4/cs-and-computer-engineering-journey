/* doNtimes da seção antetior renomeada para repeat */
function repeat(n, action){
    for(let i = 0; i < n; i++)
        action(i);
}
/* funcoes de ordem superior recebem funções como parametros/argumentos e também retornando funções */
function greaterThan(n){
    return m => m > n;
}

/* aqui, basicamente, estamos usando a função greaterThan 
para criar uma nova função que verificar se um número é maior que 10*/
let greaterThan10 = greaterThan(10); /* o corpo da função é m => m > 10 */
console.log(greaterThan10(20)); // -> true
console.log(greaterThan10(10)); // -> false
console.log(greaterThan10(2)); // -> false

/* funcoes que mudam funcoes */

function noisy(f){
    return (...args) => {
        console.log("calling with", args);
        let result = f(...args);
        console.log("called with", args, "returned", result);
        return result;
    }
}


/* max tem como parametro (...args) */
/* max tem como corpo tudo que está entre {} da função noisy */
let max = noisy(Math.max); 
max(1, 2, 3, 4, 5); 

/* podemos fazer também */
noisy(Math.max)(1, 2, 3, 4, 5);

/* uma função que criar um 'novo' controle de fluxo */
function unless(test, then){
    if(!test)
        then();
}

repeat(40, n => unless(n % 2 == 1, () => console.log(n, "is even!")));

/* uso do forEach */
/* o metodo forEach, usa cada elemento do array como argumento de uma função, ou seja, é uma função que aplica
uma outra função em cada elemento do array, isto é, se comporta como um função de ordem superior */
arr = [];
[1, 2, 3, 4, 5, 6].forEach(number => arr.push(number*number));
console.log(arr);

