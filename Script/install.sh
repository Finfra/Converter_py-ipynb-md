#!/bin/bash
currentPath=$(pwd)
thePath=${BASH_SOURCE[0]}
sourceFile=$(pwd)/$thePath
sourcePath=`echo $(dirname $sourceFile)|sed "s/\/\.\//\//g"|sed "s/\/\.//g"`

# echo sourcePath=$sourcePath
# echo currentPath=$currentPath

cd $sourcePath
for i in p2j j2m m2p p2m m2j j2p md2ipynb j2mAll m2jAll; do
    echo copy $i to /usr/local/bin/$i
    sudo cp $i /usr/local/bin/
    sudo chmod +x /usr/local/bin/$i
done

cd $currentPath
