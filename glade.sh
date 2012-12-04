#!/bin/sh

# rootdir=`dirname $0`
rootdir=`pwd`

export GLADE_CATALOG_PATH=$rootdir/src/gui/glade
export GLADE_MODULE_PATH=$rootdir/src/gui/glade
# export PYTHONPATH=$rootdir/src/gui/glade

echo $GLADE_CATALOG_PATH
echo $GLADE_MODULE_PATH

glade-3 -v res/QuillConvert.xml
