FILENAME = resume

$(FILENAME).png: $(FILENAME).pdf
	convert -density 250 -flatten $<[0] -quality 100 $@

$(FILENAME).pdf: $(FILENAME).tex
	pdflatex $<

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.out
