# Algoritmos Computacionais I: slides e exemplos

Material da disciplina **Algoritmos Computacionais I** (UERJ), dada a cursos de engenharia,
baseado no livro *Introdução à Programação e aos Algoritmos* (J. A. Ribeiro, LTC, 2019).

O livro e este material servem a qualquer curso de graduação que ensine computação, e também a
quem quer aprender por conta própria: os slides, os exemplos e os notebooks podem ser usados e
adaptados para outras turmas e áreas (veja as licenças no fim).

* **Repositório:** <https://github.com/jaraujouerj/algoritmos-computacionais-aulas> ([baixar tudo em ZIP](https://github.com/jaraujouerj/algoritmos-computacionais-aulas/archive/refs/heads/main.zip))
* **Slides** em LaTeX (Beamer, 16:9): um arquivo por aula, em [`slides/`](slides/).
* **Exemplos de código** do livro, em Python, em [`code/`](code/).
* **Site com exercícios e soluções comentadas:** <https://www.araujo.eng.uerj.br/livro/>

Os slides compilados (PDF) estão na página de slides do site:
<https://www.araujo.eng.uerj.br/livro/slides/>. Os PDFs não são versionados neste
repositório, pois são gerados a partir dos `.tex`.

## Estrutura

```
slides/             aulas (aulaNN_*.tex, C1_* e C2_*), estilo ac1.sty, Makefile, figuras/
code/CapN/          programas do livro, por capítulo (prog.N.x_nome.py)
code/Projeto1/      exemplo de leitura de arquivo CSV (aulas 23 e 27 a 29)
notebooks/          notebooks Jupyter das aulas 27 a 29 (Matplotlib e Pandas)
imagens/            figuras usadas nos slides
template_aula.tex   template Beamer autônomo, para criar uma aula nova
```

A tabela que liga cada aula ao seu arquivo está em [`slides/LEIAME.md`](slides/LEIAME.md).
A disciplina tem 35 aulas em 4 blocos; as aulas 15 e 25 são provas e não têm slides.
`C1_recursao` e `C2_ordenacao` são **apresentações extras** para Engenharia de Computação.

## Como compilar os slides

Requisitos: uma distribuição TeX (TeX Live ou MiKTeX) com `beamer` e `latexmk`.

```bash
cd slides
make                                   # todas as aulas
make aula05_bases_da_programacao.pdf   # uma aula
make clean                             # remove PDFs e arquivos auxiliares
```

As figuras das aulas 27 a 29 já estão em `slides/figuras/`. Para regerá-las:
`python3 slides/figuras/gera_figuras.py` (precisa de `numpy`, `pandas` e `matplotlib`).

### Sobre o logo da instituição

Os slides foram feitos com o logo da UERJ no cabeçalho e na capa. **O logo não faz parte
deste repositório** (marca institucional). Sem o arquivo, os slides compilam normalmente,
só que sem logo. Para usar o seu:

1. Coloque a imagem em `imagens/logo_uerj_cor_transparencia.png` (ou mude o caminho em
   `\logouerj`, no arquivo `slides/ac1.sty`);
2. Ajuste o nome e a instituição no mesmo arquivo (`\autor`, `\instituicao`).

## Exemplos de código

Os programas seguem a numeração do livro: `code/Cap4/prog.4.16_calcula_pi.py` é o
Programa 4.16. Cada slide cita, no rodapé, os arquivos relacionados ao assunto da página.
Para executar:

```bash
python3 code/Cap4/prog.4.16_calcula_pi.py
```

Os exemplos de NumPy, Pandas e Matplotlib (aulas 21 e 27 a 29) exigem
`pip install numpy pandas matplotlib`.

## Notebooks

Complemento para as aulas 27 a 29, de apoio aos trabalhos com análise de dados. **Não fazem
parte do livro.**

* [`notebooks/tutorial_de_matplotlib.ipynb`](notebooks/tutorial_de_matplotlib.ipynb): aula 27 (gráficos
  de linha, dispersão, histograma, *boxplot*, barras).
  [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jaraujouerj/algoritmos-computacionais-aulas/blob/main/notebooks/tutorial_de_matplotlib.ipynb)
* [`notebooks/introducao_ao_pandas.ipynb`](notebooks/introducao_ao_pandas.ipynb): aulas 28 e 29
  (`DataFrame`, filtros, `groupby`, valores ausentes).
  [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jaraujouerj/algoritmos-computacionais-aulas/blob/main/notebooks/introducao_ao_pandas.ipynb)

Podem ser abertos com `jupyter lab` ou enviados ao Google Colab. Requerem `numpy`, `pandas`,
`matplotlib` (versão 3.9 ou mais nova) e `seaborn`, e **acesso à internet**: o notebook de
Pandas baixa o `gapminder.tsv` do repositório do Gapminder (sem internet, salve o arquivo na
pasta do notebook e ele será usado), e o de Matplotlib carrega conjuntos de dados de exemplo
do `seaborn`.

## O que não está neste repositório

* o texto do livro e seus PDFs;
* o logo da UERJ;
* provas, listas de avaliação e trabalhos de alunos.

## Créditos

* Os dois notebooks são **versões bastante simplificadas** de material do livro *Pandas for
  Everyone*, de Daniel Chen (Addison-Wesley). O texto e os exemplos originais pertencem ao
  autor e à editora; quem quiser o conteúdo completo deve consultar o livro.
* O notebook de Pandas usa dados do **Gapminder** (<https://www.gapminder.org/data/>), sob a
  licença Creative Commons Attribution 4.0 International (CC BY 4.0).

## Licenças

* Slides, estilo e figuras: **CC BY-SA 4.0**, em [`LICENSE-SLIDES.md`](LICENSE-SLIDES.md).
* Código dos exemplos: **MIT**, em [`LICENSE-CODIGO`](LICENSE-CODIGO).

Reuso e adaptação são bem-vindos. Para sugerir correções ou melhorias, abra uma *issue* ou
um *pull request*.
