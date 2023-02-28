let location1 = 3;
let location2 = 4;
let location3 = 5;

let guess = 0;
let hits = 0;
let guesses = 0;

let issunk=false;

while (issunk == false) {
    guess = prompt("ready, aim, fire! (digite um numero entre 0  e 6!");
    if (guess <0 || guess>6) {
        alert(`digite um numero valido!${guess}`)
    }else {
            guesses++ 
        if (guess === location1|| guess === location2|| guess === location3) {
                alert(`hit! ${hits} ${guesses}${guess}`)
                hits++
            }else {
            alert(`errroou!${guess}${location1}`)
            guesses++ 
            
        }

    }
}