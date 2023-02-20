# PyMorse
PyMorse is module for using morse code in python.  
PyMorseはモールス信号をpythonで使うためのモジュールです。  
Use PyMorse,so Everybody can convert morse code to string,string to morse code for easy.  
PyMorseを使えば誰もが簡単にモールス信号を文字列へ、文字列をモールス信号へ変換することができます。
# DEMO & Usage
```Python  
import pymorse
# string to morse code
print(pymorse.string_to_code("Helloworld"))
# morse code to string
print(pymorse.code_to_string("...._._.-.._.-.._---_,_.--_---_.-._.-.._-.."))
```
# Requirement
None!
# Installation
```bash
$ pip install git+https://github.com/roistaff/PyMorse
```
# Note
 Morse code doesn't have a comma and space.   
 モールスコードにはコンマはありません。
# Author
 Roi Staff（スタッフ・ロイ）  
 Gmail:roistaff1983@gmail.com  
 if you found something wrongs please tell me.
# License
MIT
