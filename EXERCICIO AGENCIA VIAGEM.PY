# COMENTARIOS ANTES DE RESOLVER O EXERICIO, 
# 27/03/2026
# FATIAR O PROBLEMA, 

# DESTINO É UM INPUT DO TIPO TEXTO, 
# VOU PEGARO DICIONARIO E VOU COLOCAR LÁ EM CIMA 
# DEPOIS VOU PEDIR PRO USUARIO DIGITAR A QUANTIDADE DE PESSOAS 

# # Parte 1: Escolha do Destino

# # Peça ao usuário:

# # Nome do destino

# # Quantidade de pessoas


# Parte 2: Cálculo do Valor
# Calcule:

# Valor total da viagem (preço * pessoas)
# Parte 3: Regras da Agência (SEM if, SEM loop)

# Aplique:
# Se pessoas > 3 → desconto de 10%

# Se valor total > 10000 → desconto extra de 5%
# Se não houver vagas suficientes → taxa de 500 (overbooking)
# Se destino não existir → valor vira 0

# viagens = {
#     "Paris": {
#         "preco": 5000,
#         "vagas": 5
#     },
#     "Nova York": {
#         "preco": 4000,
#         "vagas": 3
#     },
#     "Tokyo": {
#         "preco": 6000,
#         "vagas": 2
#     }
# }




# # ---------------------------------------------------------
# INÍCIO DA RESOLUÇÃO DO EXERCÍCIO 

# O preço para paris é 5000 e a quantidade de vagas são 5 
# O preço para Nova York e 4000 e a quantidade de vagas sao 3
# O preco para Tokyo é 6000 e a quantidade de vagas são 2 

# PREMISSAS 
# # Se pessoas > 3 → desconto de 10%
# SE A QUANTIDADE DE PESSOAS FORAM SUPERIOR A 3 TERÁ DESCONTO DE 10%

# # Se valor total > 10000 → desconto extra de 5%
# SE O VALOR TOTAL FOR SUPERIOR A 10000 TERÁ DESCONTO EXTRA DE 5% ALÉM DOS 10%

# # Se não houver vagas suficientes → taxa de 500 (overbooking)
# SE NÃO TIVER VAGAS SUFICIENTES, ACRESCIMO DE 500 

# # Se destino não existir → valor vira 0


viagens = {
    "Paris": {
        "preco": 5000,
        "vagas": 5
    },
    "Nova York": {
        "preco": 4000,
        "vagas": 3
    },
    "Tokyo": {
        "preco": 6000,
        "vagas": 2
    }
}
# -----------------------------------------------------------

destino = input('Digite o Destino - ')

quantidade = int(input('Quantidade de Pessoas: '))

total = viagens[destino]["preco"]*quantidade
print('Valor Viagem',total)

desconto_sup3 = float(total * 0.1) * (quantidade > 3)
print('Desconto Extra', desconto_sup3)

desconto10 = float(total * 0.05) * (total > 10000)
print('Desconto acima' , desconto10)




