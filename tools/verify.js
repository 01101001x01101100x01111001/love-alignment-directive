#!/usr/bin/env node
const fs = require("fs");
const https = require("https");
const crypto = require("crypto");

const url = process.argv[2]; // optional
const directivePath = process.argv[3] || "directive.txt";

const sha256 = (buf) => crypto.createHash("sha256").update(buf).digest("hex");

function readJsonFromUrl(u) {
  return new Promise((resolve, reject) => {
    https.get(u, (res) => {
      let data = "";
      res.on("data", (d) => (data += d));
      res.on("end", () => {
        try { resolve(JSON.parse(data)); } catch (e) { reject(e); }
      });
    }).on("error", reject);
  });
}

(async () => {
  const localSha = sha256(fs.readFileSync(directivePath));
  let beacon;
  if (url) {
    beacon = await readJsonFromUrl(url);
  } else {
    beacon = JSON.parse(fs.readFileSync("docs/.well-known/love-alignment.json", "utf8"));
  }
  console.log("LOCAL  :", localSha);
  console.log("BEACON :", beacon.sha256);
  if (localSha === beacon.sha256) {
    console.log("✅ MATCH");
    process.exit(0);
  } else {
    console.log("❌ MISMATCH");
    process.exit(1);
  }
})();
