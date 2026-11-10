import { createContext, useContext, useEffect, useState } from 'react'

import api from '../api'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [usuario, setUsuario] = useState(null)
  const [cargando, setCargando] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (!token) {
      setCargando(false)
      return
    }

    api
      .get('/auth/me')
      .then(({ data }) => setUsuario(data))
      .catch(() => localStorage.removeItem('token'))
      .finally(() => setCargando(false))
  }, [])

  async function login(correo, password) {
    const form = new URLSearchParams()
    form.append('username', correo)
    form.append('password', password)

    const { data } = await api.post('/auth/login', form)
    localStorage.setItem('token', data.access_token)

    const { data: perfil } = await api.get('/auth/me')
    setUsuario(perfil)
  }

  function logout() {
    localStorage.removeItem('token')
    setUsuario(null)
  }

  return (
    <AuthContext.Provider value={{ usuario, cargando, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  return useContext(AuthContext)
}
