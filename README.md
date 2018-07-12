ML2018第一次作業

請使用GUI.py，需要的庫有PIL中的Image,ImageTk以及numpy，請下載image以提供k1,k2  
通過decoder.py訓練得到 w = [0.24994724,0.66296781,0.09225696]  
decoder後面添加了random來訓練，alpha = 0.0000001 * random(1,300)，但是忘記上傳我也刪了原文件  
然後跑了1000次以後得到現在的數據，誤差的計算方式是用原圖每個像素點和解密出來的圖每個像素點計算差值再做2.5次方再做和，再取得最小誤差的w  
目前的結果如下圖,左側為原始圖片，右側為解密后。其他圖片請下載整個repository測試。
![image](https://github.com/BergLoo/ML2018_410421252_Image-Decryption-using-Linear-Percetpron/blob/master/image/I.png?raw=true)
![image](https://github.com/BergLoo/ML2018_410421252_Image-Decryption-using-Linear-Percetpron/blob/master/image/xd.png?raw=true)
