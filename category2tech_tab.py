from category2tech_tab_dic import Category2TechTabRule

class Category2TechTab:
    def __init__(self):
        """
        関数`__init__`はクラスをインスタンス化した時に実行されます。
        """

    def category2tab(self, category):
        rule = Category2TechTabRule()
        tab_word = ""
        detail_word = ""
        for check in rule.chage_rule:
            for chek_tag in check[1]:
                if chek_tag in category:
                    if tab_word:
                        if check[0] not in tab_word:
                            tab_word = tab_word + ",<" + check[0] + ">"
                    else:
                        tab_word = "<" + check[0] + ">"
        if tab_word:
            for detail in rule.detail_rule:
                for detail_tag in detail[1]:
                    if detail_tag in category:
                        if detail_word:
                            if detail[0] not in detail_word:
                                detail_word = detail_word + ",<" + detail[0] + ">"
                        else:
                            detail_word = "<" + detail[0] + ">"
            if detail_word:
                return tab_word + "," + detail_word
            else:
                return tab_word
        else:
            return ""

