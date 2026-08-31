export default function MetricPage({ params }: { params: { key: string } }) {
  return (
    <main>
      <h1>{params.key}</h1>
      <p>Last 30 days</p>
    </main>
  );
}
