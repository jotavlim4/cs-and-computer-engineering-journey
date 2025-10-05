function multiplier(factor){
    return number => number * factor;
}

twice = multiplier(5);
treeTimes = multiplier(5);
fourTimes = multiplier(5);

console.log(twice(2)); // 10
console.log(treeTimes(3)); // 15
console.log(fourTimes(4)); // 20


/* como funcionam clousures */

/* A função multiplier retorna uma outra função. Essa função retornada "captura" o valor do parâmetro `factor` 
do seu ambiente pai (a função multiplier). Dessa forma, mesmo após a função multiplier encerrar sua execução e 
suas variáveis temporárias serem liberadas, a função retornada ainda consegue acessar e "se lembrar" do valor de `factor`.
Em seguida, associamos essa função retornada a uma variável (como `twice`, `treeTimes` ou `fourTimes`), 
o que nos permite chamá-la a qualquer momento, e ela sempre usará o valor de `factor` que foi capturado no momento de sua criação.
*/