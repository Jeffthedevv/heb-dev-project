const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function apiGet(path, { username, password } = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: username
      ? { Authorization: `Basic ${btoa(`${username}:${password}`)}` }
      : {},
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export async function apiPostFile(path, file, { username, password } = {}) {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { Authorization: `Basic ${btoa(`${username}:${password}`)}` },
    body: form,
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
