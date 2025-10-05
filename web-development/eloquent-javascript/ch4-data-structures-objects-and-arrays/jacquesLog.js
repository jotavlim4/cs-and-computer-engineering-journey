let journal = [];

function addEntry(events, squirrel){
    journal.push({events, squirrel}); // events e squirrel são propriedades do objeto journal.
}


function phi([n00, n01, n10, n11]){
    let phiCoeficient = (n11 * n00 - n10 * n01)/ Math.sqrt((n10 + n11) * (n00 + n01) * (n01 + n11) * (n00 + n10));
    return phiCoeficient;
}   

// table é um array de número inteiros.
function tableFor(event, journal){
    let table = [0, 0, 0, 0];
    for(let i = 0; i < journal.length; i++){ // as entradas de jornal são objetos com duas propriedades 'events' e 'squirrel'
        let entry = journal[i], index = 0;   // então entry é cada um desses objetos e o loop for itera sobre eles.
                                           
        if(entry.events.includes(event)) // se o 'event' passado como argumento estiver listado na propriedades events da entrada atual o index é incrementado.
            index += 1;                 // entry.events retorna um array de eventos que ocorreram. includes checa se 'event' pertence a esse array
    
        if(entry.squirrel) // o incremento no index torna ele = 1 ou = 2, ou seja, a segunda posição e a terceira.
            index += 2; // a table[1] = ocorrecias onde squirrel é falso e event é true, table[2] = ocorrencias onde squirrel é true e event é false.
        
        table[index] += 1; // incrementa a posição correta em table.
    }
    
    return table;
}


// essa função, basicamente, extrai todos os eventos que estão na propriedade events de cada
// uma das entradas de journal.

function journalEvents(journal){
    let events = [];
    // tem a mesma funcionalidade do loop for tradicional. iterada sobre cada entrada de journal.
    for(let entry of journal){
        for(let event of entry.events) // para cada entrada do array entry.events
            if(!events.includes(event)) // verifico de event está listado nele.
                events.push(event); // se sim, incluo, uma única vez, esse event na lista events.
    }
    return events;
}

for(let event of journalEvents(journal))
    console.log(event + ":", phi(tableFor(event, journal)));


for(let entry of journal){
    if(entry.events.includes("peanuts") && !entry.events.includes("brushed teeth"))
        entry.events.push("peanut teeth");
}