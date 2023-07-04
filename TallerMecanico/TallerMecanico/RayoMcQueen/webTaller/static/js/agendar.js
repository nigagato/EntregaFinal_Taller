function validarMensaje(event) {
    event.preventDefault(); // Evita el envío del formulario

    var nombre = document.getElementById('txtNombre').value;
    var email = document.getElementById('txtEmailAgendar').value;
    var telefono = document.getElementById('txtTelefono').value;
    var fechaAtencion = document.getElementById('fechaAtencion').value;

    if (nombre.trim() === '' || email.trim() === '' || telefono.trim() === '' || fechaAtencion.trim() === '') {
        alert('Por favor, complete todos los campos del formulario.');
        return;
    }

    var telefonoLength = telefono.trim().length;
    if (telefonoLength !== 9) {
        alert('El número de teléfono debe tener 9 dígitos.');
        return;
    }

    var fechaActual = new Date();
    var fechaSeleccionada = new Date(fechaAtencion);

    if (fechaSeleccionada <= fechaActual) {
        alert('Debes agendar con al menos 1 día de anticipación.');
        return;
    }

    // Si pasa todas las validaciones, se envía el formulario
    event.target.form.submit();
}

document.getElementById('btnAgendarForm').addEventListener('click', validarMensaje);
