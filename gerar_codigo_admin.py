import base64, json, time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from pathlib import Path

def _b64e(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode("utf-8").rstrip("=")

def carregar_privada(path="keys/master_private.pem", senha=b"SENHA_FORTE_AQUI"):
    pem = Path(path).read_bytes()
    key = serialization.load_pem_private_key(pem, password=senha)
    assert isinstance(key, ed25519.Ed25519PrivateKey)
    return key

def gerar_codigo_promover(usuario_alvo: str, nonce: str):
    payload = {
        "acao": "promover_admin",
        "usuario_alvo": usuario_alvo.strip(),
        "ts": int(time.time()),
        "nonce": nonce,
    }
    payload_bytes = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return payload, payload_bytes

if __name__ == "__main__":
    usuario = input("Usuário alvo: ").strip()
    nonce = input("Nonce (copie do sistema): ").strip()

    priv = carregar_privada()

    payload, payload_bytes = gerar_codigo_promover(usuario, nonce)
    sig = priv.sign(payload_bytes)

    codigo = f"{_b64e(payload_bytes)}.{_b64e(sig)}"
    print("\n=== CÓDIGO MESTRE ===")
    print(codigo)
    print("=====================")