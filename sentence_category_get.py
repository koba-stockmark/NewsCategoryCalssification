import spacy

from sentence_category_check import SentenceCategoryCheker
from data_dump import DataDumpSave
from pas_analysis import PasAnalysis


class SentenceCategoryGet:

    def __init__(self):
        """
        関数`__init__`はクラスをインスタンス化した時に実行されます。
        """

        self.nlp = spacy.load('ja_ginza_electra')  # Ginzaのロード　tranceferモデル
#        self.nlp = spacy.load('ja_ginza')  # Ginzaのロード
        pas_model = PasAnalysis()
        self.pas_analysis = pas_model.pas_analysis
        scc_model = SentenceCategoryCheker()
        self.sentence_category_check = scc_model.sentence_category_check
        d_d_s = DataDumpSave()
        self.data_dump_and_save = d_d_s.data_dump_and_save
        self.data_dump_and_save2 = d_d_s.data_dump_and_save2
        self.data_dump_and_save3 = d_d_s.data_dump_and_save3
        self.text_treace = d_d_s.text_treace

        self.debug = False  # デバッグ用フラグ

    """
    文を解析してカテゴリの取得
    """

    def category_get(self, text):

        ret = ''
        ##########################################################################################################################################
        # 形態素解析
        ##########################################################################################################################################
        doc = self.nlp(text)  # 文章を解析
        if self.debug:
            self.text_treace(*doc)
        ##########################################################################################################################################
        # 述語項構造解析
        ##########################################################################################################################################
        pas_result = self.pas_analysis(self.debug, text, *doc)
        argument = pas_result[0]["argument"]
        predicate = pas_result[0]["predicate"]
        # デバッグ表示用解析データ
        ##########################################################################################################################################
        #    主述部のカテゴリチェック
        ##########################################################################################################################################
        category = self.sentence_category_check(predicate, argument, *doc)
        # デバッグ表示用解析データ
        if self.debug:
            self.data_dump_and_save3(text, argument, predicate)
            ret = ret + self.data_dump_and_save2(text, argument, predicate)
            return category, ret
        # デバッグ表示用解析データ
        return category, ""
