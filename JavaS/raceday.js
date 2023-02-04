let raceNumber = Math.floor(Math.random() * 1000);


const registrocedo = false;
 let runnersage = 18;

    if (runnersage >18 && registrocedo === true){
            raceNumber += 1000;
    } if  (runnersage > 18 && registrocedo === true){
            raceNumber += 1000;
        console.log(`seu numero de registro é ${raceNumber} e você irá correr as 9:30am.`)
    } else if (runnersage>18 && registrocedo===false){
            raceNumber += 1000;
            console.log(`seu numero de registro é ${raceNumber} e você irá correr as 11:00am.`) 
    }else if (runnersage<18){
        console.log(`seu numero de registro é ${raceNumber} e você irá correr as 12:30 pm.`)
    } else {
        console.log('você tem que ir até a mesa para resolver seus problemas com idade!')
    }        
