from chunker import ChunkExtractor
from sub_verb_dic import SubVerbDic
from category_rule_dic import CategoryRule
from government_action_dic import GovernmentActionRule

class SentenceCategoryCheker:

    def __init__(self):
        """
        関数`__init__`はクラスをインスタンス化した時に実行されます。
        """
        self.government_predicate = []
        self.subject_is_government = False
        self.is_government_press = False
        self.is_government_action = False
        self.action_is_haikei = False
        self.lase_predicate_subject_is_government = False

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

    def phase_chek(self, start, end, sub_start, sub_end, obj_start, obj_end, pre_phase, p_rule, *doc):
        ng_postfix = ["省", "庁", "局"]

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
        if len(doc) > new_end + 1 and doc[new_end + 1].lemma_ in ng_postfix:
            return ""
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
                        if ret:
                            ret = ret + ',' + rule["label"]
                        else:
                            ret = ret + rule["label"]
            # フルマッチでない場合は後方マッチ
            if not ret:
                for rule in p_rule.phrase_rule:
                    if "words" in rule:
                        if self.rule_check2(verb_word, rule["words"]):
                            if ret:
                                ret = ret + ',' + rule["label"]
                            else:
                                ret = ret + rule["label"]
        # 目的語からフェーズをチェック
        if verb_word in s_v_dic.sub_verb_dic and verb_word not in s_v_dic.special_sub_verb_dic and obj_start >= 0:
            ret2 = self.phase_chek(obj_start, obj_end, -1, -1, -1, -1, '', p_rule,  *doc)
            # 項全体として重複をチェック
            for ret3 in ret2.split(','):
                if ret3 not in ret:
                    ret = ret + ',' + ret3 + ','
            # 項の部分要素を重複をチェック
            for pt in range(obj_start, obj_end + 1):
                if (len(doc) > pt + 1 and (doc[pt + 1].lemma_ == '方' or doc[pt + 1].lemma_ == 'ため')) or (len(doc) > pt + 2 and doc[pt + 1].pos_ == 'AUX' and (doc[pt + 2].lemma_ == '方' or doc[pt + 2].lemma_ == 'ため')):      # 〇〇する方　はフェーズ判断に用いな
                    continue
                ret2 = self.phase_chek(pt, pt, -1, -1, -1, -1, '', p_rule, *doc)
                for ret3 in ret2.split(','):
                    if ret3 not in ret:
                        ret = ret + ',' + ret3 + ','
        # 補助表現がメイン術部のとき
        if not pre_phase and not ret and verb_word in s_v_dic.sub_verb_dic:
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

    def sub_phase_check(self, predicate, *doc):
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
    #    フェイズ可能性ありの補助述部の例外チェック
    ##########################################################################################################################################
    def sub_predicate_check(self, predicate, argument, p_rule, *doc):
        chunker = ChunkExtractor()
        s_v_dic = SubVerbDic()

