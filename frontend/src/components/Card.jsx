export default function Card({ titulo, children }) {
  return (
    <article className="card">
      <h3>{titulo}</h3>
      <div>{children}</div>
    </article>
  )
}
