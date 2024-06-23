function validarCampos() {
    var camposNN = document.querySelectorAll('.NN');
    var error = false;

    for (var i = 0; i < camposNN.length; i++) {
        var campo = camposNN[i];
        if (campo.value.trim() === '') {
            var errorMessage = document.getElementById('error-message');
            errorMessage.textContent = "El campo no admite vacíos.";
            campo.classList.add('invalido');
            error = true;
        }
    }

    return !error; 
}