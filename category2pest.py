from category2pest_dic import Category2PestRule

class Category2Pest:
    def __init__(self):
        """
        関数`__init__`はクラスをインスタンス化した時に実行されます。
        """

    def category2pest(self, category):
        rule = Category2PestRule()
        pest_word = ""
        detail_word = ""
        for check in rule.chage_rule:
            for chek_tag in check[1]:
                if chek_tag in category:
                    pest_word = check[0]
        for detail in rule.detail_rule:
            for detail_tag in detail[1]:
                if detail_tag in category:
                    detail_word = detail[0]
        if pest_word:
            if detail_word:
                return "<" + pest_word + "・" + detail_word + ">"
            else:
                return "<" + pest_word + "・トピック>"
        else:
            if detail_word:
                return "<PEST不明-" + detail_word + ">"
            return ""

