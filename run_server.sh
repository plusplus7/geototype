rm -rf release
cp -r src release
cd release

export PYTHONPATH=$PYTHONPATH:data
python main.py
