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

