# ros2_netspeed
![test](https://github.com/guangjitian755-cell/ros2_netspeed/actions/workflows/test.yml/badge.svg)   
ROS 2 上でネットワーク通信速度（Download / Upload）を計測し，トピックとして配信するためのパッケージです.  

## 詳細
このパッケージは、指定したネットワークインターフェースの送受信バイト数を一秒ごとに取得し，  
その差分から Download / Upload の通信速度（bytes/sec） を算出して publish します.    
計測処理は Python ノードで実装されており，psutil を用いてネットワークインターフェースの統計情報を取得します.   
受信側ノード（subscriber）は，取得した速度をログとして出力します.   

## 使用方法
```bash
$ git clone https://github.com/guangjitian755-cell/ros2_netspeed.git  
$ cd ros2_netspeed  
$ colcon build  
$ source install/setup.bash  
```  

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
- ROS2
- Python
- pusutil

## テスト環境
以下の環境で動作確認を行いました.   

### ローカル
- Ubuntu 22.04.5 LTS
- Python 3.10.12
- ROS2:Humble

### リモート(GitHub Actions)
- Ubuntu 22.04 (ubuntu-latest)  
-コンテナ: ryuichiueda/ubuntu22.04-ros2:latest
  -ベースOS:Ubuntu 22.04
  - ROS2:Humble

© 2025 Hikaru Yoshida
