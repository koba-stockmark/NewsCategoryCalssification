from chunker import ChunkExtractor
from sub_verb_dic import SubVerbDic
from category_rule_dic import CategoryRule

class SentenceCategoryCheker:

    def __init__(self):
        """
        関数`__init__`はクラスをインスタンス化した時に実行されます。
        """

    # 完全一致での辞書とのマッチング
    def rule_check(self, verb, rule):
        if verb in rule:
            return True
        return False

    # 後方一致での辞書とのマッチング
    def rule_check2(self, verb, rule):
        for check in rule:
            if check == verb[-len(check):]:
                return True
        return False

    def category_chek(self, start, end, sub_start, sub_end, obj_start, obj_end, pre_category, p_rule, *doc):
        if start == -1 or end == -1:
            return ""
        chunker = ChunkExtractor()
        s_v_dic = SubVerbDic()
        ret = ''
        new_end = end
        for c_pt in range(start, end):      # 述部の語幹だけを切り出す
            if doc[c_pt].pos_ == 'ADP' and ((doc[c_pt].lemma_ != 'を' and doc[c_pt].lemma_ != 'の' and doc[c_pt].lemma_ != 'が') or (doc[c_pt].lemma_ == 'を' and len(doc) > c_pt + 1 and doc[c_pt + 1].norm_ == '為る')):
                new_end = c_pt - 1
                break
        verb_word = chunker.compaound(start, new_end, *doc)
        obj_word = chunker.compaound(obj_start, obj_end, *doc)
        # O-V　ルール
        if obj_start >= 0:
            for rule in p_rule.phrase_rule:
                if "rule" in rule:
                    verb_ok = False
                    for check_verb in rule["rule"]["verb"]:
                        if check_verb and check_verb in verb_word:
                            verb_ok = True
                            break
                    if verb_ok:
                        for check_obj in rule["rule"]["obj"]:
                            if check_obj and check_obj in obj_word:
                                if ret:
                                    ret = ret + ',' + rule["label"]
                                else:
                                    ret = ret + rule["label"]
                                break
        if sub_start >= 0:
            sub_verb_word = chunker.compaound(sub_start, sub_end, *doc)
            for rule in p_rule.phrase_rule:
                if "rule" in rule:
                    verb_ok = False
                    for check_verb in rule["rule"]["verb"]:
                        if check_verb and check_verb in sub_verb_word:
                            verb_ok = True
                            break
                    if verb_ok:
                        for check_obj in rule["rule"]["obj"]:
                            if check_obj and check_obj in verb_word:
                                if ret:
                                    ret = ret + ',' + rule["label"]
                                else:
                                    ret = ret + rule["label"]
                                break

        # 補助表現以外のメイン術部
        if verb_word not in s_v_dic.sub_verb_dic or verb_word in s_v_dic.special_sub_verb_dic:
        # フルマッチ
            for rule in p_rule.phrase_rule:
                if "words" in rule:
                    if self.rule_check(verb_word, rule["words"]):
                        if rule["label"] not in ret:
                            if ret:
                                ret = ret + ',' + rule["label"]
                            else:
                                ret = ret + rule["label"]
            # フルマッチでない場合は後方マッチ
            if not ret:
                for rule in p_rule.phrase_rule:
                    if "words" in rule:
                        if self.rule_check2(verb_word, rule["words"]):
                            if rule["label"] not in ret:
                                if ret:
                                    ret = ret + ',' + rule["label"]
                                else:
                                    ret = ret + rule["label"]
        # 目的語からフェーズをチェック
        if verb_word in s_v_dic.sub_verb_dic and verb_word not in s_v_dic.special_sub_verb_dic and obj_start >= 0:
            ret2 = self.category_chek(obj_start, obj_end, -1, -1, -1, -1, '', p_rule,  *doc)
            # 項全体として重複をチェック
            if ret2:
                for ret3 in ret2.split(','):
                    if ret and ret3 not in ret:
                        ret = ret + ',' + ret3
                    else:
                        ret = ret3
            # 項の部分要素を重複をチェック
            for pt in range(obj_start, obj_end + 1):
                if (len(doc) > pt + 1 and (doc[pt + 1].lemma_ == '方' or doc[pt + 1].lemma_ == 'ため')) or (len(doc) > pt + 2 and doc[pt + 1].pos_ == 'AUX' and (doc[pt + 2].lemma_ == '方' or doc[pt + 2].lemma_ == 'ため')):      # 〇〇する方　はフェーズ判断に用いな
                    continue
                ret2 = self.category_chek(pt, pt, -1, -1, -1, -1, '', p_rule, *doc)
                if ret2:
                    for ret3 in ret2.split(','):
                        if ret and ret3 not in ret:
                            ret = ret + ',' + ret3
                        else:
                            ret = ret3
        # 補助表現がメイン術部のとき
        if not pre_category and not ret and verb_word in s_v_dic.sub_verb_dic:
            for rule in p_rule.phrase_rule:
                if "words" in rule:
                    if verb_word in rule["words"]:
                        if ret:
                            ret = ret + ',' + rule["label"]
                        else:
                            ret = ret + rule["label"]
        return ret.rstrip(',')

    ##########################################################################################################################################
    #    補助述部の時制チェック
    ##########################################################################################################################################

    def sub_category_check(self, predicate, *doc):
        rule = CategoryRule()

        if predicate["sub_lemma"]:
            if predicate["sub_lemma"] in rule.mirai:
                return "<時制.未来>"
            if predicate["sub_lemma"] in rule.genzai:
                return "<時制.現在>"
            if predicate["sub_lemma"] in rule.kako:
                return "<時制.過去>"
        return ''

    ##########################################################################################################################################
    #    カテゴリー可能性ありの補助述部の例外チェック
    ##########################################################################################################################################
    def sub_predicate_check(self, predicate, argument, p_rule, *doc):
        chunker = ChunkExtractor()
        s_v_dic = SubVerbDic()

