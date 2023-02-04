let userName = 'bniel';
const userQuestion = 'arroz é bom?';
 let randomNumber = Math.floor(Math.random()* 8);
let eighBall = '';
userName ? console.log(`Hello,${userName}!`) : console.log('Hello');
console.log(`${userName} você perguntou: ${userQuestion}`);

switch(randomNumber) {
    case randomNumber = 0:
        eighBall ='It is certain';
    break;
    case randomNumber = 1:
        eighBall ='It is decidedly so';
       
    break;
    case randomNumber = 2:
      eighBall='Reply hazy try again';
    break;
    case randomNumber = 3:
      eighBall ='Cannot predict now';
    break;
    case randomNumber = 4:
           eighBall ='Do not count on it';
    break;
    case randomNumber = 5:
      eighBall ='My sources say no';
    break;
    case randomNumber = 6:
       eighBall ='Outlook not so good';
    break;    
    case randomNumber = 7:
       eighBall ='Signs point to yes';
    break;    

    

}
console.log(eighBall)   