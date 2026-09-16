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

