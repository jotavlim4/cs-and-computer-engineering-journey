const SCRIPTS = require("../code/chapter/scripts.js");

function dominantDirection(text){
    let scripts = countBy(text, char => {
        let script = characterScript(char.codePointAt(0));
        return script ? script.direction : "none";
    }).filter(({name}) => name != "none"); 
    
    let max = 0;
    let direction = null;
    for(let dir of scripts){
        if(dir.count > max)
            max = dir.count;
            direction = dir.name;
    }
    return direction;
}
