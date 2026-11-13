"""Gera as figuras usadas nas aulas 27 (Matplotlib) a 29 (Pandas).

Uso (a partir da pasta slides/figuras):  python gera_figuras.py
Requer: numpy, pandas, matplotlib.
Os dados de produção vêm de ../../Projeto1/dadosproducao.csv.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

AZUL = "#003e7e"
OURO = "#b07c00"
CINZA = "#7a8594"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True,
                     "grid.alpha": 0.25, "figure.dpi": 150})
SAIDA = dict(bbox_inches="tight")

# 1) gráfico de linha: seno e cosseno
x = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.plot(x, np.sin(x), color=AZUL, label="sen(x)")
ax.plot(x, np.cos(x), color=OURO, linestyle="--", label="cos(x)")
ax.set_title("Seno e cosseno")
ax.set_xlabel("x (rad)")
ax.set_ylabel("y")
ax.legend()
fig.savefig("fig_linha.png", **SAIDA)

# 2) dispersão com ajuste de reta (ensaio de resistor)
V = np.array([5.0, 10.0, 15.0, 20.0])
I = np.array([0.25, 0.52, 0.76, 1.01])
a, b = np.polyfit(V, I, 1)
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.scatter(V, I, color=AZUL, zorder=3, label="medidas")
xx = np.linspace(0, 22, 50)
ax.plot(xx, a * xx + b, color=OURO, label=f"ajuste: I = {a:.4f} V + {b:.4f}")
ax.set_title("Ensaio de um resistor")
ax.set_xlabel("Tensão (V)")
ax.set_ylabel("Corrente (A)")
ax.legend()
fig.savefig("fig_dispersao.png", **SAIDA)

# 3) subplots 2 x 2 (quarteto de Anscombe, valores clássicos)
xs = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
ys = [
    [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
    [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
    [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
conj = [(xs, ys[0]), (xs, ys[1]), (xs, ys[2]), (x4, y4)]
fig, axs = plt.subplots(2, 2, figsize=(6, 4.2), sharex=True, sharey=True)
for k, (ax, (xi, yi)) in enumerate(zip(axs.ravel(), conj)):
    ax.scatter(xi, yi, color=AZUL, s=18)
    ax.set_title(["I", "II", "III", "IV"][k], fontsize=10)
    ax.set_xlim(2, 20)
    ax.set_ylim(2, 14)
fig.suptitle("Quarteto de Anscombe: mesma média, mesma reta, dados diferentes")
fig.tight_layout()
fig.savefig("fig_anscombe.png", **SAIDA)

# 4-6) dados de produção
df = pd.read_csv("../../Projeto1/dadosproducao.csv")

fig, ax = plt.subplots(figsize=(6, 3.2))
ax.hist(df["tempo_ciclo_seg"], bins=10, color=AZUL, edgecolor="white")
ax.set_title("Distribuição do tempo de ciclo")
ax.set_xlabel("Tempo de ciclo (s)")
ax.set_ylabel("Número de peças")
fig.savefig("fig_hist.png", **SAIDA)

maqs = sorted(df["maquina"].unique())
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.boxplot([df.loc[df.maquina == m, "tempo_ciclo_seg"] for m in maqs],
           tick_labels=maqs, patch_artist=True,
           boxprops=dict(facecolor="#cfdcf0", color=AZUL),
           medianprops=dict(color=OURO, linewidth=2))
ax.set_title("Tempo de ciclo por máquina")
ax.set_xlabel("Máquina")
ax.set_ylabel("Tempo de ciclo (s)")
fig.savefig("fig_boxplot.png", **SAIDA)

tab = df.groupby("maquina")["status"].value_counts().unstack(fill_value=0)
tab = tab[["Aprovado", "Retrabalho", "Descarte"]]
fig, ax = plt.subplots(figsize=(6, 3.2))
tab.plot(kind="bar", stacked=True, ax=ax, color=[AZUL, OURO, "#b3261e"],
         rot=0)
ax.set_title("Situação das peças por máquina")
ax.set_xlabel("Máquina")
ax.set_ylabel("Peças")
ax.set_ylim(0, 23)
ax.legend(title=None, ncol=3, loc="upper center")
fig.savefig("fig_barras.png", **SAIDA)
fig, ax = plt.subplots(figsize=(6, 3.2))
(df.groupby("maquina")["tempo_ciclo_seg"].mean()
   .plot(kind="bar", rot=0, color=AZUL, ax=ax))
ax.set_title("Tempo médio de ciclo por máquina")
ax.set_xlabel("Máquina")
ax.set_ylabel("Tempo médio (s)")
fig.savefig("fig_media.png", **SAIDA)
print("figuras geradas")
