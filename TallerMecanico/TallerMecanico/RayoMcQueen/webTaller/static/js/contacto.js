function validarContacto(event) {
    event.preventDefault(); // Evita el envío del formulario

    var nombre = document.getElementById('txtNombre').value;
    var email = document.getElementById('txtEmailMensaje').value;
    var telefono = document.getElementById('txtTelefono').value;

    if (nombre.trim() === '' || email.trim() === '' || telefono.trim() === '') {
        Swal.fire({
            title: 'error',
            text: 'Por favor, complete todos los campos del formulario.',
            icon: 'error',
            confirmButtonText: 'Aceptar'
        });
        return;
    }

    var telefonoLength = telefono.trim().length;
    if (telefonoLength !== 9) {
        Swal.fire({
            title: 'error',
            text: 'El número de teléfono debe tener 9 dígitos.',
            icon: 'error',
            confirmButtonText: 'Aceptar'
        });
        return;
    }

    event.target.form.submit();
}

document.getElementById('contactoForm').addEventListener('submit', validarContacto);
