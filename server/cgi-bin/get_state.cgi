#!/bin/bash
declare -A LIFETIME
LIFETIME[horizontal]=6
LIFETIME[vertical]=6
LIFETIME[belt]=60

declare -A NOOP
NOOP[horizontal]=noh
NOOP[vertical]=nov
NOOP[belt]=nobelt

#move to a service!
wiringPi-gpio mode 8 output
wiringPi-gpio mode 9 output


echo -ne "Content-type: text/plain\r\n\r\n"


LED=false
if [[ "x$QUERY_STRING" == "x1" ]]; then
	LED="wiringPi-gpio write 9 "
	DBDIR=/dev/shm/hademo1
elif [[ "x$QUERY_STRING" == "x2" ]]; then
	LED="wiringPi-gpio write 8 "
	DBDIR=/dev/shm/hademo2
elif [[ "x$QUERY_STRING" == "xweb1" ]]; then
	DBDIR=/dev/shm/hademo1
elif [[ "x$QUERY_STRING" == "xweb2" ]]; then
	DBDIR=/dev/shm/hademo2
fi


$LED 1

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

$LED 0
