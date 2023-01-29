let num = document.querySelector('input#adnum')
let lista = document.querySelector('select#lista')
let res = document.querySelector('div#res')
let valores = []

function isnumero(n) {
    if (Number(n)>=1 && Number(n)<= 100){
        return true
    } else {
        return false
    }
}

function inlista(n) {
    if(l.indexOf(Number(n))!=-1) {
        return true 

    }else {
        return false
   
    }
}

function adicionar() {
    if(isnumero(num.value)&& !inlista(num.value,valores)){

    }else{
        window.alert('valor invalido ou ja encontrado na lista')
    }
}