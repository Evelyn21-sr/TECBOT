import { Link } from 'react-router-dom'

import { useAuth } from '../context/AuthContext'

export default function Navbar() {
  const { usuario, logout } = useAuth()

  return (
    <nav className="navbar">
      <Link to="/" className="logo">
        TECBOT
      </Link>
      <div className="enlaces">
        <Link to="/noticias">Noticias</Link>
        <Link to="/carreras">Carreras</Link>
        <Link to="/convocatorias">Convocatorias</Link>
        <Link to="/eventos">Eventos</Link>
        <Link to="/becas">Becas</Link>
        <Link to="/servicios">Servicios</Link>
        <Link to="/recursos">Recursos</Link>
        {usuario ? (
          <button onClick={logout}>Salir</button>
        ) : (
          <Link to="/login">Ingresar</Link>
        )}
      </div>
    </nav>
  )
}
