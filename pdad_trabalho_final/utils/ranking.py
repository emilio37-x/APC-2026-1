import tkinter as tk

#usando a rend_ind, usamos o metodo buble sort para ordenar do maior para o menor de acordo com as Ras
def ranking_ras_bubble_sort(dados, ras):
    ranking = []

    for codigo, nome in ras.items():
        dados_ra = dados[dados["localidade"] == codigo]
        rendas_positivas = dados_ra[dados_ra["renda_ind"] > 0]["renda_ind"]

        if len(rendas_positivas) > 0:
            media = rendas_positivas.mean()
            ranking.append([nome, media])

    n = len(ranking)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ranking[j][1] < ranking[j + 1][1]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

    return ranking[:5]

# aqui cria uma janela onde irá mostrar o top 5 da lista que ordenamos e crimaos a cimaa com o buble sort
def mostrar_top5_ras(dados, ras):
    top5 = ranking_ras_bubble_sort(dados, ras)

    janela_top5 = tk.Toplevel()
    janela_top5.title("Top 5 RAs por renda média")
    janela_top5.geometry("450x300")

    titulo = tk.Label(
        janela_top5,
        text="Top 5 RAs com maior renda média",
        font=("Arial", 14, "bold")
    )
    titulo.pack(pady=15)

    for i, item in enumerate(top5, start=1):
        nome = item[0]
        media = item[1]

        texto = f"{i}º - {nome}: R$ {media:.2f}"

        tk.Label(
            janela_top5,
            text=texto,
            font=("Arial", 11)
        ).pack(pady=4)