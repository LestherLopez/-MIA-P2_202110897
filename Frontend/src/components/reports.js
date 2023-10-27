import React, { useState, useEffect } from 'react';
import './reports.css';

function Reports_Card() {

  return (
    <div className="card mt-4 primer-div">
      <h5 className="card-header">
        <div className='d-flex justify-content-between'>
            <p>Manejo de Archivos</p>
        </div>
      </h5>
      <div className="card-body">
        <center>
            <img src="./logo512.png" class="img-fluid" alt="..."></img>
            <figcaption>Texto para la primera imagen</figcaption>
        </center>
        <center>
            <img src="./logo512.png" class="img-fluid" alt="..." ></img>
            <figcaption>Texto para la primera imagen</figcaption>
        </center>
        <center>
            <img src="./logo512.png" class="img-fluid" alt="..."></img>
            <figcaption>Texto para la primera imagen</figcaption>
        </center>
        <center>
            <img src="./logo512.png" class="img-fluid" alt="..."></img>
            <figcaption>Texto para la primera imagen</figcaption>
        </center>
      </div>
    </div>
  );
}

export default Reports_Card;