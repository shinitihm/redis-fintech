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
