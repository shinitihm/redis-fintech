import redis

# Conectar ao Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# Chave do cliente
chave = "acesso:cliente:5050:mes7"

# a) Registrar os acessos
# Dias: 1, 5, 10 e 31
# Offset = dia - 1


dias_acesso = [1, 5, 10, 31]

for dia in dias_acesso:
    offset = dia - 1
    r.setbit(chave, offset, 1)

print("Acessos registrados com sucesso!")

