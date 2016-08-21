__author__ = 'Sandeep Bharti'
import requests
from bs4 import BeautifulSoup

def spider(url):
    print("Enter the category(case insensitive): ")
    print("ex-games & entertainment -> games---entertainment")
    categ=input()
    categ=categ.lower()
    categ=list(categ)
    for i,v in enumerate(categ):
        if v==' ' or v=='&':
            categ.pop(i)
            categ.insert(i,'-')
    categ=''.join(categ)

    print(categ)
    src=requests.get(url)
    ptext=src.text
    sp=BeautifulSoup(ptext,"html.parser")
    for link in sp.findAll('a'):
        title=link.string
        title=str(title)
        title=title.lower()
        title=list(title)
        for i,v in enumerate(title):
           if v==' ' or v=='&':
                title.pop(i)
                title.insert(i,'-')
        title=''.join(title)
        print(title)
        if (categ+'-')==title:
            url1="http://www.awwwards.com/websites/"+categ
            spider1(url1)
        else:
            print("Invalid category")


def spider1(url):
    src=requests.get(url)
    ptext=src.text
    f=open("sites.txt","w")
    sp=BeautifulSoup(ptext,"html.parser")
    for link in sp.findAll('a'):
        href=link.get("href")
        nurl = "http://www.awwwards.com"+str(href)
        title=link.string
        title=str(title)
        title=title.lower()
        n="none"
        if title == n:
            f.write(nurl)
            f.write("\n")
    f.close()


def main():
    print("Want list of awarded or nominated sites?(1/2)")
    print("1.Awarded")
    print("2.Nominated")
    n=int(input())
    if n==1:
        url="http://www.awwwards.com/awards-of-the-day/"
        spider(url)
    else:
        url="http://www.awwwards.com/nominees/"
        spider(url)

main()
