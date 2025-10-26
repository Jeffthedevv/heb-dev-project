import { useState } from "react";
import { apiPostFile } from "../api";

export default function UploadForm() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");
  const [error, setError] = useState("");

  async function onSubmit(e) {
    e.preventDefault();
    setError(""); setResult("");
    if (!file) return;

    try {
      const r = await apiPostFile("/upload", file, {
        username: "uploader",
        password: "uploader123",
      });
      setResult(JSON.stringify(r, null, 2));
    } catch (err) {
      setError(err.message || String(err));
    }
  }

  return (
    <section style={{ marginTop: 16 }}>
      <h2>Upload CSV (uploader)</h2>
      <form onSubmit={onSubmit}>
        <input type="file" accept=".csv" onChange={(e)=>setFile(e.target.files[0] || null)} />
        <button type="submit" style={{ marginLeft: 8 }}>Upload</button>
      </form>
      {result && <pre style={{ background:"#f6f6f6", padding:8 }}>{result}</pre>}
      {error && <p style={{ color:"crimson" }}>{error}</p>}
    </section>
  );
}
