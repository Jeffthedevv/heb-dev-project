import { useEffect, useState } from "react";
import { apiGet } from "../api";

export default function DataTable() {
  const [rows, setRows] = useState([]);
  const [q, setQ] = useState("");
  const [page, setPage] = useState(0);
  const limit = 10;

  useEffect(() => {
    (async () => {
      const data = await apiGet(
        `/records?limit=${limit}&offset=${page * limit}&q=${encodeURIComponent(q)}`,
        { username: "viewer", password: "viewer123" }
      );
      setRows(data);
    })();
  }, [q, page]);

  return (
    <section style={{ marginTop: 24 }}>
      <h2>Customers</h2>
      <input
        placeholder="Filter by name"
        value={q}
        onChange={(e) => { setPage(0); setQ(e.target.value); }}
        style={{ marginBottom: 8 }}
      />
      <table border="1" cellPadding="6" style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr><th>ID</th><th>Name</th><th>Email</th><th>Created</th></tr>
        </thead>
        <tbody>
          {rows.map(r => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.name}</td>
              <td>{r.email || ""}</td>
              <td>{new Date(r.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div style={{ marginTop: 8 }}>
        <button disabled={page===0} onClick={() => setPage(p => p - 1)}>Prev</button>
        <span style={{ margin: "0 8px" }}>Page {page + 1}</span>
        <button onClick={() => setPage(p => p + 1)}>Next</button>
      </div>
    </section>
  );
}