all: thesis2.pdf

RUBBER := $(shell rubber --version 2>/dev/null)

thesis2.pdf: thesis2.tex chapters/*.tex references.bib
ifdef RUBBER
	@echo "Found rubber, using it"
	rubber --pdf $<
else
	pdflatex $<
	biber thesis2
	pdflatex $<
endif
