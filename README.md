# ros2_netspeed
![test](https://github.com/guangjitian755-cell/ros2_netspeed/actions/workflows/test.yml/badge.svg)   
ROS 2 上でネットワーク通信速度（Download / Upload）を計測し，トピックとして配信するためのパッケージです.  

## 詳細
このパッケージは、指定したネットワークインターフェースの送受信バイト数を一秒ごとに取得し，  
その差分から Download，Upload の通信速度（Mbps） を算出して publish します.    
計測処理は Python oードで実装されており，psutil を用いてネットワークインターフェースの統計情報を取得します.   
受信側ノード（subscriber）は，取得した速度をログとして出力します.   

## ノード一覧
### measur1  
ダウンロード速度を計測しpublishするノード  
pustilライブラリを使用してos起動後からの累積の受信したデータのバイト数の値を取得し，現在の値から一秒前の値を引くことによってダウンロード速度を算出する．算出した値の単位をbpsからMbpsに変換してdownload_speedトピックにpublishする.  
### measur2
アップロード速度を計測しpublishするノード  
pustilライブラリを使用してos起動後からの累積の送信したデータのバイト数の値を取得し，現在の値から一秒前の値を引くことによってアップロード速度を算出する．算出した値の単位をbpsからMbpsに変換してupload_speedトピックにpublishする.  
### output
measur1とmeasur2で計測した値が出揃ったときにログに出力するノード  
download_speedトピックとupload_speedトピックから現在の値を読み取り，値を両方とも受信するとそれらを標準出力に表示する．

## トピック一覧
### download_speed
- 型: std_msgs/Float64  
- publish: measur1  
- subscribe: output.py  
- 概要: ダウンロード速度
### upload_speed
- 型: std_msgs/Float64
- publish: measur2  
- subscribe: output.py  
- 概要: アップロード速度 
## 実行例
```bash
$ ros2 launch ros2_netspeed netspeed.launch.py  
[output-3]           0.007            0.008  
[output-3]           0.073            0.077  
[output-3]          25.791            0.822  
[output-3]          47.151            1.204  
[output-3]          29.898            0.711  
```    
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．  
## 必要なソフトウェア
- ROS 2
- Python
- pusutil

## テスト環境
以下の環境で動作確認を行いました.   

### ローカル
- Ubuntu 22.04.5 LTS
- Python 3.10.12
- ROS 2:Humble

### リモート(GitHub Actions)
- Ubuntu 22.04 (ubuntu-latest)  
- コンテナ: ryuichiueda/ubuntu22.04-ros2:latest
  - ベースOS:Ubuntu 22.04
  - ROS 2:Humble

© 2025 Hikaru Yoshida
