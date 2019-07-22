from googletrans.gtoken import TokenAcquirer
import requests


SCRAW_URL = 'https://translate.google.com/translate_a/single?client=webapp&sl' \
            '=auto&tl=vi&hl=vi&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=' \
            'rm&dt=ss&dt=t&source=bh&ssel=0&tsel=0&kc=1&tk=%s&q=%s'
TAB_FOR_ERASE = ['<b>', '</b>']
ENCODING = 'utf-8'
SYNONYMS_NUMS = 5
EXAMPLES_NUMS = 3


def erase_tab(sentence):
    for tab in TAB_FOR_ERASE:
        sentence = sentence.replace(tab, '')
    return sentence

class GoogleScrawler:
    def __init__(self, word):
        self.word = word
        self.acquirer = TokenAcquirer()

    def get_info_of_word(self):
        # This function return a dict contaning information of word (raw word, word type,
        # meaning, example of word)
        # E.x: {"raw_word": "dog",
        #       "word_type": "noun",
        #       "word_meaning": "con cho",
        #       "examples": "I have a pretty dog"}
        try:
            word_info = {}
            tk = self.acquirer.do(self.word)
            _url = SCRAW_URL % (tk, self.word)

            response = requests.get(_url)
            if response.status_code != 200:
                raise Exception("Scrawl translation from Google translate unsuccessfully!")
            raw_info = response.json()
            word_info['word'] = self.word
            word_info['word_type'] = self.get_word_type(raw_info)
            word_info['meaning'] = self.get_meaning_of_word(raw_info)
            word_info['pronounce'] = self.get_pronounce_of_word(raw_info)
            word_info['synonyms'] = self.get_synonyms_of_word(raw_info)
            word_info['examples'] = self.get_examples_of_word(raw_info)
            return word_info
        except Exception as e:
            return e

    def get_word_type(self, raw_info):
        # This function return type of word: noun(n), verb(v), adj, adv...
        # Return type: str
        try:
            word_type_list = raw_info[1]
            word_types = []
            for i in word_type_list:
                word_types.append(i[0])
            return ', '.join(word_types)
        except Exception as e:
            return e

    def get_meaning_of_word(self, raw_info):
        # This function return meanings of word
        # E.x: "con cho(danh tu), di theo(dong tu)"
        # Return type: str
        try:
            word_type_list = raw_info[1]
            word_meanings = []
            for i in word_type_list:
                word_meanings.append(i[1][0] + "(" + i[0] + ")")
            return ', '.join(word_meanings)
        except Exception as e:
            return e

    def get_pronounce_of_word(self, raw_info):
        try:
            return raw_info[0][1][-1]
        except Exception as e:
            return e

    def get_synonyms_of_word(self, raw_info):
        try:
            synonyms_list = raw_info[11]
            word_synonyms = []
            for i in synonyms_list:
                synonyms = []
                synonums_count = 1
                for k in i[1][0][0]:
                    if synonums_count > SYNONYMS_NUMS:
                        break
                    synonyms.append(k)
                    synonums_count += 1
                synonyms = ', '.join(synonyms)
                synonyms = "%s(%s)" % (i[0], synonyms)
                word_synonyms.append(synonyms)
            return ', '.join(word_synonyms)
        except Exception as e:
            return e

    def get_examples_of_word(self, raw_info):
        try:
            ex_list = raw_info[13]
            word_examples = []
            ex_count = 1
            for ex in ex_list[0]:
                if ex_count > EXAMPLES_NUMS:
                    break
                word_examples.append(erase_tab(ex[0]))
                ex_count += 1
            return ', '.join(word_examples)
        except Exception as e:
            return e

def main(word):
    gs = GoogleScrawler(word)
    return gs.get_info_of_word()