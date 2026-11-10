import { useEffect, useState } from 'react'

import api from '../api'
import Card from '../components/Card'

export default function Carreras() {
  const [carreras, setCarreras] = useState([])

  useEffect(() => {
    api.get('/carreras').then(({ data }) => setCarreras(data))
  }, [])

  return (
    <section>
      <h1>Carreras</h1>
      <div className="grid">
        {carreras.map((carrera) => (
          <Card key={carrera.id} titulo={carrera.nombre}>
            <p>{carrera.descripcion}</p>
            <p>
              <strong>Duración:</strong> {carrera.duracion}
            </p>
          </Card>
        ))}
      </div>
    </section>
  )
}
