import { request } from "./client.js";

const surah = process.argv[2];
try {
  const data = await request("/api/islamic/quran", surah ? { surah } : {});
  console.log(JSON.stringify(data, null, 2));
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exitCode = 1;
}
