import React from 'react';



function Modal() {
    const estiloBoton = {
        backgroundColor: '#28a745', // Azul vibrante
        color: 'white', // Texto en blanco
        border: 'none', // Sin borde
        borderRadius: '0.25rem',
        padding: '0.375rem 0.75rem',
        cursor: 'pointer',
        transition: 'background-color 0.2s, color 0.2s, box-shadow 0.2s',
        boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)', // Sombra al pasar el cursor
      };
      const estiloBotonc = {
        backgroundColor: '#FF0000', 
        color: 'white',// Texto en blanco
        border: 'none', // Sin borde
        borderRadius: '0.25rem',
        padding: '0.375rem 0.75rem',
        cursor: 'pointer',
        transition: 'background-color 0.2s, color 0.2s, box-shadow 0.2s',
        boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)', // Sombra al pasar el cursor
      };
  return (
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content bg-dark text-light">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Iniciar Sesion</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form>
                    <div class="mb-3">
                        <label for="username" class="col-form-label">Username</label>
                        <input type="text" class="form-control bg-dark text-light" id="username"></input>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="col-form-label">Password</label>
                        <input type="password" class="form-control bg-dark text-light" id="password"></input>
                    </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" style={estiloBotonc}>Close</button>
                    <button type="button" class="btn btn-primary" style={estiloBoton}>Login</button>
                </div>
                </div>
            </div>
        </div>
  );
}

export default Modal;