var numero = prompt('digite um número: ')

if (numero > 10){
    alert(numero + 'é maior que 10')
}else if(numero<10){
    alert(numero + "é menor que 10")
}else{
    alert(numero + "é igual a 10")
}


alert("parte 2.2")
var num1 = prompt("digite um número");
var num2 = prompt("digite um número");

num1 = parseInt (num1);
num2 = parseInt (num2);

alert(num1+num2)

alert("parte 2.3")

var num1 = prompt("valor1")
var operacao = prompt("operação a ser realizada (+, -, *, /): ")

num1 = parseFloat(num1);
num2 = parseFloat(num2);

switch(operacao){
    case '+':
        alert(num1 + num2);
        break;
    case '-':
        alert(num1 - num2);
        break;
    case '*':
        alert(num1 * num2);
        break;
    case '/':
        alert(num1/num2);
        break;
    default:
        alert("ERRO FATAL! OPERAÇÃO INVÁLIDA");
}

alert("parte 2.4")

var nome = prompt("digite um nome: ")
var valor = prompt("Número de vezes")

valor = parseInt(valor)

for (var i = 1; i<=valor; i++) {
    alert(nome);
}

alert("parte 2.5")

var nome = prompt("Digite seu nome: ")
var end = prompt("Digite seu endereço: ")
var email = prompt("Digite seu email: ")

var obj = {
    propriedadenome: nome,
    propriedadeend: end,
    propriedadeemail: email   
}

alert(obj.propriedadenome);
alert(obj.propriedadeend);
alert(obj.propriedadeemail);