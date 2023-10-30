import React, { useState, useEffect } from 'react';

import './reports.css';



function Reports_Card() {
  
  // Recuperar la cadena JSON desde localStorage4
  const listaJSON = localStorage.getItem('miListaGuardada');
  
  // Convertir la cadena JSON en una lista
  const imageNamess = JSON.parse(listaJSON);
  
  const [imageUrls, setImageUrls] = useState([]);

  useEffect(() => {
    // Aquí colocarás el código para obtener las URL de las imágenes desde Amazon S3.
    // Puedes usar el código que mencioné anteriormente para obtener las URL y almacenarlas en el estado 'imageUrls'.
    const s3BucketUrl = 'https://lestherlopez.s3.amazonaws.com/';


    const urls = imageNamess.map(imageName => ({ url : s3BucketUrl + imageName, description: imageName}));
    setImageUrls(urls);
  }, []);
  
  return (
    
    <div className="card mt-4 primer-div">
      <h5 className="card-header">
        <div className='d-flex justify-content-between'>
            <p>Manejo de Archivos</p>
        </div>
      </h5>
      <div className="card-body">
      
      {imageUrls.map((url, index) => (
  url.description.slice(-3) === "jpg" ? (
    <center key={index}>
      <img src={url.url} className="img-fluid" alt="..." />
      <figcaption>{url.description}</figcaption>
    </center>
  ) : url.description.slice(-3) === "txt" ? (
    <center key={index}>
      <a href={url.url} target="_blank" rel="noopener noreferrer">
        Ver archivo de texto
      </a>
      <figcaption>{url.description}</figcaption>
    </center>
  ) : (
    <center key={index}>
      <span>{url.description}</span>
    </center>
  )
))}

      </div>
    </div>
  );
}

export default Reports_Card;