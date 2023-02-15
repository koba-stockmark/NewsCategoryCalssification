import spacy
import sys

sys.path.append('../PredicateStructuring')

from sentence_category_check import SentenceCategoryCheker
from data_dump import DataDumpSave
from pas_analysis import PasAnalysis
from category2pest import Category2Pest


class SentenceCategoryGet:

    def __init__(self):
        """
        関数`__init__`はクラスをインスタンス化した時に実行されます。
        """

        self.nlp = spacy.load('ja_ginza_electra')  # Ginzaのロード　tranceferモデル
        pas_model = PasAnalysis()
        self.pas_analysis = pas_model.pas_analysis
        scc_model = SentenceCategoryCheker()
        self.sentence_category_check = scc_model.sentence_category_check
        d_d_s = DataDumpSave()
        self.data_dump_and_save = d_d_s.data_dump_and_save
        self.data_dump_and_save2 = d_d_s.data_dump_and_save2
        self.data_dump_and_save3 = d_d_s.data_dump_and_save3
        self.text_treace = d_d_s.text_treace
        c2p = Category2Pest()
        self.category2pest =c2p.category2pest

    """
    文を解析してカテゴリの取得
    """

    def category_get(self, text):

        debug = False  # デバッグ用フラグ
        ret = ''
        ##########################################################################################################################################
        # 形態素解析
        ##########################################################################################################################################
        doc = self.nlp(text)  # 文章を解析
        if debug:
            self.text_treace(*doc)
        ##########################################################################################################################################
        # 述語項構造解析
        ##########################################################################################################################################
        pas_result = self.pas_analysis(debug, text, *doc)
        argument = pas_result[0]["argument"]
        predicate = pas_result[0]["predicate"]
        # デバッグ表示用解析データ
        if debug:
            ret = ret + pas_result[1]
        # デバッグ表示用解析データ
        ##########################################################################################################################################
        #    主述部のカテゴリチェック
        ##########################################################################################################################################
        category = self.sentence_category_check(predicate, argument, *doc)
        pest = self.category2pest(category)
        category = category + "\t" + pest
        # デバッグ表示用解析データ
        if debug:
            ret = ret + self.data_dump_and_save2(text, argument, predicate)
            self.data_dump_and_save3(text, argument, predicate)
            print(category)
            return ret
        # デバッグ表示用解析データ
        return category
