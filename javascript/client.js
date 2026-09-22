import { VEXO_API_KEY, BASE_URL } from "./config.js";

async function request(path, params = {}) {
  if (!VEXO_API_KEY.trim()) throw new Error("VEXO_API_KEY belum diisi di javascript/config.js");
  const query = new URLSearchParams({ ...params, apikey: VEXO_API_KEY });
  const response = await fetch(`${BASE_URL}${path}?${query}`);
  let data;
  try { data = await response.json(); } catch { throw new Error(`Response bukan JSON (HTTP ${response.status})`); }
  if (!response.ok || (data && data.status === false)) throw new Error(data?.message || `HTTP ${response.status}`);
  return data;
}

export { request };
