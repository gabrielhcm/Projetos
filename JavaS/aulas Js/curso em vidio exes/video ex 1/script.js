function carregar() {
    let msg = window.document.getElementById('msg')
    let img = window.document.getElementById('imagem')
    let data = new Date()
    let hora = data.getHours()
    //var hora = 15
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora>= 0 && hora < 12) {
        //dia
        img.src = 'dia.png'
        document.body.style.background ='rgb'
    } else if (hora >=12 && hora < 18) {
        //tarde
        img.src = 'tarde.png'
    } else {
        // noite
        img.src = 'noite.png'
    }
}