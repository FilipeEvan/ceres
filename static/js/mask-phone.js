 function maskPhone() {
    element = document.getElementById('phone');
    phone = element.value;

    //Remover tudo o que não é dígito
    phone = phone.replace(/\D/g,"");    // DDI
    //Colocar parênteses em volta dos dois primeiros dígitos
    phone = phone.replace(/^(\d{2})(\d)/g,"($1) $2");   // DDD 
    //Colocar hífen entre o quarto e o quinto dígitos
    phone = phone.replace(/(\d)(\d{4})$/,"$1-$2");    

    // // Remover tudo o que não é dígito
    // phone = phone.replace(/\D/g,"")
    // // Colocar o sinal de mais em volta dos dois primeiros dígitos
    // phone = phone.replace(/^(\d)/,"+$1")
    // // Colocar parênteses em volta dos dois primeiros dígitos
    // phone = phone.replace(/(.{3})(\d)/,"$1($2")
    // phone = phone.replace(/(.{6})(\d)/,"$1)$2")
    // //Colocar hífen entre o quarto e o quinto dígitos
    // if(phone.length == 12) {
    //     phone = phone.replace(/(.{1})$/,"-$1")
    // } else if (phone.length == 13) {
    //     phone = phone.replace(/(.{2})$/,"-$1")
    // } else if (phone.length == 14) {
    //     phone = phone.replace(/(.{3})$/,"-$1")
    // } else if (phone.length == 15) {
    //     phone = phone.replace(/(.{4})$/,"-$1")
    // } else if (phone.length > 15) {
    //     phone = phone.replace(/(.{4})$/,"-$1")
    // }

    element.value = phone
}
   
    