import React from 'react';
import './navbar.css';

function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light custom-navbar">
            <a className="navbar-brand ms-3" href="#" style={{color:'white'}}>Proyecto 2 MIA</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNavDropdown">
                <ul className="navbar-nav">
                    <li className="nav-item active">
                        <a className="nav-link" href="/" style={{ background: '#1a1a1a', color: 'white' }}>Home</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/reports" style={{ background: '#1a1a1a', color: 'white' }}>Reportes</a>
                    </li>
                    <li className="nav-item">
                    <button className="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal" style={{ background: '#1a1a1a', color: 'white', border: 'none' }}>Iniciar Sesión</button>

                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;
