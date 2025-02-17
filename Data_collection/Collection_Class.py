from bs4 import BeautifulSoup
import requests

class Collect:
    def __init__(self,base_url):
        self.base_url = base_url

    def get_ingredients(self, url):
        og_url = self.base_url + url
        resp1 = requests.get(og_url)
        soup1 = BeautifulSoup(resp1.text, "html.parser")
        tab = soup1.find_all('figcaption')
        str1 = ', '.join(i.text.strip() for i in tab)
        return str1

    def get_instructions(self,url):
        og_url1 = self.base_url + url
        resp = requests.get(og_url1)
        soup = BeautifulSoup(resp.text, "html.parser")
        a = soup.text.split()
        start_index = a.index('Instructions')
        end_index = a.index('Browse')
        result = a[start_index:end_index]
        result = " ".join(result)
        return result