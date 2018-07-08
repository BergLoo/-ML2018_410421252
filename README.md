ML2018第一次作業

因爲第一次作業做錯了方向做成了加密，所以修改了一下encoder變成decoder  
w =[[0.25006898] [0.65998043][0.0901495 ]]   
每個像素點的誤差平均值 = 12.3   
左側是原圖，右側是訓練后生成的圖片  
有一些奇怪的像素點，感覺是因為alpha比較小在剛開始訓練的時候效果好但是到了後面W差不多接近的時候差值比較小所以需要alpha比較大才有比較明顯的W的改變。  
這個之後再改進。
![image](https://github.com/BergLoo/-ML2018_410421252/blob/master/image/I.png?raw=true)
![image](https://github.com/BergLoo/-ML2018_410421252/blob/master/image/I-NEW.png?raw=true)

基本的思路就是讀入四張圖片，然後用gradient descent去實作   
最後再測試一下實作的效果

誤差的測試： 
用產生的E′ 的每個像素減去E的再取絕對值，把所有像素的加起來再除以總量得到平均差值：  
每個像素點的誤差平均值 = 0.4787 

這是生成的E′ ，不過似乎github上不能用灰色階的png，這張是jpeg，png原檔在image中的E-g 

![image](https://github.com/BergLoo/-ML2018_410421252/blob/master/image/E-g.jpeg?raw=true)
![image](https://github.com/BergLoo/-ML2018_410421252/blob/master/image/E%20for%20display.jpeg?raw=true)
