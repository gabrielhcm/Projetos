function contar() {
    let ini = document.getElementById('txti')
    let fim = document.getElementById('txtf')
    let passo = document.getElementById('txtp')
    let res = document.getElementById('res')
    if (ini.Value.length == 0 || fim.Value.length == 0 || passo.Value.length == 0) {
        window.alert('erro')
    }   else {
        res.innerHTML = 'contando: '
        let i = number(ini.Value)
        let f = number(fim.Value)
        let p = number(passo.Value)
        if (i<f) {
        
            for (let c = i; c <= f;c += p) {
                res.innerHTML += ` ${(c.Value)}`
            }
        }else{
            for(let c = i;c >=f;c-=p){
                res.innerHTML += ` ${(c.Value)}`
            }
        }
        res.innerHTML+=`\u`
    }


}


