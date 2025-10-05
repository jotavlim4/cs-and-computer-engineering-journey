/* entendo  acesso a objteos por meio de diferentes notações. */
const preçosFrutas = {"nome": "banana", "valor": 1.5 };
let i = "valor";

console.log(preçosFrutas.valor);
console.log(preçosFrutas[i]);


/* propriedade lenght dos objetos arrays. */
const arr = [1, 2, 4, 4 , 7];
const arr2 = [1, 2, 4, 4 , 7];

console.log(arr.length);
console.log(arr2["length"]);

/* criando propriedades */
let day1 = {
    squirrel: false,
    events: ["work", "touched tree", "pizza", "running"]
};

console.log(day1.wolf);

day1.wolf = false;

console.log("wolf" in day1);
