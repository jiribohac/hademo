#!/bin/bash
echo -ne "Content-type: text/plain\r\n\r\n"

case $HOSTNAME in
	server1)
		OTHER_SERVER=server2
		;;
	server2)
		OTHER_SERVER=server1
		;;
	*)
		echo "Wrong HOSTNAME"
		exit 1
esac

PN="${QUERY_STRING}"
P1="${PN%%&*}"
PN="${PN#*&}"

GROUP="${P1%%=*}"
VALUE="${P1##*=}"

P1="${PN%%&*}"
PN="${PN#*&}"
P2_NAME="${P1%%=*}"
P2_VALUE="${P1##*=}"

P1="${PN%%&*}"
PN="${PN#*&}"
P3_NAME="${P1%%=*}"
P3_VALUE="${P1##*=}"

CLIENT="$P2_VALUE"
if [[ "x$CLIENT" == "x1" ]]; then
	DBDIR=/dev/shm/hademo1
elif [[ "x$CLIENT" == "x2" ]]; then
	DBDIR=/dev/shm/hademo2
else
	exit 1
fi
[ -d $DBDIR ] || mkdir -p $DBDIR

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

if [[ "x$P3_NAME" != "xnopropagate" ]]; then
	curl -s --max-time 0.5 --fail "http://${OTHER_SERVER}/cgi-bin/set_state.cgi?${QUERY_STRING}&nopropagate" 
fi


