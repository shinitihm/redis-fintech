import redis


# Conexão Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=False
)


# Chave do cliente
chave_seguranca = "seguranca:cliente:7700:data:20250901"


# ==========================================
# A) Registrar validações realizadas
# ==========================================

# Bit 0 = Geolocalização
r.setbit(chave_seguranca, 0, 1)

# Bit 1 = Biometria
r.setbit(chave_seguranca, 1, 1)

# Bit 2 = Dispositivo cadastrado
r.setbit(chave_seguranca, 2, 1)


print("Checklist de segurança registrado!")


# ==========================================
# B) Verificar quantidade de validações
# necessárias para liberar PIX
# ==========================================

quantidade_validacoes = r.bitcount(
    chave_seguranca
)


print(
    "Quantidade de validações:",
    quantidade_validacoes
)


if quantidade_validacoes >= 4:
    print("PIX de alto valor LIBERADO")
else:
    print("PIX de alto valor BLOQUEADO - segurança insuficiente")

