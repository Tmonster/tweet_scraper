thepwd=`pwd`
cd ~/torch/torch-rnn/
th train.lua -max_epochs 1 -input_h5 $thepwd/nn-data/${1}.h5 -input_json $thepwd/nn-data/${1}.json -gpu -1
cd $thepwd
