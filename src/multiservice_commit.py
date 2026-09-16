import redis


# Conexão Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=False
)


# Chaves
chave_pix = "pix:cliente:3300:semana1"
chave_push = "push:cliente:3300:semana1"


# ==========================================
# A) Registrar eventos Pix e Push
# ==========================================

# Cliente usou Pix:
# Terça (Bit 2)
# Sexta (Bit 5)

r.setbit(chave_pix, 2, 1)
r.setbit(chave_pix, 5, 1)


# Cliente abriu Push:
# Segunda (Bit 1)
# Terça (Bit 2)
# Quinta (Bit 4)

r.setbit(chave_push, 1, 1)
r.setbit(chave_push, 2, 1)
r.setbit(chave_push, 4, 1)


print("Eventos registrados com sucesso!")


# ==========================================
# B) Consolidar interação Pix OU Push
# BITOP OR
# ==========================================

chave_engajamento = "engajamento:cliente:3300:semana1"


r.bitop(
    "OR",
    chave_engajamento,
    chave_pix,
    chave_push
)


dias_interacao = r.bitcount(
    chave_engajamento
)


print(
    "Dias com interação:",
    dias_interacao
)

