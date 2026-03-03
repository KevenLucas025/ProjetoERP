from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from pathlib import Path

out = Path("keys")
out.mkdir(exist_ok=True)

private_key  = ed25519.Ed25519PrivateKey.generate()
public_key  = private_key .public_key()

priv_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(b"SENHA_FORTE_AQUI"),
)

pub_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

(out / "master_private.pem").write_bytes(priv_bytes)
(out / "master_public.pem").write_bytes(pub_bytes)

print("OK!")
print("Chave privada: keys/master_private.pem (GUARDE FORA DO PROJETO)")
print("Chave pública: keys/master_public.pem (essa vai no app)")

