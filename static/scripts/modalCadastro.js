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
let error = document.getElementById('error');
let cab = document.getElementById('cab');

let userExists = document.getElementById('userExists');

let nameError = error.getAttribute('name');

if (nameError != '1' && nameError!='2') {
    modal.style.display='none';
    btnlogin.style.display = 'none'
    btncadastro.style.display = 'none'
    userExists.style.display = 'none';
    conf.style.display = 'none';
    document.getElementById('confir').required=false;
} else {
    if (nameError=='1') {
        modal.style.display='flex';
        userExists.style.display = 'flex';
        btncadastro.style.display = 'block';
        btnlogin.style.display = 'none'
        pergunta.innerHTML = "Já possui uma conta?";
        acao.innerHTML = "Entrar";
        cad_log.innerHTML = 'Cadastre-se';
        document.getElementById('confir').required=true;
        conf.style.display = 'flex';
    } else if (nameError='2') {
        modal.style.display='flex';
        userExists.style.display = 'flex';
        btnlogin.style.display = 'block';
        btncadastro.style.display = 'none';
        document.getElementById('confir').required=false;
        conf.style.display = 'none';
        pergunta.innerHTML = "Não possui uma conta?";
        acao.innerHTML = "Registre-se";
        cad_log.innerHTML = 'Bem-Vindo';
    }    
}




btnSignup.onclick = function() {
    userExists.style.display = 'none';
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
    userExists.style.display = 'none';
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
        btncadastro.disabled = true;
        document.getElementById('msg').innerHTML = 'As senhas não batem!'
    } 
    if (document.getElementById('confir').required==true && document.getElementById('senha').value==document.getElementById('confir').value && btncadastro.disabled==true) {
        btncadastro.disabled = false;
        document.getElementById('msg').innerHTML = ''
    }
}