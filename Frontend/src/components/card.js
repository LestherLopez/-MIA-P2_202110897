import React, { useState, useRef } from 'react';
import Button from 'react-bootstrap/Button';
function Card() {

    const [results, setResults] = useState('');
    const [commands, setCommands] = useState('');
    const [isPaused, setIsPaused] = useState(false);
    const [commands_list, setCommands_list] = useState([]);
    const textAreaRef = useRef(null);
    
    const fileInputRef = useRef(null);

        const handleButtonClick = () => {
            fileInputRef.current.click();
        };

  
    const handleFileChange = (e) => {
      const file = e.target.files[0];
      const reader = new FileReader();
  
      reader.onload = (event) => {
        setCommands(event.target.result);
      };
  
      if (file) {
        reader.readAsText(file);
      }
    };

    const handleTextAreaKeyPress = (event) => {
        if (event.key === 'Enter') {
            if(isPaused){
                sendCommands(commands_list);
            }
        }
    };

    const sendCommands = async (commands) => {
        for (let i = 0; i < commands.length; i++) {
            const command = commands[i].trim();
        
            if (command) { // Evita enviar líneas en blanco
                setCommands_list(commands.slice(i+1, commands.length));
                if(command == 'pause'){
                    setIsPaused(true);
                    console.log(commands_list);
                    setResults(prevResults => prevResults + `[Pause] => Presiona Enter para continuar\n`);
                    break;
                }
                try {
                    const response = await fetch("http://127.0.0.1:5000" +'/execute', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ command }),
                    });
            
                    const data = await response.json();
                    setResults(prevResults => prevResults + `${data.mensaje}\n`);
                } catch (error) {
                    console.error(`Error en la solicitud ${i + 1}: ${error}`);
                }
            }
        }
    };

    const handleSubmit = () => {
        //Para enfocar el textarea
        textAreaRef.current.focus();
        //Para limpiar el textarea
        setResults('');
        //Para dividir los comandos por salto de línea
        const commandLines = commands.split('\n');
        //Actualizamos la lista de comandos y enviamos los comandos
        setCommands_list(commandLines);
        sendCommands(commandLines);
    };

    const estiloOscuro = {
        backgroundColor: '#1a1a1a', // Fondo oscuro
        color: 'white', // Texto en blanco
        border: '1px #001f3f', // Borde blanco
        borderRadius: '0.25rem',
        padding: '0.375rem 0.75rem',
      };
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
      const estiloText = {
               
        height: '200px',
        backgroundColor: '#4b1d3f',
        border: 'none',
        color: '#FFFFFF',
        margin: '0px',
        fontSize: '1.1rem',
          
      };
      const header = {
        top: '0',
        left: '0',
        right: '0',
        width: '100%',
        height: '40px',
        display: 'flex', // Utilizar flexbox para centrar vertical y horizontalmente
        alignItems: 'center', // Centrar verticalmente
        justifyContent: 'center', // Centrar horizontalmente
        color: '#FFFFFF',
        lineHeight: '40px', // camelCase en lugar de lineheight
        fontWeight: '600', // camelCase en lugar de fontweight
        backgroundColor: '#242424', // camelCase en lugar de backgroundcolor
        textAlign: 'center',
      };
  return (
    <div style ={estiloOscuro }lassName="card mt-4">
      <h5 className="card-header">
        <div className='d-flex justify-content-between'>
            <p>Manejo de Archivos</p>
            <div>
                <input
                        type="file"
                        ref={fileInputRef}
                        style={{ display: 'none' }}
                        onChange={handleFileChange}
                         />
                <Button onClick={handleButtonClick}>Cargar Archivo</Button>    
            </div>
        </div>
      </h5>

      <div className="card-body">

        <div className="d-flex flex-row-reverse">
        </div>
        <div className="mb-3">
            <div style = {header}class="title-bar">Consola de Comandos</div>
            <textarea 
                className="form-control" 
                placeholder="Ingresa aquí los comandos que deseas ejecutar" 
                style={estiloText}
                value={commands}
                onChange={(e) => setCommands(e.target.value)}
            ></textarea>
        </div>

        <div className="d-flex flex-row-reverse">
        </div>
        <div className="mb-3">
            <div style={header} class="title-bar">Consola de salida</div>
            <textarea 
                className="form-control" 
                placeholder="Aquí aparecerán los resultados" 
                readOnly
                ref={textAreaRef}
                style={estiloText} 
                value={results}
                onKeyDown={handleTextAreaKeyPress}
            ></textarea>

        </div>

        <button style={estiloBoton}  className="btn btn-primary mt-3" onClick={handleSubmit}>Ejecutar</button>
      </div>
    </div>
  );
}

export default Card;
