function validarNombre() {
    let nom=document.getElementById("txtNombre").value;
    nom = nom.trim();
    if(nom.length >= 3) {
        registro.setNombre(nom);
        return true;
    } else {
        alert('Nombre invalido');
        return false;
    }
}

function validarPass() {

    let pass=document.getElementById("pwdPass").value;
    let pass1=document.getElementById("pwdConfirmPass").value;
    pass = pass.trim();
    pass1 = pass1.trim();

    if(pass.length>=4 && pass==pass1){
        registro.setPassword(pass);
        return true;
    } else {
        alert('Contraseña invalida');
        return false;
    }
}

function validarEmail() {
    let email=document.getElementById("txtEmail").value;
    email = email.trim();
    if(email.length>=3 && email.includes('@')){
        registro.setEmail(email);
        return true;
    } else {
        alert('Email invalido');
        return false;
    } 
}

function validar() {
    
    registro = new registro();

    let resp;
    resp=validarNombre();
    if (resp==false){
        return false;
    }

    resp=validarEmail();
    if(resp==false){
        return false;
    }

    resp=validarPass();
    if(resp==false){
        return false;
    }
    
    localStorage.setItem('clientes',JSON.stringify(registro));
    location.href = 'index.html';
    alert('Registrado correctamente.');
    return true;
    
}






function login() {
    let email = document.getElementById("txtEmail").value;
    let pass = document.getElementById("pwdPass").value;

    let clientes = localStorage.getItem('clientes');
    let datos = JSON.parse(clientes);

    if (email.trim() === datos.email && pass.trim() === datos.password) {
        alert('Bienvenid@ de vuelta ' + datos.nombre);

        let persona = {email: email, pass: pass};
        localStorage.setItem('login', JSON.stringify(persona));
        location.href = 'index.html';
    } else {
        alert('Contraseña incorrecta');
    }
}