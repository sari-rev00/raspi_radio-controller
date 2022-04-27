## イントロダクション
raspberry piを使ったラジコン用pythonスクリプトです。<br>
raspberry piのGPIOをモータドライバに接続し、モータの動作で前進・後進・右左旋回を制御します。<br>
raspberry piで制御用のAPIを起動し、操作用端末（PC等）のキー入力でAPIを叩いてラジコンを制御します。<br>
<br>

## 名前の由来
動作の様子が節足動物のダンゴムシに似ているため。<br>
<br>

## 構成
- ラジコン本体：　raspberry pi、電子回路、モーター、ギアボックス、シャーシ、サーバプログラム
- コントローラ：　PC、クライアント（制御）プログラム
<br><br>

## 動作概要
- ラジコン本体の立ち上げ
    - モーター電源用電池の接続
    - raspberry pi用電源（5Vモバイルバッテリー）の接続　＊動作に必要な機能は自動起動します。
- クライアントの立ち上げ
    - PC立ち上げ
    - dangomushi_cntrol_crient.pyの起動
<br><br>

## 操作方法
クライアントのキーボードで操作を行います。<br>
キーを推している間だけ、下記動作を行います。<br>
| 動作 | 操作 |
| --- | --- |
| 前進 | ↑(上方向キー) |
| 後進 | ↓(下方向キー) |
| 右旋回 | →(右方向キー) |
| 左旋回 | ←(左方向キー) |
<br><br>

## セットアップ
TBD<br>
<br>

## ラジコン本体回路図
TBD<br>
<br>

## モジュールの説明
- client
    - 操作用端末用スクリプト
- dangomushi_server
    - ラジコン本体のraspberry piで使用するスクリプト
<br><br>

## System requirements (Dev environment)
- server
    - **OS:** raspbian buster
    - **Hardware** raspberry pi
    - **Python:** 3.7 (or latter)
- controller
    - **OS:** Win10 (or latter)
    - **Hardware** Intel CORE i5(8th gen)
    - **Python:** 3.7 (or latter)
<br><br>


## Misc
Copyright (c) 2022 SAri<br>
<br>


