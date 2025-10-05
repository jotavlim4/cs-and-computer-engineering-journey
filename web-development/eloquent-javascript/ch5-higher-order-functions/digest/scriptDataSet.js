const SCRIPTS = require("../code/chapter/scripts");

/* simulando a implementação do método filter */
function filter(array, test){
    let passed = [];
    for(let element of array){
        if(test(element)){
            passed.push(element); 
        }
    }
    return passed;
}

/* simulando a implementação do método map */
function map(array, transform){
    let mapped = [];
    for(let element of array){
        mapped.push(transform(element))
    }
    return mapped;
}

/* simulando a implementação do método reduce */
function reduce(array, combine, start){
    let current = start;
    for(let element of array){
        current = combine(current, element); /* combine é uma função */
    }
    return current;
}

/* funcao que conta a quantidade de caracteres de um script */
function characterCount(script){ /* script é um objeto */
    return script.ranges.reduce( /* script.ranges é um array de arrays com dois elementos cada */
    (count, [from, to]) => { /* usa desestruturação */
        return count + (to - from);
    }, 0);    
}


function average(array){
    return array.reduce((a, b) => a + b, 0);
} 

/* filtra os scripts que ainda são utlizados utilzando o método filter */
/* em seguida, acessa a propriedade year de cada um scripts ativos e constroi um array */
/* esse array é usado como argumento de average que retornada a média */
/* que por fim é arredondado. */
//console.log(Math.round(average(
//SCRIPTS.filter(s => s.living).map(s => s.year))));


function characterScript(code){
    for(let script of SCRIPTS){
        if(script.ranges.some((
        ([from, to]) =>{ 
        return code >= from && code < to;})))
            return script;
    }
    return null;
}

function countBy(items, groupName){
    let counts = [];
    for(let item of items){
        let name = groupName(item);
        let know = counts.findIndex(c => c.name == name); //verifica aquele nome já ocorre em counts 
        if(know == -1){ // se nao cria um novo objeto
            counts.push({name, count:1});
        }
        else{
            counts[know].count++; //se sim incrementa a quantidade de vezes que ele ocorre.
        }
    }
    return counts;
}

function textScripts(text){
    let scripts = countBy(text, char => {
        let script = characterScript(char.codePointAt(0));
        return script ? script.name : "none";
    }).filter(({name}) => name != "none");
    
    let total = scripts.reduce((n, {count}) => n + count, 0);
    if(total == 0) return "No scripts found!";
    
    return scripts.map(({name, count}) =>{
        return `${Math.round(count * 100 / total)}% ${name}`;
    }).join(", ");
    
}

console.log(textScripts('"João Victor Lima Silva! 𐔰𐔱𐔵 ڳڻھہة ۅۆ" אבגד '));




/* ou simplesmente: */
let rtlScripts = SCRIPTS.filter(script => script.direction == "rtl"); /* filter é um método para arrays */
rtlScripts = rtlScripts.map(script => script.name);
