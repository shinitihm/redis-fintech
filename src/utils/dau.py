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


# b) Verificar se acessou no dia 5

dia_verificar = 5
offset = dia_verificar - 1

acessou = r.getbit(chave, offset)

if acessou:
    print(f"O cliente acessou o aplicativo no dia {dia_verificar}.")
else:
    print(f"O cliente NÃO acessou o aplicativo no dia {dia_verificar}.")


# c) Contar dias ativos no mês

total_dias = r.bitcount(chave)

print(f"Total de dias ativos em julho: {total_dias}")


if total_dias >= 15:
    print("Cliente recebe isenção da taxa de manutenção.")
else:
    print("Cliente NÃO recebe isenção da taxa de manutenção.")