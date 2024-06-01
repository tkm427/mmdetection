元レポジトリ
https://github.com/open-mmlab/mmdetection

## フォルダ構成


## Getting Started
1. docker/Dockerfileからコンテナを作る
```
docker build -t mmdetection .
```
```
docker run --name mmseg-container --gpus all --shm-size 8g -it mmdetection
```
参考：　https://bo-li.medium.com/how-to-use-mmsegmentation-docker-image-and-mount-local-drive-3c16fa048d15

2. 必要なパッケージをインストール
cd mmdetection
pip install requirements.txt -r
