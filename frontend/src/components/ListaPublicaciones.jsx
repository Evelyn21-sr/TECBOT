import { useEffect, useState } from 'react'

import api from '../api'
import Card from './Card'

export default function ListaPublicaciones({ endpoint, titulo }) {
  const [items, setItems] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    api
      .get(endpoint)
      .then(({ data }) => setItems(data))
      .catch(() => setError('No se pudo cargar la información'))
  }, [endpoint])

  return (
    <section>
      <h1>{titulo}</h1>
      {error && <p className="error">{error}</p>}
      <div className="grid">
        {items.map((item) => (
          <Card key={item.id} titulo={item.titulo}>
            <p>{item.contenido}</p>
          </Card>
        ))}
      </div>
    </section>
  )
}
