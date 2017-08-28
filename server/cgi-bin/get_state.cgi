#!/bin/bash
DBDIR=/dev/shm/hademo1
declare -A LIFETIME
LIFETIME[horizontal]=4
LIFETIME[vertical]=3
LIFETIME[belt]=10

declare -A NOOP
NOOP[horizontal]=noh
NOOP[vertical]=nov
NOOP[belt]=nobelt


echo -ne "Content-type: text/plain\r\n\r\n"

RESPONSE="OK "
for i in belt vertical horizontal; do 
	F="$DBDIR/$i"
	if ! [[ -e "$F" ]]; then
		RESPONSE="$RESPONSE ${NOOP[$i]}"
		continue
	fi
	MTIME=`stat --printf="%Y" "$F"`
	NOW=`date "+%s"`
	if [[ $NOW -gt $(($MTIME + ${LIFETIME[$i]})) ]]; then
		RESPONSE="$RESPONSE ${NOOP[$i]} "
		continue
	fi

	read VAL < $F
	RESPONSE="$RESPONSE $VAL "
done

echo $RESPONSE
