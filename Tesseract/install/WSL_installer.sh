# 必要な開発ツールをインストール
# See. https://github.com/tesseract-ocr/tesseract/wiki/Compiling

sudo apt-get install g++ # or clang++ (presumably)
sudo apt-get install autoconf automake libtool
sudo apt-get install autoconf-archive
sudo apt-get install pkg-config
sudo apt-get install libpng-dev
sudo apt-get install libjpeg8-dev
sudo apt-get install libtiff5-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libicu-dev
sudo apt-get install libpango1.0-dev
sudo apt-get install libcairo2-dev

# Leptonicaをソースからコンパイル
# See. http://www.leptonica.org/source/README.html

wget http://www.leptonica.org/source/leptonica-1.74.4.tar.gz
tar xvfz leptonica-1.74.4.tar.gz
rm leptonica-1.74.4.tar.gz
cd leptonica-1.74.4/
./configure
make
sudo make install

# Tesseract LSTMをソースからコンパイル
# See. https://github.com/tesseract-ocr/tesseract/wiki/Compiling-%E2%80%93-GitInstallation

git clone https://github.com/tesseract-ocr/tesseract.git tesseract-ocr
cd tesseract-ocr
./autogen.sh
./configure
make
sudo make install
make training
sudo make training-install
sudo ldconfig

# 学習済み言語データをインストール
# 日本語の場合、jpnとjpn_vertの2つが必要

wget https://github.com/tesseract-ocr/tessdata_best/raw/master/eng.traineddata
wget https://github.com/tesseract-ocr/tessdata_best/raw/master/jpn.traineddata
wget https://github.com/tesseract-ocr/tessdata_best/raw/master/jpn_vert.traineddata
sudo mv *.traineddata /usr/local/share/tessdata/

# 日本語の言語データの33行目が不具合を起こすのでコメントアウトしたい.
# そのまま編集するとデータが壊れるので、編集可能なconfig部分のみを抽出して編集し、その後結合するという方法をとる.

sudo combine_tessdata -e /usr/local/share/tessdata/jpn.traineddata jpn.config
sudo emacs jpn.config # comment out line 33
sudo combine_tessdata -o /usr/local/share/tessdata/jpn.traineddata jpn.config
sudo combine_tessdata -e /usr/local/share/tessdata/jpn_vert.traineddata jpn_vert.config
sudo emacs jpn_vert.config # comment out line 33
sudo combine_tessdata -o /usr/local/share/tessdata/jpn_vert.traineddata jpn_vert.config

# 動作確認
tesseract test.png out --oem 1 -l jpn
