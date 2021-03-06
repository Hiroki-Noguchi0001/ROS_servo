# ROS_servo
## 2020 robot system homework 2

rosとpigpioを用いてサーボモータを動かします。

---
## 動作環境

### OS : ubuntu 20.04 server

### ROS : Noetic

---
## 使用したもの

・ [Raspberry Pi4 model B 4GB](https://akizukidenshi.com/catalog/g/gM-14778/)　× 1

・ [Futaba S3003 (サーボモータ)](https://www.rc.futaba.co.jp/servo_air/analog/s3003.html) × 1

   *Futaba S3003の[データシート](http://www.es.co.th/schemetic/pdf/et-servo-s3003.pdf)
   
・ [オスメスジャンパーピン](https://akizukidenshi.com/catalog/g/gC-08934/) × 3

---
## 回路図
![回路図](https://github.com/Hiroki-Noguchi0001/ROS_servo/blob/images/image1.png "回路図")

| servo motor | PIN 番号     |
|:------------|:-------------|
| 赤(Vcc)     | : 2 (5V)     |
| 黒(GND)     | : 39 (GND)   |
| 白(pulse)   | : 7 (GPIO 4) |

・Vccは5Vのピンであればどこでも問題ありません。

・GNDはGNDのピンであればどこでも問題ありません。

・GPIOに関してはこのパッケージではGPIO 4 のみ対応しております。

＊GPIOを変更したい場合はscript内にある[servo_motor.py](https://github.com/Hiroki-Noguchi0001/ROS_servo/blob/master/scripts/servo_motor.py)
の5行目のGPIO_PINの数字を変更することでGPIOを変更することができます。

---
## デモ動画

[![servo](https://github.com/Hiroki-Noguchi0001/ROS_servo/blob/images/image2.jpg)](https://www.youtube.com/watch?v=IvMhjApOxDI)

上の画像をクリックすると動画が再生されます

---
## インストール方法

### 本パッケージ

```sh
$ cd ~/catkin_ws/src
$ git clone https://github.com/Hiroki-Noguchi0001/ROS_servo.git
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc
```

### pigpio

[こちらのサイトを参考しました](http://abyz.me.uk/rpi/pigpio/download.html)

```sh
$ wget https://github.com/joan2937/pigpio/archive/master.zip
$ unzip master.zip
$ cd pigpio-master
$ make
$ sudo make install
```
unzipがインストールされていない場合は
```sh
$ sudo apt install unzip
```
でインストールしてください。

---
## 使用方法

上記の手順で本パッケージとpigpioをインストールした後

```sh
$ roscd servo
$ cd scripts
$ chmod +x pulse.py
$ chmod +x servo_motor.py
$ sudo pigpiod
$ roslaunch servo motor.launch
```
以上のコマンドを入力してください。

roslaunch servo motor.launchを実行後、サーボモータが約45°ずつ回転します。

回転角度の限界(初期位置から約180°)に到達すると初期位置に戻ります。

プログラムを終了する際は　ctrl + c で終了してください。

---
## ライセンス

### ROS : [BSD 3-Clause "New" or "Revised" License](https://github.com/Hiroki-Noguchi0001/ROS_servo/blob/master/LICENSE)

### pigpio : [The Unlicense](https://github.com/joan2937/pigpio/blob/master/UNLICENCE)
