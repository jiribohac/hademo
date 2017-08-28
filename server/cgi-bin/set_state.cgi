#!/bin/bash
DBDIR=/dev/shm/hademo1
[ -d $DBDIR ] || mkdir -p $DBDIR
echo -ne "Content-type: text/plain\r\n\r\n"

GROUP="${QUERY_STRING%%=*}"
VALUE="${QUERY_STRING##*=}"

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
mv $T $DBDIR/$GROUP

