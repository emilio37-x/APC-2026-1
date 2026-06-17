# exercicio 1

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")
print(moradores.head())
print(moradores.shape)'''

# exercicio 1.2

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")

colunas = ["morador_id", "localidade", "idade_calculada", "id_genero", "escolaridade", "renda_ind", "peso_mor",]
print(moradores[colunas])'''


# exercicio 1.3

'''import pandas as pd

domicilios = pd.read_excel("semana12/domicilios (1).xlsx")

mais = 0
mais1 = 0
ficha = 0
ficha2 = 0

for _, linha in domicilios.iterrows():
    if linha['A01npessoas'] > mais:
        mais = linha['A01npessoas']
        ficha = linha['A01nficha']
    if linha['A01ncriancas'] > mais1:
        mais1 = linha['A01ncriancas']
        ficha2 = linha['A01nficha']
print(f"Domicílio {ficha} tem a maior quantidade de moradores: {mais}")
print(f"Domicílio {ficha2} tem a maior quantidade de crianças: {mais1}")'''

# exercicio 1.4

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")

adultos = moradores[moradores["idade_calculada"] == 99999]
print(adultos[["morador_id", "idade_calculada"]])'''


# exercicio 2]

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")

idades = moradores[moradores["idade_calculada"] != 99999]["idade_calculada"].tolist()

c = 0
soma = 0
maximo = 0
minimo = 0
ficha = None
ficha2 = None

for idade in idades:
    if idade > maximo:
        maximo = idade
    if c < 1:
        minimo = idade
    else:
        if idade > 0 and idade < minimo:
            minimo = idade
    c = c + 1
    soma = soma + idade

media = soma / len(idades)
print(f"Total de moradores com idade declarada: {len(idades)}")
print(f"Soma das idades: {soma}")
print(f"Média de idade: {media:.1f} anos")
print(f'Morador com maior idade tem {maximo} anos')
print(f'Morador com menor idade tem {minimo} anos')'''

# exercicio 2_2

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")

escolaridade_nome = {
    1: "Sem instrução",
    2: "Fundamental incompleto",
    3: "Fundamental completo",
    4: "Médio incompleto",
    5: "Médio completo",
    6: "Superior incompleto",
    7: "Superior completo",
    8: "Sem classificação",
}

contagem = {}
for _, linha in moradores.iterrows():
    nivel = linha["escolaridade"]
    if nivel in escolaridade_nome:
        if nivel not in contagem:
            contagem[nivel] = 0
        contagem[nivel] += 1

print("Escolaridade dos moradores:")
for nivel, total in contagem.items():
    print(f"  {escolaridade_nome[nivel]}: {total} moradores")'''

# exercício 2_3

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")

ra_alvo = 5320  # Gama

filtro = moradores[moradores["localidade"] == ra_alvo]

print(f"Moradores da RA {ra_alvo}:")
for _, linha in filtro.iterrows():
    print(f"  {linha['morador_id']} — {linha['idade_calculada']} anos — escolaridade: {linha['escolaridade']}")'''

# exercicio 2_4

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")

com_renda = moradores[(moradores["renda_ind"] > 0) & (moradores["renda_ind"] != 99999)]

soma = 0

print(f"Moradores com renda declarada: {len(com_renda)}")
for _, linha in com_renda.iterrows():
    soma += linha['renda_ind']
    print(f"  {linha['morador_id']} — R$ {linha['renda_ind']:,.0f}")
print(f'A média de salário dos valores é R$ {soma/len(com_renda):.2f}')'''

# exercicio 3_1

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")

validos = moradores[moradores["idade_calculada"] != 99999].copy()
lista = validos[["morador_id", "idade_calculada"]].head(450).to_dict("records")

# Bubble Sort por idade
n = len(lista)
soma = 0
for i in range(n):
    for j in range(n - i - 1):
        if lista[j]["idade_calculada"] > lista[j + 1]["idade_calculada"]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Moradores ordenados do mais novo ao mais velho:")
for m in lista:
    soma += 1
    print(f"  {m['morador_id']}: {m['idade_calculada']} anos")
print(f'Total de trocas para ordenar do menor para o maior {soma} vezes')'''

