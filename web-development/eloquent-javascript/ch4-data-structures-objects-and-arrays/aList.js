/* minha solução */

function arrayToList(arr){
    let list = {};
    if(arr.length === 0){
        return null;
    }
    else{
        list.value = arr[0];
        list.rest = arrayToList(arr.slice(1));
        return list;
    }
}

function listToArray(list){
    let array = [];
    if(list.rest === null)
        return [list.value];
    else{
        return [list.value].concat(listToArray(list.rest));
    }
}


function prepend(value, list){
    let newList = {};
    newList.value = value;
    newList.rest = list;
    
    return newList;
}

function nth(list, number){
    if(number == 0)
        return list.value;
    else if(list.rest == null)
        return undefined;
    else{
        return nth(list.rest, number - 1);
    }
}

/* solução do autor */

function arrayToList(array) {
  let list = null;
  for (let i = array.length - 1; i >= 0; i--) {
    list = {value: array[i], rest: list};
  }
  return list;
}

function listToArray(list) {
  let array = [];
  for (let node = list; node; node = node.rest) {
    array.push(node.value);
  }
  return array;
}

function prepend(value, list) {
  return {value, rest: list};
}

function nth(list, n) {
  if (!list) return undefined;
  else if (n == 0) return list.value;
  else return nth(list.rest, n - 1);
}

