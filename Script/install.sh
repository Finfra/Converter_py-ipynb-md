#!/bin/bash

for i in p2j j2m m2p p2m m2j j2p md2ipynb ; do
    cp $i /usr/local/bin/
    chmod /usr/local/bin/$i
done

