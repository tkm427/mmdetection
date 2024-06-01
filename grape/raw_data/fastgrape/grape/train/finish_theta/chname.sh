#!/bin/sh
from=$1
to=$2
if [ ${from} = ${to} ]
then
  echo 'two arguments are the same.'
  exit 0
fi

for f in *
do
j=`echo ${f}|sed 's/'"${from}/${to}/g"`
if [ "${f}" != "${j}" ]
then
  echo "${f} -> ${j}"
  mv -- "${f}" "${j}"
fi
done
