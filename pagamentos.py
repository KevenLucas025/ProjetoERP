import mercadopago
import os

class MercadoPagoService:
    def __init__(self):
        token = os.getenv("MP_ACCESS_TOKEN")
        if not token:
            raise Exception("MP_ACCESS_TOKEN não encontrado")

        self.sdk = mercadopago.SDK(token)

    def criar_pagamento_pix(self, valor, descricao, email_cliente):
        pagamento = {
            "transaction_amount": float(valor),
            "description": descricao,
            "payment_method_id": "pix",
            "payer": {
                "email": email_cliente
            }
        }

        resposta = self.sdk.payment().create(pagamento)
        return resposta["response"]
    
    def obter_pagamento(self, pagamento_id):
        resposta = self.sdk.payment().get(pagamento_id)
        return resposta["response"]

