#!usr/bin/env
# -*- coding: utf-8 -*-
"""
Jhonatan da Silva
Last Updated version :
Wed Apr 12 09:58:12 2017
Number of code lines: 
59
"""
import subprocess
from datetime import date
import pandas as pd
listOfVariables = ['pyData1','pyData2']
day = date.today().day
month = date.today().month
weekDay = date.today().weekday()
reportDay = str(day) + '/' + str(month)
weekMap = {0:'Segunda',1:'Terça',2:'Quarta',3:'Quinta',4:'Sexta',5:'Sábado',6:'Domingo'}

def main():
    color = '\\color{myred}'
    #init = weekMap[weekDay] + ' $\\rightarrow$ ' + reportDay  + ' $\\rightarrow$ '+color + 'Objetivos'
    #items = toDo()
    #writeLaTeX(Init(init),itemize(items))
    init = weekMap[weekDay] + ' $\\rightarrow$ ' + reportDay + ' $\\rightarrow$ ' +color+  ' Objetivos alcançados'
    items = did()
    writeLaTeX(Init(init),itemize(items))

def toDo():
    items = ['haha','hehe','hihi','hoho','huhu','haha','hehe']
    return items

def did():
    items = ['haha','hehe','hihi']
    return items

def Init(msg):
    init = ['\\centering','\\huge \\color{myblue2}' + msg + ' '\
            '\\color{black}',\
            '\\normalsize']
    return init

def itemize(*argv):
    begin = '\\begin{itemize}'
    end = '\\end{itemize}'
    item = []
    item.append(begin)
    item.extend(['\\item ' +str(content) for args in argv for content in args])
    item.append(end)
    return item

def writeLaTeX(*argv):

    with open('report.tex') as f:
        data = f.read().splitlines()

    with open('report.txt','w') as f:
        [f.write(d + '\n') for d in data[:-1]]
        [f.write(content + '\n') for args in argv for content in args]
        f.write(data[-1])
    
    fileName = 'report.tex'
    subprocess.call('mv report.txt ' +fileName,shell=True)
    subprocess.call('pdflatex '+ fileName,shell=True)

if __name__ == '__main__':
    main()

