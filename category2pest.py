
class Category2Pest:

    chage_rule = [
        ["経済",
            ["市場動向", "業界情報", "情報公開", "市場データ", "業績", "支援", "投資", "資金", "生産活動", "営業活動",
            "受注", "価格", "価格変更", "株式概況", "提携", "海外展開", "経済", "買収", "契約"]],
        ["政治",
             ["議案", "会議", "対談", "政府", "要請", "税金"]],
        ["技術",
             ["技術動向", "技術開発", "研究", "実験", "調査", "特許", "サービス", "商品化", "技術背景", "採用", "効果"]],
        ["社会",
             ["社会統計", "社会情勢", "社会問題", "法廷", "表彰"]]
    ]

    detail_rule = [
        ["オピニオン",
            ["コラム", "意見", "見解", "提案"]],
        ["トピック",
            ["説明", "紹介"]],
        ["レポート",
             ["レポート"]],
        ["予測",
             ["予測"]],
        ["目標",
            ["戦略", "施策", "方針", "目標", "行動変化", "対策"]],
        ["リスク／チャンス",
             ["障害", "問題"]],
        ["組織",
            ["人事", "組織", "設立", "組織変更"]],
        ["イベント",
             ["イベント", "セミナー"]]
    ]
    def category2pest(self, category):
        pest_word = ""
        detail_word = ""
        for check in self.chage_rule:
            for chek_tag in check[1]:
                if chek_tag in category:
                    pest_word = check[0]
        for detail in self.detail_rule:
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

