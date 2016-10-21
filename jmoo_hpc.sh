#!/usr/bin/env bash

mkdir out
mkdir err
rm out/out.*
rm err/*

#for i in `seq 0 10`;
#do
#    bsub -W 60 -n 1 -o ./out/out.$i -e ./err/err.%J /share/jchen37/hpc_env/miniconda/bin/python2.7 jmoo_interface.py -repeats 1 -repeatOffset $i
#done


#dt=$(date '+%m%d_%H%M');
#bsub -W 60 -n 1 -o ./out/stats_$dt.%J -e ./err/err.%J /share/jchen37/hpc_env/miniconda/bin/python2.7 jmoo_interface.py -chartOnly

bsub -W 100 -n 1 -o ./out/stats_$dt.%J -e ./err/err.%J /share/jchen37/hpc_env/miniconda/bin/python2.7 jmoo_interface.py -new