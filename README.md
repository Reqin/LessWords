# LessWord
## 简介
一个背单词查单词的软件实现，主要使用了爬虫、tkinter；后期打包使用的pyinstaller。
## 依赖
* python>=3.6
* os
* shutil
* time
* abc
* pikle
* tkinter
* urllib
* lxml
## 本地化
```
git clone https://github.com/Reqin/LessWord/
cd LessWord
python LessWords.py
```
## 打包为exe
### 依赖
* pyinstaller>3.4
### 打包
```
python installer.py
```
打包好的程序放在项目根目录`dist`文件夹中，中间过程文件存放在`build`文件夹中

# 注
主应用程序必须和`img`目录位于同一目录下
