# 学習データのアノテーションを行うスクリプト
input_dir=/mmdetection/grape/data/resize
python preprocessing/Mask2polygon.py $input_dir/train/label/
python preprocessing/Mask2polygon.py $input_dir/val/label/