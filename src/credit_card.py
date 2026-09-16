import redis

# Conexão com Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=False
)

# Chaves do cliente
chave_debito = "cartao:debito:cliente:8820:mes8"
chave_credito = "cartao:credito:cliente:8820:mes8"

# ==========================================
# A) Registrar utilização de Débito e Crédito
# ==========================================

# Função auxiliar:
# Offset = Dia - 1
def registrar_uso(chave, dias):
    for dia in dias:
        offset = dia - 1
        r.setbit(chave, offset, 1)


# Débito usado nos dias 2 e 10
registrar_uso(chave_debito, [2, 10])

# Crédito usado nos dias 10 e 20
registrar_uso(chave_credito, [10, 20])


print("Eventos registrados!")


# ==========================================
# B) BITOP AND
# Dias em que usou Débito e Crédito juntos
# ==========================================

chave_ambos = "cartao:ambos:cliente:8820:mes8"

r.bitop(
    "AND",
    chave_ambos,
    chave_debito,
    chave_credito
)


# Contar bits ligados
dias_ambos = r.bitcount(chave_ambos)

print(
    "Dias usando ambas as funções:",
    dias_ambos
)
