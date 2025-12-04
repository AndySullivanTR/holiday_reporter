from werkzeug.security import generate_password_hash
import json

with open('data/reporters.json', 'r') as f:
    reporters = json.load(f)

reporters['tatiana.bautzer']['password'] = generate_password_hash('x8ZQRd')

with open('data/reporters.json', 'w') as f:
    json.dump(reporters, f, indent=2)

print("✓ Password reset for tatiana.bautzer to x8ZQRd")
