#!/usr/bin/env bash

mkdir out
mkdir err
rm out/*
rm err/*

bsub -W 60 -n 1 -o ./out/out.%J -e ./err/err.%J /share/jchen37/hpc_env/miniconda/bin/python2.7 jmoo_interface.py -repeats 1