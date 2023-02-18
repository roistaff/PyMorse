# PyMorse
PyMorse is module for using morse code in python.  
PyMorseはモールス信号をpythonで使うためのモジュールです。  
Use PyMorse,so Everybody can convert morse code to string,string to morse code for easy.  
PyMorseを使えば誰もが簡単にモールス信号を文字列へ、文字列をモールス信号へ変換することができます。
# DEMO & Usage
```Python  
import pymorse
# string to morse code
a = MORSE() #create new instance
print(a.string_to_code("hello world"))
# morse code to string
b = MORSE() #create new instance
print(b.code_to_sring("...._._.-.._.-.._---_,_.--_---_.-._.-.._-..")) # A comma means a space. 
```
# Requirement
None!
# Installation
```bash
$ pip install git+https://github.com/roistaff/PyMorse
```
# Note
  ","(comma) in a output:
 ```
 ...._._.-.._.-.._---_,_.--_---_.-._.-.._-..
 ```
 are means a space.  
 上のような出力の中のコンマは空白を意味します。  
 Morse code doesn't have a comma.   
 モールスコードにはコンマはありません。
# Author
 Roi Staff（スタッフ・ロイ）  
 Gmail:roistaff1983@gmail.com  
 if you found something wrongs please tell me.
# License
MIT