#        if p_rule == categoryRule:
#            return False
        start = predicate["lemma_start"]
        end = predicate["lemma_end"]
        if doc[end].lemma_ == "する" and "名詞" in doc[end - 1].tag_:
            end = end - 1
        new_end = end
        # かかり先がフェーズ判定語の場合はNG
#        for rule in p_rule.phrase_rule:
#            if "words" in rule:
#                if self.rule_check(doc[doc[end].head.i].lemma_, rule["words"]):
#                    if chunker.rentai_check(doc[end].i, *doc):
#                        return False

        for c_pt in range(start, end):      # 述部の語幹だけを切り出す
            if doc[c_pt].pos_ == 'ADP' and (doc[c_pt].lemma_ != 'を' or (doc[c_pt].lemma_ == 'を' and len(doc) > c_pt + 1 and doc[c_pt + 1].norm_ == '為る')):
                new_end = c_pt - 1
                break
        verb_word = chunker.compaound(start, new_end, *doc)
        # O-V　ルール
        for arg in argument:
            if arg["predicate_id"] == predicate["id"]:
                obj_start = arg["lemma_start"]
                obj_end = arg["lemma_end"]
                obj_word = chunker.compaound(obj_start, obj_end, *doc)
                if obj_start >= 0:
                    for rule in p_rule.phrase_rule:
                        if "rule" in rule:
                            verb_ok = False
                            for check_verb in rule["rule"]["verb"]:
                                if check_verb and check_verb in verb_word:
                                    verb_ok = True
                                    break
                            if verb_ok:
                                for check_obj in rule["rule"]["obj"]:
                                    if check_obj and check_obj in obj_word:
                                        return True
                if predicate["sub_lemma_start"] > 0:
                    sub_verb = chunker.compaound(predicate["sub_lemma_start"], predicate["sub_lemma_end"], *doc)
                    for rule in p_rule.phrase_rule:
                        if "rule" in rule:
                            verb_ok = False
                            for check_verb in rule["rule"]["verb"]:
                                if check_verb and check_verb in sub_verb:
                                    verb_ok = True
                                    break
                            if verb_ok:
                                for check_obj in rule["rule"]["obj"]:
                                    if check_obj and check_obj in verb_word:
                                        return True

        # 補助用言以外のメイン術部
        if verb_word not in s_v_dic.sub_verb_dic or verb_word in s_v_dic.special_sub_verb_dic or verb_word in s_v_dic.information_verb_dic:
            if verb_word in s_v_dic.information_verb_dic:
                return True
            # フルマッチ
            for rule in p_rule.sub_phrase_rule:
                if "words" in rule:
                    if self.rule_check(verb_word, rule["words"]):
                        return True
            # フルマッチでない場合は後方マッチ
            for rule in p_rule.sub_phrase_rule:
                if "words" in rule:
                    if self.rule_check2(verb_word, rule["words"]):
                        return True
        return False

    ##########################################################################################################################################
    #    主述部のカテゴリーチェック
    ##########################################################################################################################################

    def rule_chek_and_set(self, predicate, argument, p_rule, *doc):
        rule = CategoryRule()
        s_v_dic = SubVerbDic()
        chunker = ChunkExtractor()

        single = ''
        for chek_predicate in predicate:
            no_argument = True
            ok_f = False
            # 補助述部でもチェック対象にしてよいかチェック
            if not chek_predicate["main"] and p_rule != rule:
                ok_f = self.sub_predicate_check(chek_predicate, argument, p_rule, *doc)
            if chek_predicate["main"] or ok_f:
                pre_category = ''
                koto_f = False
                for re_arg in argument:
                    category = ''
                    if chek_predicate["id"] != re_arg["predicate_id"]:
                        continue
                    no_argument = False
                    if not re_arg["case"]:
                        continue
                    if re_arg["subject"] and doc[re_arg["lemma_end"]].lemma_ != 'こと' and re_arg["case"] != 'が' and re_arg["case"] != 'も':  # 他の項がある主語からフェーズ生成はない
                        new_end = chek_predicate["lemma_end"]
                        for c_pt in range(chek_predicate["lemma_start"], chek_predicate["lemma_end"]):  # 述部の語幹だけを切り出す
                            if doc[c_pt].pos_ == 'ADP' and doc[c_pt].lemma_ != 'を':
                                new_end = c_pt - 1
                                break
                        verb_word = chunker.compaound(chek_predicate["lemma_start"], new_end, *doc)
