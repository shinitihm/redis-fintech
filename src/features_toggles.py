import redis

# Conexão Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=False
)


# Chaves das empresas
alfa = "permissoes:pj:1001"
beta = "permissoes:pj:1002"

