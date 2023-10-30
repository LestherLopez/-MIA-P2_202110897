// imageData.js
export const imageNames = [];

// Convertir la lista en una cadena JSON
const listaJSON = JSON.stringify(imageNames);

// Guardar la cadena JSON en sessionStorage bajo una clave específica
sessionStorage.setItem('miListaGuardada', listaJSON);