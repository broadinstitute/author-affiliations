# author-affiliations
A Python script to number and format affiliations in an author list, given a list of authors and their affiliations.

## Running
This works by running
```bash
python affiliate.py [authors] [affiliations] [output]
```
where:
* `[authors]` is a path to a file giving an ordered list of authors and shorthands for their affiliations
* `[affiliations]` is a path to a file giving the full names of each affiliation shorthand
* `[output]` is a path to a file to which to write the author list and affiliations in HTML

The output is formatted in HTML to display superscripts (without Unicode) and easily allow copy+pasting into a document.

It also supports the option `--out-latex` to produce the same output in LaTeX.

## Example
[examples/authors.txt](./examples/authors.txt) is an example of the `[authors]` input and [examples/affiliations.txt](./examples/affiliations.txt) is an example of the `[affiliations]` input.
[examples/output.html](./examples/output.html) is the output of this example, and [examples/output.tex](./examples/output.tex) is the output in LaTeX.
It was produced by running
```bash
python affiliate.py examples/authors.txt examples/affiliations.txt examples/output.html --out-latex examples/output.tex
```
GitHub won't render the HTML, but you can download it and open it in a browser.
