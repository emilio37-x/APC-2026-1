# cria os filtros

def filtrar_dados(dados, ra=None, genero=None, escolaridade=None, cor=None):
    dados_filtrados = dados.copy()

    if ra is not None:
        dados_filtrados = dados_filtrados[dados_filtrados["localidade"] == ra]

    if genero is not None:
        dados_filtrados = dados_filtrados[dados_filtrados["id_genero"] == genero]

    if escolaridade is not None:
        dados_filtrados = dados_filtrados[dados_filtrados["escolaridade"] == escolaridade]

    if cor is not None:
        dados_filtrados = dados_filtrados[dados_filtrados["E05"] == cor]

    return dados_filtrados

#recebe os dados filtrados e armazena para ser mostrado na tela
def obter_dados_filtrados(dados, ras, combo_ra, combo_genero, combo_escolaridade, combo_cor):
    generos = {
        "Todos os gêneros": None,
        "Cisgênero": 1,
        "Transgênero": 2,
        "Outro": 3
    }

    escolaridades = {
        "Todas as escolaridades": None,
        "Sem instrução": 1,
        "Fundamental incompleto": 2,
        "Fundamental completo": 3,
        "Médio incompleto": 4,
        "Médio completo": 5,
        "Superior incompleto": 6,
        "Superior completo": 7,
        "Sem classificação": 8
    }

    cores_racas = {
        "Todas as cores/raças": None,
        "Branca": 1,
        "Preta": 2,
        "Amarela": 3,
        "Parda": 4,
        "Indígena": 5
    }

    ra_nome = combo_ra.get()

    if ra_nome == "Todas as Regiões":
        ra_codigo = None
    else:
        ra_codigo = None
        for codigo, nome in ras.items():
            if nome == ra_nome:
                ra_codigo = codigo
                break

    return filtrar_dados(
        dados,
        ra=ra_codigo,
        genero=generos[combo_genero.get()],
        escolaridade=escolaridades[combo_escolaridade.get()],
        cor=cores_racas[combo_cor.get()]
    )