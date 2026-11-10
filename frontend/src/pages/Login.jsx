import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

import { useAuth } from '../context/AuthContext'

export default function Login() {
  const [correo, setCorreo] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const { login } = useAuth()
  const navigate = useNavigate()

  async function enviar(evento) {
    evento.preventDefault()
    try {
      await login(correo, password)
      navigate('/')
    } catch {
      setError('Correo o contraseña incorrectos')
    }
  }

  return (
    <section>
      <h1>Ingresar</h1>
      <form onSubmit={enviar}>
        <input
          type="email"
          placeholder="Correo institucional"
          value={correo}
          onChange={(evento) => setCorreo(evento.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(evento) => setPassword(evento.target.value)}
          required
        />
        <button type="submit">Entrar</button>
      </form>
      {error && <p className="error">{error}</p>}
    </section>
  )
}
