var nombre = document.forms['registrar']['nombre'];
var rut = document.forms['registrar']['rut'];
var contrasena = document.forms['registrar']['contrasena'];
var direccion = document.forms['registrar']['direccion'];
var correo = document.forms['registrar']['correo'];


var error_nombre = document.getElementById('error_nombre');
var error_rut = document.getElementById('error_rut');
var error_contrasena = document.getElementById('error_contrasena');
var error_direccion = document.getElementById('error_direccion');
var error_correo = document.getElementById('error_correo');

nombre.addEventListener('textInput', verifica_nombre);
rut.addEventListener('textInput', verifica_rut);
contrasena.addEventListener('textInput', verifica_contrasena);
direccion.addEventListener('textInput', verifica_direccion);
correo.addEventListener('textInput', verifica_correo);



function validaCampos() {
  if (nombre.value.length < 4) {
    nombre.style.border = "1px solid red";
    error_nombre.style.display = "block";
    nombre.focus();
    return false;
  }

  if (rut.value.length < 4) {
    rut.style.border = "1px solid red";
    error_rut.style.display = "block";
    rut.focus();
    return false;
  }

  if (contrasena.value.length < 4) {
    contrasena.style.border = "1px solid red";
    error_contrasena.style.display = "block";
    contrasena.focus();
    return false;
  }
  if (direccion.value.length < 4) {
    direccion.style.border = "1px solid red";
    error_direccion.style.display = "block";
    direccion.focus();
    return false;
  }

  if (correo.value.length < 4) {
    correo.style.border = "1px solid red";
    error_correo.style.display = "block";
    correo.focus();
    return false;
  }

}

function verifica_nombre() {
  if (nombre.value.length >= 3) {
    nombre.style.border = "1px solid silver";
    error_nombre.style.display = "none";
    return true;
  }

}

function verifica_rut() {
  if (rut.value.length >= 3) {
    rut.style.border = "1px solid silver";
    error_rut.style.display = "none";
    return true;
  }
}

function verifica_contrasena() {
  if (contrasena.value.length >= 3) {
    contrasena.style.border = "1px solid silver";
    error_contrasena.style.display = "none";
    return true;
  }
}

function verifica_direccion() {
  if (direccion.value.length >= 3) {
    direccion.style.border = "1px solid silver";
    error_direccion.style.display = "none";
    return true;
  }
}

function verifica_correo() {
  if (correo.value.length >= 3) {
    correo.style.border = "1px solid silver";
    error_correo.style.display = "none";
    return true;
  }
}