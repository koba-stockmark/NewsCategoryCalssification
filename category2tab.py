from category2tab_dic import Category2TabRule

class Category2Tab:
    def __init__(self):
        """
        関数`__init__`はクラスをインスタンス化した時に実行されます。
        """

    def category2tab(self, category):
        rule = Category2TabRule()
        tab_word = ""
        detail_word = ""
        for check in rule.chage_rule:
            for chek_tag in check[1]:
                if chek_tag in category:
                    tab_word = check[0]
            if tab_word:
                break
        for detail in rule.detail_rule:
            for detail_tag in detail[1]:
                if detail_tag in category:
                    detail_word = detail[0]
            if detail_word:
                break
        if tab_word:
            if tab_word == "技術":
                if detail_word == "オピニオン":
                    tab_word = "技術コラム"
#                elif detail_word == "レポート":
#                    tab_word = "技術レポート"
                else:
                    tab_word = "技術トピック"
            return "<" + tab_word + ">"
        else:
            if detail_word:
                return "<tab不明-" + detail_word + ">"
            return ""

