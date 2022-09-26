const form = document.getElementById("formularioCadastro");
const senha = document.getElementById("password");
const senhaConfirmacao = document.getElementById("password_confirm");


form.addEventListener("submit", (e) => {
    e.preventDefault();
  
    checarInputs();
});



function checarInputs() {
    const senhaValor = senha.value;
    const senhaConfirmacaoValor = senhaConfirmacao.value;

    if(senhaValor != senhaConfirmacaoValor){
        alert("Senhas não coincidem")
    }

}