from bs4 import BeautifulSoup
import requests

# This module scraw antonyms of word from website https://www.thesaurus.com

SCRAW_URL = "https://www.thesaurus.com/browse/%s?s=t"
ANTONYM_NUMBER = 5
ENCODING = 'utf-8'

class AntonymsScrawler:
    def __init__(self, word):
        self.word = word

    def get_antonyms_of_word(self):
        try:
            _url = SCRAW_URL % self.word
            response = requests.get(_url)
            if response.status_code != 200:
                raise Exception("Scraw antonyms of word Unsuccessfully!")
            html_doc = response.content
            soup = BeautifulSoup(html_doc, 'html.parser')
            ul_tag = self.get_antonyms_ul_tag(soup)
            if ul_tag:
                antonyms_list = self.get_antonyms_list(ul_tag)
                return {"antonyms": ', '.join(antonyms_list)}
            else:
                return {"antonyms": ""}
        except Exception as e:
            return e

    def get_antonyms_ul_tag(self, soup):
        try:
            section_tag_list = soup.find_all('section')
            for section_tag in section_tag_list:
                p_tag = section_tag.find('p')
                if p_tag:
                    if "Antonyms for" in p_tag.get_text():
                        return section_tag.find('ul')
        except Exception as e:
            return e

    def get_antonyms_list(self, ul):
        try:
            antonyms_list = []
            li_tag_list = ul.find_all('li')
            antonyms_count = 1
            for li_tag in li_tag_list:
                if antonyms_count > ANTONYM_NUMBER:
                    break
                antonyms_list.append(li_tag.get_text())
                antonyms_count += 1
            return antonyms_list
        except Exception as e:
            return e

def main(word):
    _as = AntonymsScrawler(word)
    return _as.get_antonyms_of_word()
