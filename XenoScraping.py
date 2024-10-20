import requests
from bs4 import BeautifulSoup

# 引数：url 返り値：soupオブジェクト
def url2soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
    
# Xeno cantの種固有ID記事の合計ページ（音声データ数によりページ数が増加）
# 引数：soupオブジェクト 返り値：ページ数
def soup2page_num(soup):
    page_links = soup.select('nav.results-pages ul li a')
    max_page_number = 1
    
    for link in page_links:
        page_number = link.get_text()
        if page_number.isdigit():  # 数字かどうかを確認
            max_page_number = max(max_page_number, int(page_number))
    return max_page_number

# Xeno cantの種固有ID記事に含まれる音声ファイル固有のID
# 引数：soupオブジェクト 返り値：音声ファイルIDリスト
def sound_ids(soup):
    fancybox_a_tags = soup.find_all('a', class_='fancybox', rel='sono')
    sound_ids = [title["title"].split(":")[0] for title in fancybox_a_tags]
    return sound_ids

