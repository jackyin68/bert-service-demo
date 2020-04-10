pip install bert-serving-server  # server
pip install bert-serving-client  # client, independent of `bert-serving-server`
bert-serving-start -model_dir /tmp/english_L-12_H-768_A-12/ -num_worker=1

python ../example/example3.py
python ../example/example8.py