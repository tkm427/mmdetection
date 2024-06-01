## mmdetectionの元レポジトリ
https://github.com/open-mmlab/mmdetection

## フォルダ構成
基本は元レポジトリのまま

追加分
- grape/ : ブドウの実をセグメンテーションするためのフォルダ. 
  - raw_data/ : 学習用の画像の元データ
  - data/ : 前処理後の画像データ
  - preprocess/ : 前処理用のファイル
  - MMDet_InstanceSeg_Tutorial.ipynb : demo/MMDet_InstanceSeg_Tutorial.ipynbを参考に、grapeのセグメンテーションを行うためのファイル

- fisheye_to_cubemap/ : 魚眼画像が関係する変換を行う

基本は元レポジトリのまま
  - rotate_fisheye.py : 魚眼画像の投影の中心を回転させるためのファイル

回転のために、下のパッケージに引数 rotate を追加して、変更

※ 横方向の回転しか実装できず、横方向の回転と90度回転を組み合わせることで、任意の角度の回転を実現

※ 回転後の画像の黒い部分は、正確な領域ではなく大雑把な領域

元レポジトリ
https://github.com/bhautikj/vrProjector/blob/master/vrProjectorWrapper.py

## Getting Started
### 1. docker/Dockerfileからコンテナを作る
```
docker build -t mmdetection .
```

```
docker run --name mmseg-container --gpus all --shm-size 8g -it mmdetection
```

参考：　https://bo-li.medium.com/how-to-use-mmsegmentation-docker-image-and-mount-local-drive-3c16fa048d15

### 2. 必要なパッケージをインストール
```
cd mmdetection
pip install -r requirements.txt
```

### 3. 学習用データのannotationを作成
```
cd grape/preprocess
sh annotation.sh [input_dir]
```
[input_dir]には、学習用の画像データが入っているディレクトリを指定する

例：sh annotation.sh /mmdetection-grape/grape/data/resize_blur5

### 4. annotationファイルを修正
color画像はJPG、label画像はpngであるため、annotationファイルを修正する

annotationファイルを開いてpngをJPGに変換

### 5. grape/MMDet_InstanceSeg_Tutorial.ipynbでモデルの学習を行う

### 6. 学習したモデルを使って、セグメンテーションを行う
