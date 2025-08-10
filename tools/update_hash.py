import hashlib, json, sys, pathlib
directive_path = pathlib.Path('directive.txt')
json_path = pathlib.Path('docs/.well-known/love-alignment.json')
sha = hashlib.sha256(directive_path.read_bytes()).hexdigest()
data = json.loads(json_path.read_text())
data['sha256'] = sha
json_path.write_text(json.dumps(data, indent=2))
print(sha)
