#!/bin/bash
# comply info collect
# een script om te checken tot hoe ver een groepje zich houd aan de voorgeschreven richtlijnen voor automatische tests
# dit script checked vanuit hoe de staat van de repo nu is:
# voor iedere assignment
# * of de map bestaat
#   * of er een Makefile in de map zit
#     * of dat Makefile een run en build target heeft

# directory waar dit script staat
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

checklocatieN() {
	if [ $# = 0 ];then
		echo Je voert deze functie op de verkeerde manier uit. Deze functie heeft precies 1 argument nodig. Dit argument is hoeveelste assignment je wil gebruiken.
		exit
	fi
	n=${1}
	if test -d                "$SCRIPT_DIR/"*${n};then
		if test -f            "$SCRIPT_DIR/"*${n}/Makefile -o  -f "$SCRIPT_DIR/"*${n}/makefile;then
			if grep -q ^run   "$SCRIPT_DIR/"*${n}/[Mm]akefile;then
				echo -n ASS${n}RUNTARGET,
			fi
			if grep -q ^build "$SCRIPT_DIR/"*${n}/[Mm]akefile;then
				echo -n ASS${n}BUILDTARGET,
			fi
			echo -n ASS${n}MAKEFILE,
		else
			echo -n ASS${n}MAP,
		fi
	fi
}


checklocatieN 1
checklocatieN 2
checklocatieN 3
echo
