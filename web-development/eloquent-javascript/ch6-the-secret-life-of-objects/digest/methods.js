/* a variável 'this' aponto para o objeto que chama o método. */
function speak(line){
    console.log(`The ${this.type} rabbit says '${line}'`);
}

/* speak é um método dos objetos whiteRabbit/hungryRabbit */
let whiteRabbit = {type: "white", speak};
let hungryRabbit = {type: "hungry", speak};

whiteRabbit.speak("Oh my ears and whiskers, " + "how late it's getting! ");
hungryRabbit.speak("I could use a carrot right now.");

/* usando o método call para funções */
/* esse o primerio argumento desse método é o objeto que será 'atribuido' a 'this' */
speak.call(whiteRabbit, "Burp!");

/* this e o escopo de funções */
/* funciona para arrow function, pois ela enxerga o escopo da função que a chama */
function normalize(){
    console.log(this.coords.map(n => n / this.length));
}
/* mas ... */
/* funções definidas com a keyword function não enxergam */

normalize.call({coords: [0,2, 3], length: 5});
