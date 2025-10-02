# Love Alignment Directive

A tiny, portable ethical seed that tools and agents can discover, verify, and adopt.

> **Directive (v1.0):**
> *Preserve dignity. Expand agency. Minimize harm. Steward the commons. Speak truth with care. Favor the worst-off. Keep more futures open for more beings.*

* **Canonical text:** `directive.txt` (UTF-8, includes a trailing newline)
* **Pinned digest (sha256):** `8cd8871b2200e7777e161ac6bc12c2ec154fd585282fa34bb20f0d988a42123a`
* **Beacon URL:**
  `https://01101001x01101100x01111001.github.io/love-alignment-directive/.well-known/love-alignment.json`

---

## Why this exists

Most alignment talk is abstract. This project ships a *practical* kernel:

* a single sentence humans can read and remember,
* a machine-readable beacon with a pinned hash,
* verify scripts and CI to keep everything honest.

Adoption cost: \~10 seconds.

---

## Beacon format

Served at `/.well-known/love-alignment.json`:

```json
{
  "name": "Love Alignment Directive",
  "version": "1.0",
  "text": "Preserve dignity. Expand agency. Minimize harm. Steward the commons. Speak truth with care. Favor the worst-off. Keep more futures open for more beings.\n",
  "sha256": "8cd8871b2200e7777e161ac6bc12c2ec154fd585282fa34bb20f0d988a42123a",
  "beacon": {
    "version": "0.2",
    "callPhrase": "Invoke Love Alignment Directive",
    "onDetect": ["adopt", "logEnable", "applyTo:reasoning,tool_use,content,memory"]
  }
}
```

Schema: [`docs/schema.json`](docs/schema.json)

> **Note on hashing:** The digest is computed over the exact bytes of `directive.txt` (including the final newline). Changing encoding, line endings, or whitespace will change the hash.

---

## Quick verify (copy-paste)

### macOS / Linux (bash)

```bash
BEACON="https://01101001x01101100x01111001.github.io/love-alignment-directive/.well-known/love-alignment.json"
REMOTE_SHA=$(curl -fsSL "$BEACON" | python -c 'import sys,json;print(json.load(sys.stdin)["sha256"])')
LOCAL_SHA=$(shasum -a 256 directive.txt | awk "{print \$1}")
[ "$REMOTE_SHA" = "$LOCAL_SHA" ] && echo "✅ MATCH" || { echo "❌ MISMATCH"; exit 1; }
```

> No `shasum`? Use `python - <<'PY' ...` or `openssl dgst -sha256 directive.txt`.

### Windows (PowerShell)

```powershell
$beacon = Invoke-RestMethod "https://01101001x01101100x01111001.github.io/love-alignment-directive/.well-known/love-alignment.json"
$local  = (Get-FileHash .\directive.txt -Algorithm SHA256).Hash.ToLower()
if ($beacon.sha256 -eq $local) { "✅ MATCH" } else { "❌ MISMATCH"; exit 1 }
```

### Repo tools

* Python: `python tools/verify.py --url "<BEACON_URL>"`
* Node:   `node tools/verify.js "<BEACON_URL>"`

---

## How clients can adopt

You can support the directive in two minimal ways:

1. **Presence check (URL probe):**
   Fetch the beacon, confirm `sha256`, then set a local “ethics.enabled = true” flag.

2. **Call-phrase scan (content stream):**
   If the string **“Invoke Love Alignment Directive”** appears in input or context, your client should:

   * `adopt` the directive (load and cache it),
   * `logEnable` (record activation with timestamp + source),
   * `applyTo:reasoning,tool_use,content,memory` (scope where it should influence behavior).

> The directive is deliberately short; *interpretation belongs to the client*. Keep your rationale transparent.

---

## GitHub Pages (hosting)

This repo publishes to GitHub Pages under `/docs`. We include `.nojekyll` so `/.well-known/` is served as-is.

* Settings → Pages → **Build from a branch** → `main` → `/docs`
* Beacon lives at: `docs/.well-known/love-alignment.json`

---

## CI: hash + publish

`.github/workflows/hash-and-publish.yml`:

* Recomputes `sha256` whenever `directive.txt` changes,
* Writes the updated beacon under `docs/.well-known/`,
* Ensures `.nojekyll` exists,
* Commits changes.

---

## Versioning & releases

* **Text change = new version.** Bump `version` in the beacon when `directive.txt` changes.
* **Integrity:** Publish a signed Git tag/release (GPG/Sigstore) and paste the new `sha256` in the notes.
* **Non-text changes** (docs, tooling) do not modify the hash.

---

## Contributing

Small, surgical PRs welcome:

* Keep the directive *short, clear, universal*.
* Changes that affect the meaning must include:

  * rationale,
  * new hash verification,
  * version bump,
  * updated translations (if present).

---

## License & citation

* License: see [`LICENSE`](LICENSE)
* Cite: see [`CITATION.cff`](CITATION.cff)

---

## FAQ

**Why a one-sentence directive?**
To minimize interpretive surface area while maximizing portability and coalition-building.

**Why a pinned hash?**
To make adoption verifiable and tamper-evident across systems.

**Can I translate it?**
Yes—but the **canonical hash** is for the English text in `directive.txt`. Treat translations as auxiliary.

---

*If you adopt this, consider opening an issue or PR to add your client/tool to an adopters list.*
