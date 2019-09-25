#!/usr/bin/env bash
#
## tankmek // 02.08.18
## CCTC Linux Challenge
###################

function do_gz () {
  echo "Gzip extraction"
  mv $1 "$1".gz
  gzip -dq "$1".gz
}

function do_bz () {
  echo "Bzip extraction"
}

function do_b2 () {
  echo "Bz2 extraction"
  bzip2 -dq $1
}

function untar () {
  echo "Tar extraction"
  tar xf $1
  rm $1
}

function scrape () {
  for i in *
    do
      filetype=$(file $i)
      case $filetype in
        *bzip2*)
          do_b2 $i
          ;;
        *gzip*)
          do_gz $i
          ;;
        *tar*)
          untar $i
          ;;
        *)
          echo "END END END"
          cat $i
          exit 0
          ;;
      esac
    done
}

while :
  do
    scrape
done
