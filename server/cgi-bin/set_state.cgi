#!/bin/bash
DBDIR=/dev/shm/hademo1
OTHER_SERVER=192.168.0.232

[ -d $DBDIR ] || mkdir -p $DBDIR

echo -ne "Content-type: text/plain\r\n\r\n"

P1="${QUERY_STRING%%&*}"
P2="${QUERY_STRING##*&}"

GROUP="${P1%%=*}"
VALUE="${P1##*=}"

case "$GROUP" in
	belt|vertical|horizontal)

	;;
	*)
		echo ERROR
		exit 0
	;;
esac

T=`mktemp -p $DBDIR` || exit 1
echo "$VALUE" > $T
mv -f $T $DBDIR/$GROUP
echo OK

if [[ "x$P2" != "xnopropagate" ]]; then
	curl -s --max-time 0.5 --fail "http://${OTHER_SERVER}/cgi-bin/set_state.cgi?${QUERY_STRING}&nopropagate" 
fi
