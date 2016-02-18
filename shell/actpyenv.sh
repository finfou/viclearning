#!/bin/bash

usage() {
	echo "Usage: activate virtualenv"
	echo "$ [list]|<env name>";
	echo "	list: list exists environment can be activated"
	echo "	<env name>: name of environment to be activate"
}

list() {
	ls ~/pyenvs/
}

[ $# -eq 1 ] || {
	usage;
	exit 0;
}

[ "$1" == "list" ] && {
	list
}

[ -d ~/pyenvs/$1 ] && {
	path_to_exec="$HOME/pyenvs/$1/bin/activate"
	echo $path_to_exec
}
