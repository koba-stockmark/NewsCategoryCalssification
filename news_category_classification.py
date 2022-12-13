import spacy
import json
import copy
import sys

sys.path.append('../PredicateStructuring')

from chunker import ChunkExtractor
from data_dump import DataDumpSave
from sentence_category_get import SentenceCategoryGet

class CategoryClassification:

    debug = False

    ##########################################################################################################################################
    #    ニュースのカテゴリ判別
    ##########################################################################################################################################

    def __init__(self):

        self.nlp = spacy.load('ja_ginza_electra')  # Ginzaのロード　tranceferモデル
        chnker = ChunkExtractor()
        self.num_chunk = chnker.num_chunk
        d_s = DataDumpSave()
        self.text_treace = d_s.text_treace
        s_c_g = SentenceCategoryGet()
        self.category_get = s_c_g.category_get


    ##########################################################################################################################################
    # ニュースのカテゴリのチェック
    ##########################################################################################################################################

    def news_category_classification(self, text):
        l_ct = 0
        ret = ""
        for line in text.splitlines():
            l_ct = l_ct + 1
            ret_p = self.category_get(line)
            if ret_p:
                ret = ret + ret_p
            if l_ct > 5:     # 5文以内に何もカテゴリがない場合は　その他
                if ret:
                    return ret
                return "<その他>"
        return ret

