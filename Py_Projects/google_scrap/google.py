import requests
from bs4 import BeautifulSoup
import time
import csv

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

for i in range(1, 6):
    url = "https://www.google.com/search?q=%EC%A0%9C%EC%98%AC%EB%9D%BC%EC%9D%B4%ED%8A%B8&rlz=1C1CHZN_koKR971KR971&ei=olgPY53GO8jk4-EP9sOpQA&start={}0&sa=N&ved=2ahUKEwidn_PRjvH5AhVI8jgGHfZhCggQ8tMDegQIAhA_&biw=1366&bih=625&dpr=1".format(i-1)
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    scraped = soup.find_all("div", attrs = {"class" : "yuRUbf"})
    for scrap in scraped:
        title = scrap.h3.get_text()
        link = scrap.a["href"]
        curr_time = time.strftime("_%Y%m%d_%H%M%S")
        name = "D:\지웅현서\윈도코딩\coding_file\python\Py_Projects\google_scrap\file\scrap{}.txt".format(curr_time)
        with open(name, "a", encoding = 'utf-8') as f:
            f.write("\n제목 : " + title + "\n링크 : " + link + "\n")
print("작업이 완료되었습니다")