export function MetricCard({ name, value }: { name: string; value: string }) {
  return (
    <div className="card">
      <div className="card-name">{name}</div>
      <div className="card-value">{value}</div>
    </div>
  );
}
