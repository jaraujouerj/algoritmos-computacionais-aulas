import csv
from collections import Counter

CAMINHO_ARQUIVO = "dadosproducao.csv"

# Lê os dados do arquivo CSV e retorna uma lista de dicionários
def ler_dados(caminho):
    dados = []
    with open(caminho, newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(dict(linha))
    return dados

# Filtra os registros por status
def filtrar_por_status(registros, status):
    status_validos = {"Aprovado", "Retrabalho", "Descarte"}
    if status not in status_validos:
        return []
    return [registro for registro in registros if registro["status"] == status]

# Calcula a média de tempo_ciclo_seg de uma lista de registros
def calcular_media_tempo_ciclo(registros):
    tempos = [float(registro["tempo_ciclo_seg"]) for registro in registros if registro["tempo_ciclo_seg"]]
    if not tempos:
        return 0.0
    return sum(tempos) / len(tempos)

# Retorna a média de tempo_ciclo_seg separada por status Aprovado e Retrabalho
def tempo_medio_ciclo(registros):
    media_aprovado = calcular_media_tempo_ciclo(filtrar_por_status(registros, "Aprovado"))
    media_retrabalho = calcular_media_tempo_ciclo(filtrar_por_status(registros, "Retrabalho"))
    return media_aprovado, media_retrabalho

# Retorna o nome da máquina com mais registros em Retrabalho ou Descarte
def pior_maquina_por_defeitos(registros):
    contagem = {}
    for registro in registros:
        if registro["status"] in ("Retrabalho", "Descarte"):
            maquina = registro["maquina"]
            contagem[maquina] = contagem.get(maquina, 0) + 1
    if not contagem:
        return None
    return max(contagem, key=contagem.get)

# Retorna (total_pecas, aprovadas, retrabalho, descarte) de um operador específico
def resumo_por_operador(registros, nome_operador):
    registros_operador = [registro for registro in registros if registro["operador"] == nome_operador]
    total_pecas = len(registros_operador)
    aprovadas = len(filtrar_por_status(registros_operador, "Aprovado"))
    retrabalho = len(filtrar_por_status(registros_operador, "Retrabalho"))
    descarte = len(filtrar_por_status(registros_operador, "Descarte"))
    return total_pecas, aprovadas, retrabalho, descarte

# Conta quantas peças cada máquina produziu
def contar_producao_por_maquina(registros):
    producao_por_maquina = {}
    for registro in registros:
        maquina = registro["maquina"]
        producao_por_maquina[maquina] = producao_por_maquina.get(maquina, 0) + 1
    return producao_por_maquina

# Mesma contagem, agora usando Counter
def contar_producao_por_maquina_counter(registros):
    return Counter(registro["maquina"] for registro in registros)

# Monta um dicionário com o total e a contagem por status de cada máquina
def resumo_detalhado_por_maquina(registros):
    resumo = {}
    for registro in registros:
        maquina = registro["maquina"]
        status = registro["status"]
        if maquina not in resumo:
            resumo[maquina] = {"total": 0, "aprovadas": 0, "retrabalho": 0, "descarte": 0}
        resumo[maquina]["total"] += 1
        if status == "Aprovado":
            resumo[maquina]["aprovadas"] += 1
        elif status == "Retrabalho":
            resumo[maquina]["retrabalho"] += 1
        elif status == "Descarte":
            resumo[maquina]["descarte"] += 1
    return resumo

# Monta um dicionário com o total e a contagem por status de cada operador
def resumo_detalhado_por_operador(registros):
    resumo = {}
    for registro in registros:
        operador = registro["operador"]
        status = registro["status"]
        if operador not in resumo:
            resumo[operador] = {"total": 0, "aprovadas": 0, "retrabalho": 0, "descarte": 0}
        resumo[operador]["total"] += 1
        if status == "Aprovado":
            resumo[operador]["aprovadas"] += 1
        elif status == "Retrabalho":
            resumo[operador]["retrabalho"] += 1
        elif status == "Descarte":
            resumo[operador]["descarte"] += 1
    return resumo

# Retorna o operador com maior taxa de retrabalho+descarte e a respectiva taxa
def operador_maior_taxa_defeitos(registros):
    resumo = resumo_detalhado_por_operador(registros)
    pior_operador = None
    maior_taxa = -1
    for operador, dados_operador in resumo.items():
        taxa = (dados_operador["retrabalho"] + dados_operador["descarte"]) / dados_operador["total"]
        if taxa > maior_taxa:
            maior_taxa = taxa
            pior_operador = operador
    return pior_operador, maior_taxa


if __name__ == "__main__":
    dados = ler_dados(CAMINHO_ARQUIVO)
    for registro in dados[:5]:
        print(registro)
        print("id_peça: ", registro["id_peca"], 
              "maquina: ", registro["maquina"], 
              "defeito: ", registro["defeito"])

    aprovados = filtrar_por_status(dados, "Aprovado")
    print(f"\nTotal de registros com status 'Aprovado': {len(aprovados)}")

    media_aprovado, media_retrabalho = tempo_medio_ciclo(dados)
    print(f"Tempo médio de ciclo (Aprovado): {media_aprovado:.2f}s")
    print(f"Tempo médio de ciclo (Retrabalho): {media_retrabalho:.2f}s")

    print(f"Pior máquina (Retrabalho/Descarte): {pior_maquina_por_defeitos(dados)}")

    total_pecas, aprovadas, retrabalho, descarte = resumo_por_operador(dados, "Ana")
    print(f"Resumo Ana -> total: {total_pecas}, aprovadas: {aprovadas}, retrabalho: {retrabalho}, descarte: {descarte}")

    producao_por_maquina = contar_producao_por_maquina(dados)
    print(f"Produção por máquina: {producao_por_maquina}")

    producao_por_maquina_counter = contar_producao_por_maquina_counter(dados)
    print(f"Produção por máquina (Counter): {producao_por_maquina_counter}")

    resumo_maquinas = resumo_detalhado_por_maquina(dados)
    for maquina, resumo in resumo_maquinas.items():
        print(f"{maquina}: {resumo}")

    resumo_operadores = resumo_detalhado_por_operador(dados)
    for operador, resumo in resumo_operadores.items():
        print(f"{operador}: {resumo}")

    pior_operador, maior_taxa = operador_maior_taxa_defeitos(dados)
    print(f"Operador com maior taxa de retrabalho+descarte: {pior_operador} ({maior_taxa:.2%})")
