import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils.filtros import obter_dados_filtrados

# mostra o grafico na tela, atraves do histograma separado em 30 intervalos
def mostrar_graficos(dados, ras, combo_ra, combo_genero, combo_escolaridade, combo_cor):
    dados_filtrados = obter_dados_filtrados(
        dados,
        ras,
        combo_ra,
        combo_genero,
        combo_escolaridade,
        combo_cor
    )

    janela_grafico = tk.Toplevel()
    janela_grafico.title("Gráficos da Análise de Renda")
    janela_grafico.geometry("900x650")

    figura, eixos = plt.subplots(2, 1, figsize=(9, 7))

    rendas_grafico = dados_filtrados[dados_filtrados["renda_ind"] <= 20000]

    eixos[0].hist(rendas_grafico["renda_ind"], bins=30)
    eixos[0].set_title("Distribuição da renda individual (até R$ 20.000)")
    eixos[0].set_xlabel("Renda individual (R$)")
    eixos[0].set_ylabel("Quantidade de moradores")

    nomes_escolaridade = {
        1: "Sem instrução",
        2: "Fund. inc.",
        3: "Fund. comp.",
        4: "Médio inc.",
        5: "Médio comp.",
        6: "Sup. inc.",
        7: "Sup. comp.",
        8: "Sem class."
    }

    medias = dados_filtrados.groupby("escolaridade")["renda_ind"].mean()

    categorias = [
        nomes_escolaridade.get(codigo, str(codigo))
        for codigo in medias.index
    ]

    eixos[1].bar(categorias, medias.values)
    eixos[1].set_title("Renda média por escolaridade")
    eixos[1].set_xlabel("Escolaridade")
    eixos[1].set_ylabel("Renda média (R$)")
    eixos[1].tick_params(axis="x", rotation=30)

    figura.tight_layout()

    canvas = FigureCanvasTkAgg(figura, master=janela_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    #fecha o grafico para não ficar rodando em segundo plano
    def fechar_grafico():
        plt.close("all")
        janela_grafico.destroy()

    janela_grafico.protocol("WM_DELETE_WINDOW", fechar_grafico)