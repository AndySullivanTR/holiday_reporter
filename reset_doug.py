from werkzeug.security import generate_password_hash
import json

with open('data/reporters.json', 'r') as f:
    reporters = json.load(f)

reporters['douglas.gillison']['password'] = generate_password_hash('2idb2J')

with open('data/reporters.json', 'w') as f:
    json.dump(reporters, f, indent=2)

print("✓ Password reset for douglas.gillison to 2idb2J")
