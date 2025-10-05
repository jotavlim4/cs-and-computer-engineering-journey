function deepEqual(obj1, obj2){
    /* verifica igualdades de objetos primitivos como int, bool, float e strings. */
    /* verifica também, se são objetos que apontam para o mesmo endereço de memória. */
    if(obj1 === obj2) return true;
    
    /* se pelo menos um deles é null ou não é objeto já retornamos false. */
    if(obj1 === null || obj2 === null || typeof(obj1) !== "object" || typeof(obj2) !== "object") return false;
    
    /* nesse ponto, sabemos que ambos são objetos */
    /* então criamos um array de todas as suas propriedades */
    let obj1Keys = Object.keys(obj1);
    let obj2Keys = Object.keys(obj2);
    
    /* se o tamanho desse array é diferente, significa que eles não tem as mesmas propriedades */
    if(obj1Keys.length !== obj2Keys.length) return false;
    
    /* uma vez que os tamanhos são os mesmos, vamos verificar se as propriedades são as mesmas e se */
    /* os valores são o mesmo */
    for(let key of obj1Keys){  
        /* ou seja para cada chave do array de chaves de obj1 verifico se essa chave existe no array de chaves de obj2 */
        /* em seguida, verificamos recursivamente se o valor associado a essa esse par de chaves são iguais. */
        /* se ocorrer de pelo menos uma das chaves e os os valores associadas a eles não forem iguais, imediatamente retornamos false */
        if(!obj2Keys.includes(key) || !deepEqual(obj1[key], obj2[key])) /* dá logica: ~p v ~q => ~(p ^ q) */
            return false;
    }
    /* se chegou até esse ponto e não retornou false é pq são de fato iguais. */
    return true;
}