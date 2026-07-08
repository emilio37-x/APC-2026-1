from tkinter import filedialog

from utils.filtros import obter_dados_filtrados
from utils.estatisticas import calcular_estatisticas

#Exporta um arquivo txt com os filtros aplicados e as informações geradas

def exportar_estatisticas(dados, ras, combo_ra, combo_genero, combo_escolaridade, combo_cor):
    dados_filtrados = obter_dados_filtrados(
        dados,
        ras,
        combo_ra,
        combo_genero,
        combo_escolaridade,
        combo_cor
    )

    estatisticas = calcular_estatisticas(dados_filtrados)

    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de texto", "*.txt")],
        title="Salvar estatísticas"
    )

    if not caminho:
        return

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write("Sistema de Análise de Renda - PDAD 2024\n")
        arquivo.write("=" * 45 + "\n\n")

        arquivo.write(f"Região Administrativa: {combo_ra.get()}\n")
        arquivo.write(f"Gênero: {combo_genero.get()}\n")
        arquivo.write(f"Escolaridade: {combo_escolaridade.get()}\n")
        arquivo.write(f"Cor/Raça: {combo_cor.get()}\n\n")

        arquivo.write(f"Moradores analisados: {estatisticas['quantidade']}\n")
        arquivo.write(f"Renda média: R$ {estatisticas['media']:.2f}\n")
        arquivo.write(f"Menor renda: R$ {estatisticas['menor']:.2f}\n")
        arquivo.write(f"Maior renda: R$ {estatisticas['maior']:.2f}\n")