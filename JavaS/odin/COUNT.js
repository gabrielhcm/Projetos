
let resposta = parseInt(prompt("digite um numero pra fizzbuzzar! "));


for(let i = 1; i<=resposta; i++) {
   
    console.log(i);
    if  (i%3 ===0 && i%5===0){
        console.log("FizzBuzz");
    } else if(i%5===0) {
        console.log("buzz");
    } else if (i%3 ===0) {
        console.log("fizz");
    } else{
        console.log(i);
    } 

}

