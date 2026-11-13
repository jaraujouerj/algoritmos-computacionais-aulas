# Compila todas as aulas:  make        (gera um PDF por aula)
# Compila uma aula:        make aula05_bases_da_programacao.pdf
# Limpa auxiliares:        make clean
TEX := $(wildcard aula*.tex) $(wildcard C*_*.tex)
PDF := $(TEX:.tex=.pdf)

all: $(PDF)

%.pdf: %.tex ac1.sty
	latexmk -pdf -interaction=nonstopmode -halt-on-error $< >/dev/null || (echo "ERRO em $<"; exit 1)

clean:
	latexmk -C >/dev/null 2>&1; rm -f *.nav *.snm *.vrb *.toc *.out *.aux *.log

.PHONY: all clean
