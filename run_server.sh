rm -rf release
cp -r src release
cd release

python main.py $@
