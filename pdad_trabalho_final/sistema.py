#Codigo desenvolvido por Emilio de Souza Santos júnior

# exporta os módulos do progrma para main, para reconhecer as funcionalidades 
from utils.carregar import carregar_dados, tratar_dados, carregar_ras
from utils.interface import criar_janela, criar_filtros, criar_area_estatisticas, criar_botoes


moradores = carregar_dados()
dados = tratar_dados(moradores)
ras = carregar_ras()

janela = criar_janela(dados)

combo_ra, combo_genero, combo_escolaridade, combo_cor = criar_filtros(janela, ras)

labels = criar_area_estatisticas(janela)

criar_botoes(
    janela,
    dados,
    ras,
    combo_ra,
    combo_genero,
    combo_escolaridade,
    combo_cor,
    labels
)

janela.mainloop()