#                        if p_rule == categoryRule:
#                            if verb_word in s_v_dic.sub_verb_dic:
#                                continue
                    if re_arg["case"] == 'は' and not re_arg["subject"]:
                        no_subject = True
                        for check in argument:
                            if check["subject"] and check["predicate_id"] == re_arg["predicate_id"]:
                                no_subject = False
                                break
                        if no_subject:
                            continue
                    if koto_f:    # 〜こと　の項があった場合は優先して　「を格」以外は拡張しない
                        continue
                    check_case = re_arg["case"].split("-")[0]
                    if len(check_case) == 1 or (check_case.startswith("に") and check_case != "について"):
                        check_case = re_arg["case"]     # に-副詞的 などは対象外
                    if check_case not in rule.category_analyze_case:
                        if "です" not in chek_predicate["lemma"]:
                            continue
                    if "rentai_subject" in re_arg:      # 連体修飾からの主語は対象外
                        continue
                    if not category:
                        check_end = chek_predicate["lemma_end"]
                        if doc[check_end].pos_ == 'AUX':  # 形容動詞の場合は助動詞部分を除いてチェック
                            check_end = check_end - 1
                        # 〜こと　は例外で項の先頭を見る
                        if doc[re_arg['lemma_end']].lemma_ == 'こと':
                            sub_category = ""
                            for check_p in predicate:
                                # 〜こと　の成分の動詞（〜）にかかる句を調べる
                                if check_p["lemma_start"] <= re_arg['lemma_start'] <= check_p["lemma_end"] or check_p["sub_lemma_start"] <= re_arg['lemma_start'] <= check_p["sub_lemma_end"]:
                                    for check_a in argument:
                                        if check_a["predicate_id"] == check_p["id"]:
                                            sub_category = self.category_chek(check_p["lemma_start"], check_p["lemma_end"], check_p["sub_lemma_start"], check_p["sub_lemma_end"], check_a["lemma_start"], check_a["lemma_end"], '', p_rule, *doc)
                                            pre_category = sub_category
                                            if re_arg["subject"]:
                                                koto_f = True
                                            if not sub_category and chek_predicate["sub_lemma"]:
                                                check_end = chek_predicate["sub_lemma_end"]
                                                if doc[check_end].pos_ == 'AUX':  # 形容動詞の場合は助動詞部分を覗いてチェック
                                                    check_end = check_end - 1
                                                add_category = self.category_chek(chek_predicate["sub_lemma_start"], check_end, -1, -1, re_arg['lemma_start'], re_arg['lemma_end'], pre_category, p_rule, *doc)
                                                pre_category = add_category
                                                for append in add_category.split(','):  # 重複は登録しない
                                                    if append != '<その他>' and append != '<告知>' and append not in sub_category:
                                                        if sub_category:
                                                            sub_category = sub_category + ',' + append
                                                        else:
                                                            sub_category = append
                            category = self.category_chek(chek_predicate["lemma_start"], check_end, chek_predicate["sub_lemma_start"], chek_predicate["sub_lemma_end"], re_arg['lemma_start'], re_arg['lemma_end'], pre_category, p_rule, *doc)
                            if not category:
                                category = sub_category
                        else:
                            category = self.category_chek(chek_predicate["lemma_start"], check_end, chek_predicate["sub_lemma_start"], chek_predicate["sub_lemma_end"], re_arg['lemma_start'], re_arg['lemma_end'], pre_category, p_rule, *doc)
                        pre_category = category
                        if not category and chek_predicate["sub_lemma"]:
                            check_end = chek_predicate["sub_lemma_end"]
                            if doc[check_end].pos_ == 'AUX':  # 形容動詞の場合は助動詞部分を覗いてチェック
                                check_end = check_end - 1
                            add_category = self.category_chek(chek_predicate["sub_lemma_start"], check_end, -1, -1, re_arg['lemma_start'], re_arg['lemma_end'], pre_category, p_rule, *doc)
                            pre_category = add_category
                            for append in add_category.split(','):  # 重複は登録しない
                                if append != '<その他>' and append != '<告知>' and append not in category:
                                    if category:
                                        category = category + ',' + append
                                    else:
                                        category = append
                    if category:
                        ret_tence = self.sub_category_check(chek_predicate, *doc)
                        if ret_tence not in category:
                            category = category + ',' + ret_tence
                    else:
                        category = self.sub_category_check(chek_predicate, *doc)
                    if category:
                        if "category" not in re_arg:
                            re_arg["category"] = category
                        else:
                            re_arg["category"] = re_arg["category"] + ',' + category
                    if category:  # categoryのある最終術部のphaesをシングルcategoryにする
                        for check_category in category.split(","):
                            if check_category not in single:
                                if single:
                                    single = single + "," + check_category
                                else:
                                    single = check_category
            if (chek_predicate["main"] or ok_f) and no_argument:
                # 項のない述部のチェック
                category = self.category_chek(chek_predicate["lemma_start"], chek_predicate["lemma_end"], chek_predicate["sub_lemma_start"], chek_predicate["sub_lemma_end"], -1, -1, "", p_rule, *doc)
                if category:
                    for check_category in category.split(","):
                        if check_category not in single:
                            if single:
                                single = single + "," + check_category
                            else:
                                single = check_category
        return single

    ##########################################################################################################################################
    #    文のカテゴリーチェック
    ##########################################################################################################################################

    def sentence_category_check(self, predicate, argument, *doc):
        return self.rule_chek_and_set(predicate, argument, CategoryRule, *doc)

