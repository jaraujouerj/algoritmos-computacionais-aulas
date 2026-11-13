# Slides de Algoritmos Computacionais I (UERJ)

Um arquivo `.tex` (Beamer) por aula. O estilo visual (logo, nome no rodapé, cores) está em
`ac1.sty`, derivado de `../template_aula.tex`. Os PDFs não são versionados: gere com `make`
ou baixe na página de slides do site. O logo é opcional (veja o `README.md` da raiz).

## Compilar

```bash
make                                   # todas as aulas
make aula05_bases_da_programacao.pdf   # uma aula
make clean                             # remove PDFs e auxiliares
```

Requer `pdflatex` e `latexmk`. Os caminhos do logo (`../imagens/`) e das figuras (`figuras/`)
são relativos a esta pasta. As figuras das aulas 27 a 29 são geradas por
`figuras/gera_figuras.py` (precisa de numpy, pandas e matplotlib).

## Nova aula a partir do estilo

```latex
\documentclass[aspectratio=169,11pt,t]{beamer}
\usepackage{ac1}
\aulainfo{NN}{Título}{Subtítulo}
\begin{document}
\capa
% ... slides ...
\exercicios{CAP}{lista de exercícios do site}   % frame de exercícios
\resumo{\item ...}                               % frame de resumo
\end{document}
```

Frames com `lstlisting` precisam de `[fragile]`.

## Aulas

| Aula | Arquivo | Conteúdo (livro) |
|---|---|---|
| 01 | `aula01_apresentacao` | Apresentação, algoritmo (Prefácio) |
| 02 | `aula02_representacao_informacao` | Cap. 1 (1.1-1.7) |
| 03 | `aula03_arquitetura_execucao` | Cap. 1 (1.8-1.12), Cap. 2.1 |
| 04 | `aula04_pensamento_algoritmico` | Cap. 2 (2.2-2.5) |
| 05 | `aula05_bases_da_programacao` | Cap. 2 (2.6-2.9) |
| 06 | `aula06_estrutura_basica` | Cap. 3.1.1 |
| 07 | `aula07_estruturas_decisao` | Cap. 3 (3.1-3.4) |
| 08 | `aula08_iteracao` | Cap. 3 (3.5-3.6) |
| 09 | `aula09_laboratorio_problemas` | Cap. 3 (3.4), laboratório |
| 10 | `aula10_subalgoritmos` | Cap. 4 (4.1-4.3) |
| 11 | `aula11_parametros_escopo` | Cap. 4 (4.4-4.6) |
| 12 | `aula12_modulos` | Cap. 4.2 e 4.6 |
| 13 | `aula13_modulos_excecoes` | Cap. 4 (4.2, 4.7) |
| 14 | `aula14_revisao_cap1a4` | Revisão para a Prova 1 |
| 15 | (prova, sem slides) | |
| 16 | `aula16_sequencias_listas` | Cap. 5 (5.1-5.2) |
| 17 | `aula17_processamento_listas` | Cap. 5 (5.3-5.6) |
| 18 | `aula18_operacoes_listas` | Cap. 5 (5.7-5.9) |
| 19 | `aula19_matrizes` | Cap. 5 (5.10-5.11) |
| 20 | `aula20_dicionarios_tuplas` | Cap. 5 (5.12-5.13) |
| 21 | `aula21_numpy` | Cap. 5.14 |
| 22 | `aula22_strings` | Cap. 6 (6.1-6.3) |
| 23 | `aula23_arquivos` | Cap. 6 (6.4-6.5), CSV |
| 24 | `aula24_revisao_estilo` | Revisão para a Prova 2, Cap. 9 |
| 25 | (prova, sem slides) | |
| 26 | `aula26_lancamento_projeto` | Lançamento do projeto |
| 27 | `aula27_matplotlib` | Matplotlib (notebook) |
| 28 | `aula28_pandas_1` | Pandas I (notebook) |
| 29 | `aula29_pandas_2` | Pandas II (notebook) |
| 30 | `aula30_especificacao` | Especificação |
| 31 | `aula31_implementacao_1` | Implementação 1 |
| 32 | `aula32_implementacao_2` | Implementação 2 |
| 33 | `aula33_refatoracao_testes` | Refatoração e testes |
| 34-35 | `aula34_35_apresentacao` | Apresentação |
| C1 | `C1_recursao` | Cap. 7, **só Eng. de Computação** |
| C2 | `C2_ordenacao` | Cap. 8, **só Eng. de Computação** |

Os exercícios citados (ex.: 5.17, 7.4) são os do site
<https://www.araujo.eng.uerj.br/livro/exercicios/>.
