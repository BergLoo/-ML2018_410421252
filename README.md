ML2018第一次作業

基本的思路就是讀入四張圖片，然後用gradient descent去實作   
最後再測試一下實作的效果

雖然最後的結果基本上差不多了，不過還是有目前待優化的部分：   
1、沒有測試多個constant α，剛好隨便丟進去一個就成了  
2、沒有添加𝐸𝑝𝑜𝑐ℎ、MaxIterLimit、𝜖 這三個的部分  
3、沒有添加隨機生成w初始值的部分  


誤差的測試： 
用產生的E′ 的每個像素減去E的再取絕對值，把所有像素的加起來再除以總量得到平均差值：  
margin of error =  0.4787 

這是生成的E′ ，不過似乎github上不能用灰階的png，這張是jpeg，png原檔在image中的E-g   

![image](https://github.com/BergLoo/-ML2018_410421252/blob/master/image/E-g.jpeg?raw=true)

而這是原檔的E的jpeg檔，直觀上可以比較出十分相似  
![image](https://github.com/BergLoo/-ML2018_410421252/blob/master/image/E%20for%20display.jpeg?raw=true)
