from utils.filtros import obter_dados_filtrados


def calcular_estatisticas(dados_filtrados):
    quantidade = len(dados_filtrados)

    media = dados_filtrados["renda_ind"].mean()

    rendas_positivas = dados_filtrados[dados_filtrados["renda_ind"] > 0]["renda_ind"]

    if len(rendas_positivas) > 0:
        menor = rendas_positivas.min()
    else:
        menor = 0

    maior = dados_filtrados["renda_ind"].max()

    return {
        "quantidade": quantidade,
        "media": media,
        "menor": menor,
        "maior": maior
    }


def atualizar_estatisticas(dados, ras, combo_ra, combo_genero, combo_escolaridade, combo_cor, labels):
    dados_filtrados = obter_dados_filtrados(
        dados,
        ras,
        combo_ra,
        combo_genero,
        combo_escolaridade,
        combo_cor
    )

    estatisticas = calcular_estatisticas(dados_filtrados)

    label_quantidade, label_media, label_menor, label_maior = labels

    label_quantidade.config(text=f"Moradores analisados: {estatisticas['quantidade']}")
    label_media.config(text=f"Renda média: R$ {estatisticas['media']:.2f}")
    label_menor.config(text=f"Menor renda: R$ {estatisticas['menor']:.2f}")
    label_maior.config(text=f"Maior renda: R$ {estatisticas['maior']:.2f}")