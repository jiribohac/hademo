#!/bin/bash
echo -ne "Content-type: text/plain\r\n\r\n"

if [[ "x${QUERY_STRING}" == "x1" ]]; then
        echo OK 1 0 1
else
        echo ERROR
fi

