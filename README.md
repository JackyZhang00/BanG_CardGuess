# BanG_CardGuess

作者：7Seven00

# 基于opencv的图像匹配与BanG Dream!卡面局部识别

## 使用方法

### 安装必要的库

注意：本程序使用Python3.11测试，因此，请确保你的Python版本是合适的。

pip：请在工作目录下使用命令 `pip install -r requirements.txt`
conda: quick install `conda create env -f environment.yml`

### 保存卡面

**第一次使用时**，请运行`upload.bat`保存卡面至本地（目前共有2721张卡面）

### 使用方法

对于一般的卡面识别，可直接调用guess.py程序。其中需要将代码中的image_file中的路径修改为实际的图片路径。

为测试用，在工作目录下，我们提供了一个test.png文件，可用以测试程序是否正常运行

**注意：目前程序对于缩放后的图片识别效果不好，请在识别时尽量使用原图比例**