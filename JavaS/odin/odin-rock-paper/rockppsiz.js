let numeroround = prompt("digite o numero de rounds!");
let vitorias = 0;
let derrotas = 0;
let empates = 0;
let vencedor =' ';
for (let i= 0; i<numeroround; i++) {

  let pcselec = Math.floor(Math.random() * 3);
  let playerchoice = prompt("digite pedra papel ou tesoura!").toLowerCase();
  function pcchoice() {
    if (pcselec === 0){
      return "papel"
    } else if (pcselec ===1) {
      return "pedra"
    } else if (pcselec===2) {
      return "tesoura"
    }
  } 
  
  pcselec = pcchoice(); 
  function resultado() {
    if (pcselec === "pedra" && playerchoice ==="pedra") {
      return ("empate");
    } else if (pcselec  ==="pedra" && playerchoice==="papel") {
      return ("você ganhou!");
    } else if (pcselec  ==="pedra" && playerchoice==="tesoura") {
      return ("perdeu para o pc!");
    } else if (pcselec  ==="papel" && playerchoice==="pedra") {
      return ("perdeu para o pc!");
    } else if (pcselec  ==="papel" && playerchoice==="tesoura") {
      return ("você ganhou!");
    } else if (pcselec  ==="papel" && playerchoice==="papel") {
      return ("empate");
    } else if (pcselec  ==="tesoura" && playerchoice==="tesoura") {
      return ("empate");
    } else if (pcselec  === "tesoura" && playerchoice=== "papel") {
      return ("perdeu para o pc!");
    } else if (pcselec  ==="tesoura" && playerchoice==="pedra") {
      return ("você ganhou!");
    }

  }
  jogores = resultado();  
  
    if (jogores ==="você ganhou!"){
      vitorias++
    } else if (jogores ==="perdeu para o pc!"){
      derrotas++
    } else if (jogores ==="empate"){
      empates++
    }
     

  console.log(`você escolheu ${playerchoice} e o pc escolheu ${pcselec} , o resultado foi: ${jogores}`);
  console.log(`você ganhou ${vitorias} vezes, perdeu ${derrotas} vezes e empatou ${empates} vezes!`);
  console.log(vencedor)
}
if (vitorias > derrotas) {
  vencedor = "você ganhou do pc no final!"
} else if (derrotas > vitorias) {
  vencedor = "o pc ganhou de você :("
} else if (empates > vitorias && empates > derrotas) {
  vencedor = "vocês ficaram empatados!"
}  
console.log(vencedor)