
# lettermaker

Makes letters with pdflatex and python3.

## to-dos.

 - [ ] implement prefills (with option `-p, --prefill`) to prefill empty fields with defaults before the default files.
   - [ ] provide prefill for french_formal
   - [ ] provide prefill for french_informal
   - [ ] provide prefill for english_formal
   - [ ] provide prefill for english_informal
   - [ ] provide prefill for german_formal
   - [ ] provide prefill for german_informal
   - [ ] provide prefill for chinese_formal
   - [ ] provide prefill for chinese_informal
 - [ ] look for prefills at ~/.config/lettermaker/prefills/ then at $PROJECT_ROOT/prefills
 - [ ] look for defaults at ~/.config/lettermaker/defaults/ then at $PROJECT_ROOT/defaults
 - [ ] implement list function (with option `-l, --list`) to show all prefill and default options.
 - [ ] implement setup function (with option `-s, --setup`) for ~/.config/lettermaker/prefills/
 - [ ] implement setup function (with option `-s, --setup`) for ~/.config/lettermaker/templates/
 - [ ] allow TOML arrays and create a PDF output letter for each permutation.
 - [ ] have flag to toggle visibility of page numbers (define in meta section of toml file).
 - [ ] have flag to toggle visibility of folding guide lines at left margin (define in meta section of toml file).

### done 

 - [X] allow to store letter data in TOML file.
 - [X] ie. use this python package: https://docs.python.org/3/library/tomllib.html