#exercício 3_2

'''import pandas as pd

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")

com_renda = moradores[(moradores["renda_ind"] > 0) & (moradores["renda_ind"] != 99999)].copy()
lista = com_renda[["morador_id", "renda_ind", "escolaridade",]].head(450).to_dict("records")

# Selection Sort por renda (crescente)
n = len(lista)
for i in range(n):
    idx_min = i
    for j in range(i + 1, n):
        if lista[j]["renda_ind"] > lista[idx_min]["renda_ind"]:
            idx_min = j
    lista[i], lista[idx_min] = lista[idx_min], lista[i]

print("Moradores ordenados por renda (maior para menor):")
for m in lista:
    print(f"  {m['morador_id']}: R$ {m['renda_ind']:,.0f}, e nivel de escolaridade {m['escolaridade']}")'''

# exercício 3_3

'''import pandas as pd

moradores = pd.read_csv(
    "semana12/moradores.csv" , sep=";" , decimal="," , encoding="utf-8-sig")

ra_nomes = {
    5249: "Arniqueira",
    5301: "Brasília",
    5303: "Taguatinga",
    5305: "Sobradinho",
    5311: "Cruzeiro",
    5313: "Ceilândia",
    5314: "Sobradinho II",
    5315: "Jardim Botânico",
    5319: "Lago Sul",
    5320: "Gama",
    5326: "Samambaia",
    5328: "Santa Maria",
    5330: "São Sebastião",
}

# Obtém os códigos das RAs
codigos = moradores["localidade"].unique().tolist()

# Cria lista de RAs
ras = [{"codigo": c, "nome": ra_nomes.get(c, f"RA-{c}")} for c in codigos]

# Insertion Sort por nome
for i in range(1, len(ras)):
    chave = ras[i]
    j = i - 1

    while j >= 0 and ras[j]["nome"] > chave["nome"]:
        ras[j + 1] = ras[j]
        j -= 1

    ras[j + 1] = chave

print("Regiões Administrativas (ordem alfabética):")

for ra in ras:

    moradores_ra = moradores[
        (moradores["localidade"] == ra["codigo"]) &
        (moradores["idade_calculada"] != 99999)
    ]

    total = len(moradores_ra)

    media_idade = moradores_ra["idade_calculada"].mean()

    print(
        f"  {ra['nome']} - média de idade: {media_idade:.1f} anos "
        f"(cód. {ra['codigo']}): {total} moradores na amostra")'''

#exercicio 4_1

# relatorio_moradores.py
import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Uso: python relatorio_moradores.py <nome_do_arquivo.txt>")
    sys.exit(1)

arquivo_saida = sys.argv[1]

moradores = pd.read_csv("semana12/moradores.csv", sep=";", decimal=",", encoding="utf-8-sig")
validos = moradores[moradores["idade_calculada"] != 99999]
idades = validos["idade_calculada"].tolist()
media_idade = sum(idades) / len(idades)

linhas = []
linhas.append("=" * 50)
linhas.append("RELATÓRIO PDAD 2024 — MORADORES")
linhas.append("=" * 50)
linhas.append(f"Total de moradores na amostra : {len(moradores)}")
linhas.append(f"Com idade declarada           : {len(validos)}")
linhas.append(f"Média de idade                : {media_idade:.1f} anos")
linhas.append(f"Idade mínima                  : {min(idades)} anos")
linhas.append(f"Idade máxima                  : {max(idades)} anos")
linhas.append("")

with open(arquivo_saida, "w", encoding="utf-8") as f:
    for linha in linhas:
        f.write(linha + "\n")

print(f"Relatório salvo em: {arquivo_saida}")