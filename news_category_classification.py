from sentence_category_get import SentenceCategoryGet
from  category_rule_dic import CategoryRule

class CategoryClassification:

    ##########################################################################################################################################
    #    ニュースのカテゴリ判別
    ##########################################################################################################################################

    def __init__(self):

        s_c_g = SentenceCategoryGet()
        self.category_get = s_c_g.category_get

    ######################################################
    #  タイトル最後のカッコ書きを削除する
    ######################################################
    def title_punct_cut(self, text):
        if text.endswith("」"):
            return text[:text.rfind("「")]
        if text.endswith("）"):
            return text[:text.rfind("（")]
        if text.endswith(")"):
            return text[:text.rfind("(")]
        if text.endswith("】"):
            return text[:text.rfind("【")]
        if text.endswith("』"):
            return text[:text.rfind("『")]
        if text.endswith("]"):
            return text[:text.rfind("[")]
        if text.endswith("］"):
            return text[:text.rfind("[")]
        if text.endswith("〉"):
            return text[:text.rfind("〈")]
        if text.endswith("》"):
            return text[:text.rfind("《")]
        if text.endswith("＞"):
            return text[:text.rfind("＜")]
        return text


    ######################################################
    #  タイトル中のスペースを「。」に置き換える
    ######################################################
    change_word = ["＝", "―", "-", "－", "：", "｜", "…", ":", "─", "～", "|", "〜", "│", "／"]
    
    def title_change(self, text):
        ret = ""
        ct = 0
        if "<br>" in text:
            text = text.replace("<br>", "。")
        for ch in text:
            if ch in self.change_word:      # 置き換え文字
                ret = ret + "。"
            elif (ch == " " or ch == "　"):  # スペースの処理
                if ct > 0 and ct < len(text) - 1 and (not text[ct - 1].isascii() or not text[ct + 1].isascii()):
                  ret = ret + "。"
                else:
                  ret = ret + ch
            elif ch == "【" and not text.endswith("】"):  # ？を正しく解析させるための処理
                  ret = ret + "。" + ch
            elif ch == "？" or ch == "?" or ((ch == "】" or ch == "【") and not text.endswith("】")):   # ？を正しく解析させるための処理
                ret = ret + ch + "。。"
            elif ch == "、" and (text[ct - 1] == "へ" or (text[ct - 1] == "か" and (text[ct - 2] != "ほ" and text[ct - 2] != "へ"))):     # 「...〇〇へ、〇〇...」　という形の特殊タイトル処理
                ret = ret + "。"
            elif len(text) > ct + 2 and ch == "そ" and text[ct + 1] == "の" and (text[ct + 2].isdigit() or (text[ct + 2] >= "０" and text[ct + 2] <= "９")):  # その２
                ret = ret + "。" + ch
            else:
                ret = ret + ch
            ct = ct + 1
        if not ret.endswith("。"):       # 文末に句点の追加
            ret = ret + "。"
        return ret

    ##########################################################################################################################################
    # タイトルからカテゴリが判断できたかのチェック
    ##########################################################################################################################################
    def category_is_ok(self, category):
        for chek in category.split(","):
            if chek in CategoryRule.top_category:
                return True
        return False

    ##########################################################################################################################################
    # ニュースのカテゴリのチェック
    ##########################################################################################################################################

    def news_category_classification(self, title, text):
        ret = ""
        debug_dump = ""
        if title:
            l_ct = 0
            for line in title.splitlines():
#            if "。" not in line and (" " in line or "　" in line):
                line = self.title_punct_cut(line)
                line = self.title_change(line)
                l_ct = l_ct + 1
                ret_p = self.category_get(line)
                debug_dump = debug_dump + ret_p[1]
                if ret_p:
                    ret = ret + ret_p[0]
                if l_ct > 5:  # 5文以内に何もカテゴリがない場合は　その他
                    if not ret:
                        ret = "<その他>"
                    break
        if self.category_is_ok(ret):
            return ret, "", debug_dump
        t_ret = ret
        if text:
            l_ct = 0
            for lines in text.splitlines():
                if lines:
                    for line in lines.split("。"):
                        l_ct = l_ct + 1
                        ret_p = self.category_get(line + "。")
                        debug_dump = debug_dump + ret_p[1]
                        if ret_p[0]:
                            for add in ret_p[0].split(","):
                                if add not in ret:
                                    if ret:
                                        ret = ret + "," + add
                                    else:
                                        ret = add
                        if l_ct > 5:  # 5文以内に何もカテゴリがない場合は　その他
                            if ret:
                                return ret, t_ret, debug_dump
                            else:
                                return "<その他>", t_ret, debug_dump
        return ret, t_ret, debug_dump