#        if p_rule == PhaseRule:
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
                pre_phase = ''
                koto_f = False
                for re_arg in argument:
                    phase = ''
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
#                        if p_rule == PhaseRule:
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
                    if check_case not in rule.phase_analyze_case:
                        continue
                    if "rentai_subject" in re_arg:      # 連体修飾からの主語は対象外
                        continue
                    if not phase:
                        check_end = chek_predicate["lemma_end"]
                        if doc[check_end].pos_ == 'AUX':  # 形容動詞の場合は助動詞部分を除いてチェック
                            check_end = check_end - 1
                        # 〜こと　は例外で項の先頭を見る
                        if doc[re_arg['lemma_end']].lemma_ == 'こと':
                            sub_phase = ""
                            for check_p in predicate:
                                # 〜こと　の成分の動詞（〜）にかかる句を調べる
                                if check_p["lemma_start"] <= re_arg['lemma_start'] <= check_p["lemma_end"] or check_p["sub_lemma_start"] <= re_arg['lemma_start'] <= check_p["sub_lemma_end"]:
                                    for check_a in argument:
                                        if check_a["predicate_id"] == check_p["id"]:
                                            sub_phase = self.phase_chek(check_p["lemma_start"], check_p["lemma_end"], check_p["sub_lemma_start"], check_p["sub_lemma_end"], check_a["lemma_start"], check_a["lemma_end"], '', p_rule, *doc)
                                            pre_phase = sub_phase
                                            if re_arg["subject"]:
                                                koto_f = True
                                            if not sub_phase and chek_predicate["sub_lemma"]:
                                                check_end = chek_predicate["sub_lemma_end"]
                                                if doc[check_end].pos_ == 'AUX':  # 形容動詞の場合は助動詞部分を覗いてチェック
                                                    check_end = check_end - 1
                                                add_phase = self.phase_chek(chek_predicate["sub_lemma_start"], check_end, -1, -1, re_arg['lemma_start'], re_arg['lemma_end'], pre_phase, p_rule, *doc)
                                                pre_phase = add_phase
                                                for append in add_phase.split(','):  # 重複は登録しない
                                                    if append != '<その他>' and append != '<告知>' and append not in sub_phase:
                                                        if sub_phase:
                                                            sub_phase = phase + ',' + append
                                                        else:
                                                            sub_phase = append
                            phase = self.phase_chek(chek_predicate["lemma_start"], check_end, chek_predicate["sub_lemma_start"], chek_predicate["sub_lemma_end"], re_arg['lemma_start'], re_arg['lemma_end'], pre_phase, p_rule, *doc)
                            if not phase:
                                phase = sub_phase
                        else:
                            phase = self.phase_chek(chek_predicate["lemma_start"], check_end, chek_predicate["sub_lemma_start"], chek_predicate["sub_lemma_end"], re_arg['lemma_start'], re_arg['lemma_end'], pre_phase, p_rule, *doc)
                        pre_phase = phase
                        if not phase and chek_predicate["sub_lemma"]:
                            check_end = chek_predicate["sub_lemma_end"]
                            if doc[check_end].pos_ == 'AUX':  # 形容動詞の場合は助動詞部分を覗いてチェック
                                check_end = check_end - 1
                            add_phase = self.phase_chek(chek_predicate["sub_lemma_start"], check_end, -1, -1, re_arg['lemma_start'], re_arg['lemma_end'], pre_phase, p_rule, *doc)
                            pre_phase = add_phase
                            for append in add_phase.split(','):  # 重複は登録しない
                                if append != '<その他>' and append != '<告知>' and append not in phase:
                                    if phase:
                                        phase = phase + ',' + append
                                    else:
                                        phase = append
                    if phase:
                        ret_tence = self.sub_phase_check(chek_predicate, *doc)
                        if ret_tence not in phase:
                            phase = phase + ',' + ret_tence
                    else:
                        phase = self.sub_phase_check(chek_predicate, *doc)
                    if phase:
                        if "phase" not in re_arg:
                            re_arg["phase"] = phase
                        else:
                            re_arg["phase"] = re_arg["phase"] + ',' + phase
                    if phase:  # phaseのある最終術部のphaesをシングルphaseにする
                        for check_phase in phase.split(","):
                            if check_phase not in single:
                                if single:
                                    single = single + "," + check_phase
                                else:
                                    single = check_phase
            if (chek_predicate["main"] or ok_f) and no_argument:
                # 項のない述部のチェック
                phase = self.phase_chek(chek_predicate["lemma_start"], chek_predicate["lemma_end"], chek_predicate["sub_lemma_start"], chek_predicate["sub_lemma_end"], -1, -1, "", p_rule, *doc)
                if phase:
                    for check_phase in phase.split(","):
                        if check_phase not in single:
                            if single:
                                single = single + "," + check_phase
                            else:
                                single = check_phase
        return single

    ##########################################################################################################################################
    #    文のカテゴリーチェック
    ##########################################################################################################################################

    def sentence_category_check(self, predicate, argument, *doc):
        return self.rule_chek_and_set(predicate, argument, CategoryRule, *doc)

