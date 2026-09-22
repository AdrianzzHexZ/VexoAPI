import { request } from "./client.js";

const url = process.argv[2];
if (!url) {
  console.error("Pakai: node javascript/tt-downloader.js <URL_TIKTOK>");
  process.exit(1);
}
try {
  const data = await request("/api/download/tiktok-hd", { url });
  console.log(JSON.stringify(data, null, 2));
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exitCode = 1;
}
