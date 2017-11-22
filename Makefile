all: thesis2.pdf

thesis2.pdf: thesis2.tex chapters/*.tex references.bib
	pdflatex $<
	biber thesis2
	pdflatex $<
