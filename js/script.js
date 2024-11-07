const pantalla = document.querySelector('.pantalla')
let operacionpendiente = '';
let numeroAnterior = '';
let operadorActual = null;
let reiniciarPantalla = false;

function agregar(valor){
    if(reiniciarPantalla){
        pantalla.value = '';
        reiniciarPantalla = false;
    }
    if(['+', '-','*', '/', '√'].includes(valor)){
        if(operadorActual !== null){
            calcular();
        }
        numeroAnterior = pantalla.value;
        operadorActual = valor;
        reiniciarPantalla = true;
    } else{
        pantalla.value += valor;
    }

}

function limpiar(){
    pantalla.value = '';
    operacionpendiente = '';
    numeroAnterior = '';
    operadorActual = null;
}

function retroceso(){
    pantalla.value = pantalla.value.slice(0, -1);
}

function calcular(){
    if(operadorActual === null)
        return;

    const numero1 = parseFloat(numeroAnterior);
    const numero2 = parseFloat(pantalla.value);

    if (isNaN(numero1) || isNaN(numero2)){
        pantalla.value = 'Error'
        setTimeout(limpiar, 1500)
        return;
    }

    let resultado;

    switch(operadorActual){
        case '+':
            resultado = numero1 + numero2;
            break;
        case '-':
            resultado = numero1 - numero2;
            break;
        case '*':
            resultado = numero1 * numero2;
            break;
        case '/':
            resultado = numero1 / numero2;
            break;
        case '√':
            resultado = Math.sqrt(numero2);
            break;
        default:
            pantalla.value = 'Error';
            return;
    }
    
    //Redondear a 8 decimales
    resultado = Math.round(resultado * 100000000) / 100000000;
    pantalla.value = resultado;
    operadorActual = null;
    numeroAnterior = '';
    reiniciarPantalla =  true;
}

//Manejo de eventos del teclado

document.addEventListener('keydown', (event) =>{
    event.preventDefault();
    const key = event.key;

    //numeros y operadores 
    if(/[0-9\+\-\*\/\.]/.test(key)){
        agregar(key);
    }

    //tecla enter para calcular
    else if (key === 'Enter'){
        calcular();
    }

    //tecl escape para limpiar
    else if ( key === "Escape"){
        limpiar();
    }

    //tecla backspace  para borrar el ultimo caracter
    else if (key === 'Backspace'){
        retroceso();
    }

    //tecla para calcular raíz cuadrada
    else if(key === 'r'){
        agregar('√')
    }

    
})

