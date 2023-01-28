function verificar() {
let data = new Date()
let ano = data.getFullYear()
let fano = document.getElementById('txtano')
let res = document.querySelector('div#res')
if(fano.value.length == 0 ||  fano.value > ano) {
    window.alert('Erro, Verifique os dados e tente novamente')


} else {
    let fsex = document.getElementsByName('radsex')
    let idade = ano - Number(fano.value)
    let genero = ''
    let img = document.createElement('img')
    img.setAttribute('id', 'foto')
    if(fsex[0].checked){
        genero = 'homem'
        if (idade >=0 && idade < 10 ) {
            //criança
            img.setAttribute('src', 'criança m.png')
        } else if (idade < 21){
            // jovem
            img.setAttribute('src', 'homem m .png')
        } else if (idade < 50){
            //adulto
            img.setAttribute('src', 'homem.png')
        } else{
            //idoso
            img.setAttribute('src', 'homem velho.png')
        }

    } else if (fsex[1].checked){
        genero = 'mulher'
        if (idade >=0 && idade < 10 ){
            //criança
            img.setAttribute('src', 'criança f.png')
        } else if (idade < 21){
            // jovem
            img.setAttribute('src', 'mulher normal.png')
        } else if (idade < 50){
            //adulto
            img.setAttribute('src', 'mulher jovem.png')
        } else{
            //idoso
            img.setAttribute('src', 'mulher velha .png')
        }
    }    
    res.style.textAlign= 'center'
    res.innerHTML = `Detectamos ${genero} com ${idade} anos`
    res.appendChild(img)
}


}