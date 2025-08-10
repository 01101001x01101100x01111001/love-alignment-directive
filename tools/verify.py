#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, sys, urllib.request

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def main():
    p = argparse.ArgumentParser(description="Verify that directive.txt matches beacon sha256")
    p.add_argument("--url", help="Beacon URL (if omitted, read docs/.well-known/love-alignment.json locally)")
    p.add_argument("--directive", default="directive.txt", help="Path to directive.txt")
    args = p.parse_args()

    directive = pathlib.Path(args.directive).read_bytes()
    local_sha = sha256_bytes(directive)

    if args.url:
        with urllib.request.urlopen(args.url) as r:
            j = json.load(r)
    else:
        j = json.loads(pathlib.Path("docs/.well-known/love-alignment.json").read_text(encoding="utf-8"))

    beacon_sha = j["sha256"]
    print(f"LOCAL  : {local_sha}")
    print(f"BEACON : {beacon_sha}")
    if local_sha == beacon_sha:
        print("✅ MATCH")
        sys.exit(0)
    else:
        print("❌ MISMATCH")
        sys.exit(1)

if __name__ == "__main__":
    main()
