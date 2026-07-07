import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk

from utils.estatisticas import atualizar_estatisticas
from utils.graficos import mostrar_graficos
from utils.exportacao import exportar_estatisticas
from utils.ranking import mostrar_top5_ras


def criar_janela(dados):
    """
    Cria a janela principal do sistema.
    """

    janela = tk.Tk()

    janela.title("Sistema de Análise de Renda - PDAD 2024")
    janela.geometry("1000x720")
    janela.minsize(900, 650)

    titulo = tk.Label(
        janela,
        text="Sistema de Análise de Renda - PDAD 2024",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=(25, 8))

    descricao = tk.Label(
        janela,
        text="Análise da distribuição de renda individual no Distrito Federal\n"
             "utilizando os Microdados da PDAD 2024.",
        font=("Arial", 10)
    )
    descricao.pack(pady=(0, 12))

    registros = tk.Label(
        janela,
        text=f"Registros válidos para análise: {len(dados)} moradores",
        font=("Arial", 10, "bold")
    )
    registros.pack(pady=(0, 22))

    def fechar_programa():
        plt.close("all")
        janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", fechar_programa)

    return janela


def criar_filtros(janela, ras):
    """
    Cria os filtros da interface gráfica.
    """

    frame_filtros = tk.Frame(janela)
    frame_filtros.pack(pady=25)

    lista_ras = ["Todas as Regiões"] + list(ras.values())

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

    tk.Label(frame_filtros, text="Região Administrativa:", font=("Arial", 11)).grid(
        row=0, column=0, padx=10, pady=5, sticky="e"
    )

    combo_ra = ttk.Combobox(
        frame_filtros,
        values=lista_ras,
        state="readonly",
        width=28
    )
    combo_ra.current(0)
    combo_ra.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_filtros, text="Gênero:", font=("Arial", 11)).grid(
        row=1, column=0, padx=10, pady=5, sticky="e"
    )

    combo_genero = ttk.Combobox(
        frame_filtros,
        values=list(generos.keys()),
        state="readonly",
        width=28
    )
    combo_genero.current(0)
    combo_genero.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_filtros, text="Escolaridade:", font=("Arial", 11)).grid(
        row=2, column=0, padx=10, pady=5, sticky="e"
    )

    combo_escolaridade = ttk.Combobox(
        frame_filtros,
        values=list(escolaridades.keys()),
        state="readonly",
        width=28
    )
    combo_escolaridade.current(0)
    combo_escolaridade.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_filtros, text="Cor/Raça:", font=("Arial", 11)).grid(
        row=3, column=0, padx=10, pady=5, sticky="e"
    )

    combo_cor = ttk.Combobox(
        frame_filtros,
        values=list(cores_racas.keys()),
        state="readonly",
        width=28
    )
    combo_cor.current(0)
    combo_cor.grid(row=3, column=1, padx=10, pady=5)

    return combo_ra, combo_genero, combo_escolaridade, combo_cor


def criar_area_estatisticas(janela):
    """
    Cria os rótulos que exibem as estatísticas na interface.
    """

    frame_estatisticas = tk.Frame(janela)
    frame_estatisticas.pack(pady=18)

    titulo = tk.Label(
        frame_estatisticas,
        text="Estatísticas da renda",
        font=("Arial", 13, "bold")
    )
    titulo.grid(row=0, column=0, columnspan=2, pady=8)

    label_quantidade = tk.Label(
        frame_estatisticas,
        text="Moradores analisados: -",
        font=("Arial", 11)
    )
    label_quantidade.grid(row=1, column=0, sticky="w", padx=10, pady=3)

    label_media = tk.Label(
        frame_estatisticas,
        text="Renda média: -",
        font=("Arial", 11)
    )
    label_media.grid(row=2, column=0, sticky="w", padx=10, pady=3)

    label_menor = tk.Label(
        frame_estatisticas,
        text="Menor renda: -",
        font=("Arial", 11)
    )
    label_menor.grid(row=3, column=0, sticky="w", padx=10, pady=3)

    label_maior = tk.Label(
        frame_estatisticas,
        text="Maior renda: -",
        font=("Arial", 11)
    )
    label_maior.grid(row=4, column=0, sticky="w", padx=10, pady=3)

    return label_quantidade, label_media, label_menor, label_maior


def criar_botoes(
    janela,
    dados,
    ras,
    combo_ra,
    combo_genero,
    combo_escolaridade,
    combo_cor,
    labels
):
    """
    Cria os botões da interface.
    """

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=8)

    botao_atualizar = tk.Button(
        frame_botoes,
        text="Atualizar Estatísticas",
        width=22,
        command=lambda: atualizar_estatisticas(
            dados,
            ras,
            combo_ra,
            combo_genero,
            combo_escolaridade,
            combo_cor,
            labels
        )
    )

    botao_top5 = tk.Button(
        frame_botoes,
        text="Top 5 RAs",
        width=22,
        command=lambda: mostrar_top5_ras(dados, ras)
    )

    botao_grafico = tk.Button(
        frame_botoes,
        text="Mostrar Gráficos",
        width=22,
        command=lambda: mostrar_graficos(
            dados,
            ras,
            combo_ra,
            combo_genero,
            combo_escolaridade,
            combo_cor
        )
    )

    botao_exportar = tk.Button(
        frame_botoes,
        text="Exportar (.txt)",
        width=22,
        command=lambda: exportar_estatisticas(
            dados,
            ras,
            combo_ra,
            combo_genero,
            combo_escolaridade,
            combo_cor
        )
    )

    botao_atualizar.grid(row=0, column=0, padx=6, pady=5)
    botao_top5.grid(row=0, column=1, padx=6, pady=5)
    botao_grafico.grid(row=1, column=0, padx=6, pady=5)
    botao_exportar.grid(row=1, column=1, padx=6, pady=5)

    return botao_atualizar