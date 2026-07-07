import pandas as pd
from pathlib import Path
import pandas as pd


def carregar_dados():

    caminho = Path(__file__).resolve().parent.parent / "dados" / "moradores.csv"

    moradores = pd.read_csv(caminho, sep=";", decimal=",", encoding="utf-8-sig", low_memory=False)

    return moradores


def tratar_dados(moradores):
    dados = moradores[["localidade", "renda_ind", "escolaridade", "id_genero", "E05"]].copy()

    dados = dados[(dados["renda_ind"] != 99999) & (dados["renda_ind"] != 88888)]
    dados = dados[dados["id_genero"] != 99999]

    return dados


def carregar_ras():
    """
    Retorna um dicionário com os códigos e nomes das Regiões Administrativas
    do Distrito Federal, conforme o Anexo 1 do dicionário da PDAD 2024.
    """

    ras = {
        5301: "Plano Piloto",
        5302: "Gama",
        5303: "Taguatinga",
        5304: "Brazlândia",
        5305: "Sobradinho",
        5306: "Planaltina",
        5307: "Paranoá",
        5308: "Núcleo Bandeirante",
        5309: "Ceilândia",
        5310: "Guará",
        5311: "Cruzeiro",
        5312: "Samambaia",
        5313: "Santa Maria",
        5314: "São Sebastião",
        5315: "Recanto Das Emas",
        5316: "Lago Sul",
        5317: "Riacho Fundo",
        5318: "Lago Norte",
        5319: "Candangolândia",
        5320: "Águas Claras",
        5321: "Riacho Fundo II",
        5322: "Sudoeste e Octogonal",
        5323: "Varjão",
        5324: "Park Way",
        5325: "SCIA",
        5326: "Sobradinho II",
        5327: "Jardim Botânico",
        5328: "Itapoã",
        5329: "SIA",
        5330: "Vicente Pires",
        5331: "Fercal",
        5332: "Sol Nascente / Pôr do Sol",
        5333: "Arniqueira",
        5334: "Arapoanga",
        5335: "Água Quente",
    }

    return ras