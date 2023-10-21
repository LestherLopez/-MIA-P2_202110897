import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import '../components/navbar.css';
function Layout() {
  return (
    <>
    
      <Navbar bg="light" variant="light" className='fondo-negro'>
        <Container>
       
          <Nav className="me-auto">
          <Nav.Link href="#home" className="text-white">Home</Nav.Link>
          <Nav.Link href="#features" className="text-white">Crear Archivos</Nav.Link>
          <Nav.Link href="#features" className="text-white">Abrir Archivos</Nav.Link>
          <Nav.Link href="#pricing" className="text-white">Guardar Archivo</Nav.Link>
          <Nav.Link href="#features" className="text-white">Eliminar Pestaña</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default Layout;

//aqui se agregan componentes desde la pagina bootstrap-react