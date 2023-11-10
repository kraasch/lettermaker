
SHELL=/bin/bash

run:
	make clean
	make create
	make view

create:
	lettermaker -t ./example/marie.toml -o marie
	lettermaker -t ./example/empty.toml -o empty
	lettermaker -t ./example/marie.toml

view:
	zathura ./marie.pdf & disown
	zathura ./empty.pdf & disown
	zathura ./output/letter.pdf & disown

clean:
	rm -f ./marie.pdf
	rm -f ./empty.pdf
	rm -rf ./output/

hub_update:
	@hub_ctrl ${HUB_MODE} ln "$(realpath ./src/lettermaker.py)" "${HOME}/.local/bin/lettermaker"
