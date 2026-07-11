import { API } from "../lib/api";

export async function obtenerDashboard() {
  const res = await fetch(`${API}/api/system/status`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!res.ok) {
    throw new Error(await res.text());
  }

  return await res.json();
}