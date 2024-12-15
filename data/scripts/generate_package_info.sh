#! /bin/bash

if [[ $1 == "version" ]]
then
	dnf info $2 2> /dev/null | grep Version | cut -d":" -f2 | sed -n 4p
elif [[ $1 == "description" ]]
then
	dnf info $2 2> /dev/null | sed -n '/Description/,/^$/p' | awk 'NR==1,/^$/ {if (/^$/ && printed) exit; if (NF) printed=1; if (NR==1) sub(/Description *: */, ""); else sub(/^ *: */, ""); print}'
fi
