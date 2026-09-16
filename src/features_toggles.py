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


# =====================================
# A) Ativar permissões da Alfa Tech
# =====================================

def ativar_modulos(chave, modulos):
    for modulo in modulos:
        r.setbit(chave, modulo, 1)


# Alfa Tech:
# Pix (0)
# Boletos (1)
# Antecipação (3)
# Cartão Corporativo (5)

ativar_modulos(
    alfa,
    [0, 1, 3, 5]
)


print("Permissões Alfa Tech ativadas")

