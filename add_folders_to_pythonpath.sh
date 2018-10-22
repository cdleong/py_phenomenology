#!/bin/bash
# If you are using PyDev Eclipse, this isn't necessary. 
# But if you are using the CLI, you have to add the folders to your PYTHONPATH
# Or the imports don't work. 
#export PYTHONPATH=$PYTHONPATH:"`pwd`/pyphenom"
cd pyphenom && export PYTHONPATH=$PYTHONPATH:`pwd`
cd ../hw && export PYTHONPATH=$PYTHONPATH:`pwd`

