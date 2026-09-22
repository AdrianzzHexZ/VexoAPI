import { request } from "./client.js";

const kota = process.argv[2] || "Jakarta";
try {
  const data = await request("/api/tools/cekcuaca", { kota });
  console.log(JSON.stringify(data, null, 2));
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exitCode = 1;
}
