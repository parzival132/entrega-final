var usuario = document.forms['inicio']['usuario'];
var contrasena = document.forms['inicio']['contrasena'];



var error_usuario_log = document.getElementById('error_usuario_log');
var error_contrasena_log = document.getElementById('error_contrasena_log');


usuario.addEventListener('textInput', verifica_usuario);
contrasena.addEventListener('textInput', verifica_contrasena);




function validaInicio() {
  if (usuario.value.length < 4) {
    usuario.style.border = "1px solid red";
    error_usuario_log.style.display = "block";
    usuario.focus();
    return false;
  }

  if (contrasena.value.length < 4) {
    contrasena.style.border = "1px solid red";
    error_contrasena_log.style.display = "block";
    contrasena.focus();
    return false;
  }



}

function verifica_usuario() {
  if (usuario.value.length >= 3) {
    usuario.style.border = "1px solid silver";
    error_usuario_log.style.display = "none";
    return true;
  }

}

function verifica_contrasena() {
  if (contrasena.value.length >= 3) {
    contrasena.style.border = "1px solid silver";
    error_contrasena_log.style.display = "none";
    return true;
  }
}