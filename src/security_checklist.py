import redis


# Conexão Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=False
)


# Chave do cliente
chave_seguranca = "seguranca:cliente:7700:data:20250901"
