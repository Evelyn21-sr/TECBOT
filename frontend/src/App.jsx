import { Route, Routes } from 'react-router-dom'

import Footer from './components/Footer'
import Navbar from './components/Navbar'
import Becas from './pages/Becas'
import Carreras from './pages/Carreras'
import Convocatorias from './pages/Convocatorias'
import Eventos from './pages/Eventos'
import Home from './pages/Home'
import Login from './pages/Login'
import Noticias from './pages/Noticias'
import Recursos from './pages/Recursos'
import Servicios from './pages/Servicios'

export default function App() {
  return (
    <div className="app">
      <Navbar />
      <main className="contenido">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/noticias" element={<Noticias />} />
          <Route path="/carreras" element={<Carreras />} />
          <Route path="/convocatorias" element={<Convocatorias />} />
          <Route path="/eventos" element={<Eventos />} />
          <Route path="/becas" element={<Becas />} />
          <Route path="/servicios" element={<Servicios />} />
          <Route path="/recursos" element={<Recursos />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </main>
      <Footer />
    </div>
  )
}
