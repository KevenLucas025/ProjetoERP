import base64, json, time, secrets
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from master_public_key import MASTER_PUBLIC_KEY_PEM

def _b64d(s: str) -> bytes:
    s = (s or "").strip()
    pad = "=" * ((4 - len(s) % 4) % 4)
    return base64.urlsafe_b64decode(s + pad)

def gerar_nonce() -> str:
    return secrets.token_urlsafe(16)

def _load_pub():
    pem = MASTER_PUBLIC_KEY_PEM
    if isinstance(pem, str):
        pem = pem.encode("utf-8")
    pub = serialization.load_pem_public_key(pem)
    assert isinstance(pub, ed25519.Ed25519PublicKey)
    return pub

def validar_codigo_assinado(codigo: str, janela_segundos: int = 300) -> dict | None:
    try:
        codigo = (codigo or "").strip().replace("\n", "").replace("\r", "").replace(" ", "")

        if "." not in codigo:
            print("[DEBUG validar] formato inválido (sem ponto).")
            return None

        payload_b64, sig_b64 = codigo.split(".", 1)
        payload_bytes = _b64d(payload_b64)
        sig = _b64d(sig_b64)

        pub = _load_pub()

        # se falhar aqui, é chave errada OU assinatura adulterada
        pub.verify(sig, payload_bytes)

        payload = json.loads(payload_bytes.decode("utf-8"))
        ts = int(payload.get("ts", 0))
        now = int(time.time())
        diff = abs(now - ts)

        print("[DEBUG validar] now:", now, "ts:", ts, "diff:", diff, "janela:", janela_segundos)

        if ts <= 0 or diff > janela_segundos:
            print("[DEBUG validar] expirado ou ts inválido.")
            return None

        return payload

    except Exception as e:
        print("[DEBUG validar] erro:", repr(e))
        return None