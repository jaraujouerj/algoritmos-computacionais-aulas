import csv

CAMINHO_ARQUIVO = "dadosproducao.csv"

def ler_dados(caminho):
    dados = []
    with open(caminho) as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # pula o cabeçalho
        for linha in leitor:
            id_peca, maquina, operador, turno, timestamp, tempo_ciclo_seg, status, defeito = linha
            dados.append((id_peca, maquina, operador, turno, timestamp, tempo_ciclo_seg, status, defeito))
    return dados


if __name__ == "__main__":
    dados = ler_dados(CAMINHO_ARQUIVO)
    for registro in dados[:5]:
        print(registro)
