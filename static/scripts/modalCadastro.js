let modal = document.getElementById('signupModal');
let btnSignup = document.getElementById('signup');
let closex = document.getElementsByClassName('close')[0];
//Para login
let btnSignin = document.getElementById('signin');
let cad_log = document.getElementById('cad-log');
let pergunta = document.getElementById('pergunta');
let acao = document.getElementById('acao');
let enviar = document.getElementById('enviar');
let conf = document.getElementById('confirmar-senha');
let confir = document.getElementById('confir');
//
let btncadastro = document.getElementById('btncadastro');
let btnlogin = document.getElementById('btnlogin');
let formu = document.getElementById('formu');

modal.style.display='none';

btnSignup.onclick = function() {
    formu.reset();
    btnlogin.style.display = 'none';
    btnlogin.disabled=true;
    btncadastro.style.display = 'block';
    btncadastro.disabled=false;
    document.getElementById('confir').required=true;
    conf.style.display = 'flex';
    pergunta.innerHTML = "Já possui uma conta?";
    acao.innerHTML = "Entrar";
    cad_log.innerHTML = 'Cadastre-se';
    modal.style.display = 'flex';
}

btnSignin.onclick = function() {
    formu.reset();
    btnlogin.style.display = 'block';
    btnlogin.disabled=false;
    btncadastro.style.display = 'none';
    btncadastro.disabled=true;
    document.getElementById('confir').required=false;
    conf.style.display = 'none';
    pergunta.innerHTML = "Não possui uma conta?";
    acao.innerHTML = "Registre-se";
    cad_log.innerHTML = 'Bem-Vindo';
    modal.style.display = 'flex';
}

closex.onclick = function() {
    modal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

//para signin

document.getElementById('senha').onkeyup = function() {
    if (document.getElementById('confir').required==true && document.getElementById('senha').value!=document.getElementById('confir').value  && btncadastro.disabled==false) {
        console.log('batata');
        btncadastro.disabled = true;
        document.getElementById('msg').innerHTML = 'As senhas não batem!'
    } 
    if (document.getElementById('confir').required==true && document.getElementById('senha').value==document.getElementById('confir').value && btncadastro.disabled==true) {
        btncadastro.disabled = false;
        document.getElementById('msg').innerHTML = ''
    }
}

document.getElementById('confir').onkeyup = function() {
    if (document.getElementById('confir').required==true && document.getElementById('senha').value!=document.getElementById('confir').value  && btncadastro.disabled==false) {
        console.log('batata');
        btncadastro.disabled = true;
        document.getElementById('msg').innerHTML = 'As senhas não batem!'
    } 
    if (document.getElementById('confir').required==true && document.getElementById('senha').value==document.getElementById('confir').value && btncadastro.disabled==true) {
        btncadastro.disabled = false;
        document.getElementById('msg').innerHTML = ''
    }
}