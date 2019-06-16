# LessWord
## 简介
一个背单词查单词的软件，主要使用了爬虫、tkinter；后期打包使用的pyinstaller。
## 依赖
* python>=3.6
* os
* platform
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
* pyinstaller>=3.4
### 打包
```
python installer.py
```
打包好的程序放在项目根目录`dist`文件夹中，中间过程文件存放在`build`文件夹中

# 注
主应用程序必须和`img`目录位于同一目录下
## 你可能会遇到的问题
**若脚本或程序无法执行，请查看程序目录是否存在`start.lock`文件，如果存在，将它删除**



# 展示
![软件使用](https://user-images.githubusercontent.com/27119852/59552488-38bb5180-8fba-11e9-8dd0-8d8eb4d6d883.gif)



# version 1.2
## 添加控制器
新增c、t、r、l控制
### 如何控制
目前通过c、t、r、l可以实现已查询单词的重置
* 控制方法：
  `c` `t` `r` `l` `l` `l` `l` `l`
  * 速记：
    唱、跳、rap、篮球之后再打四次篮球
  
### 效果
![清空效果](https://user-images.githubusercontent.com/27119852/59561152-5c7ca700-904f-11e9-9922-2de120e5493f.gif)
