class GovernmentActionRule:
    """
    政府活動ルール

    法整備・規制
        検討,施行,改正,訓示,要請,認可,
    目標・計画・指針
        期日,
        意思決定,アクション,
        方策内容,方策作成,
    税制・予算
    指数・統計
    補助金・交付金
        支援,募集,
        融資,購入,売却,
    国際会議・会合・会談
        会談,派遣,
    その他
        契約,訴訟,勧告,
        背景,所見,
        創立,連携,
        システム管理,
        情報公開,
        イベント,


    """
    # 検討審議
    kentou_dic = [
        "審議", "判断", "可否", "審査", "諮問", "検討", "試算", "見直す", "継続審議と", "精査", "法整備", "協議"
    ]
    # O-V 規則
    o_v_kentou_dic = {"obj": {"法", "法律", "規則", "対策", "方向性", "提言", "意見", "結果", "戦略", "制度"},
                      "verb": {"整理", "まとめる", "整える", "分析", "見直す", "とりまとめる", "策定", "整備", "分ける"}
                      }

    o_v_kentou2_dic = {"obj": {"見直し", "検討", "審議", "判断", "審査", "諮問", "試算", "策定"},
                       "verb": {"行う", "行って", "入る", "継続"}
                       }

    o_v_kentou3_dic = {"obj": {"研究会", "検討会"},
                       "verb": {"開催", "立ち上げる", "設置"}
                       }

    o_v_kentou4_dic = {"obj": {"条件"},
                       "verb": {"変える", "変更", "修正"}
                       }

    # 施行, "定める", "締結", "提出"
    sekou_dic = [
        "施行", "公布", "発効", "発動", "閣議決定"
    ]

    # O-V 規則
    o_v_sekou_dic = {"obj": {"措置", "施策", "対策", "対応策", "制度", "承認", "規則", "措置", "対象"},
                     "verb": {"実施", "行う", "導入", "判断", "発表", "適用", "加える", "締結", "定める", "発行", "提出"}
                     }

    # 改正
    kaisei_dic = [
        "改正", "改訂", "改定", "追加", "変更", "修正", "見直す", "加わる"
    ]
    # O-V 規則
    o_v_kaisei_dic = {"obj": {"内容", "規則", "法律", "規格", "仕様"},
                      "verb": {"加わる"}
                      }
    o_v_kaisei2_dic = {"obj": {"制限", "宣言", "布令", "手続き"},
                       "verb": {"延長", "短縮"}
                       }

    # 廃止
    haishi_dic = [
        "廃止", "撤廃", "延期", "中止", "撤回", "解除", "やめる", "停止", "凍結"
    ]

    # 訓示
    kunji_dic = [
        "訓示", "告示", "発令", "発出", "命ずる", "発令"
    ]

    # 要請
    yousei_dic = [
        "要請", "求める", "要求", "要望"
    ]

    # 認可, "できる"
    ninka_dic = [
        "承認", "認める", "許可", "該当", "適合", "認定", "認可", "了承", "了解", "受領", "採択", "解禁", "解除", "合格",
        "出せるようにする", "容認", "受理", "署名", "登録"
    ]
    # O-V 規則
    o_v_ninka_dic = {"obj": {"承認", "許可", "認可", "手続き", "採択"},
                     "verb": {"決める", "決定", "見送る", "出す", "継続", "見直す", "受ける", "下りる", "下る"}
                     }

    o_v_ninka2_dic = {"obj": {"承認", "許可", "認可", "手続き", "採択", "登録"},
                      "verb": {"できる"}
                      }

    # 契約
    keiyaku_dic = [
        "契約", "結ぶ", "締結", "合意", "取り交わす"
    ]

    # 訴訟
    sosyou_dic = [
        "提訴", "訴訟", "裁判", "公判", "控訴", "訴追", "起訴"
    ]

    # 勧告
    kannkoku_dic = [
        "勧告", "警告", "命ずる", "命じる", "禁止", "処分", "摘発", "指導", "行政指導", "書類送検", "発令",
        "要請", "削除要請", "通知", "命令", "削除命令", "規制", "できない", "行政処分", "停止", "参加停止", "排除", "規制",
        "立入検査", "立ち入り検査", "輸出規制"
    ]
    # O-V 規則
    o_v_kannkoku_dic = {"obj": {"改善", "強化", "理解", "規制"},
                        "verb": {"促す", "求める", "強める", "動く"}
                        }
    o_v_kannkoku2_dic = {"obj": {"罰金", "制裁", "税金", "反則金", "罰"},
                         "verb": {"科す", "課す"}
                         }
    o_v_kannkoku3_dic = {"obj": {"ロックダウン", "制裁", "課税", "徴税"},
                         "verb": {"拡大", "延長"}
                         }
    o_v_kannkoku4_dic = {"obj": {"警告", "勧告", "注意", "制裁"},
                         "verb": {"記載", "追記"}
                         }

    # 期日
    date_dic = [
        "延期", "延長", "開始", "終了", "期限", "迎える", "までと"
    ]

    # 意思決定(方針) , "始める", "開始", "まとめる", "定める", "強化", "決定","取りまとめる", "講じる", "講ずる", "分かる", "迎える", "入れる",
    decision_dic = [
        "固める", "差別したとする", "決定", "示す", "方針", "推す", "強める", "減らす", "進めること", "採択", "目標",
        "加速", "模索", "進める", "続ける", "凍結", "指定", "推奨", "変更", "中止", "加える", "進める", "続ける", "乗りだす",
        "推し進める", "指定", "適用", "維持", "推計", "拡大", "縮小", "みる", "やめる", "使う", "停止", "選ぶ", "シフト", "づける",
        "結論", "控える", "支持", "推進", "増やす", "短縮", "排除", "踏み切る", "打ち出す", "急ぐ", "示す",
        "掲げる", "求める", "掲げる", "目指す", "予定", "進める", "推進", "加速", "拡充",
        "活用", "決定", "図る", "いたす", "いただく", "目的とする", "目標とする", "示す",
        "めどを付ける", "出来る", "引き上げる", "引き下げる", "実質ゼロに", "促進", "広げる", "抑え込む", "変更",

        "回答する", "採択", "賛同", "賛同宣言", "指定", "従う",
        "申請受付", "理解を深める", "選定", "設定", "措置", "加速", "継続", "促す", "続ける",
        "停止", "対応", "反映", "拡充", "確保", "図る", "決める"
    ]

    # アクション（行動）, "なる", "受ける", "響く", "判明"
    action_dic = [
        "使用", "取りかかる", "取り扱う", "受け付ける", "出す", "説明", "対策", "準備", "見解", "転換", "提出", "記載",
        "つなげる", "掲げる", "向ける", "先行開放", "増やすように促す", "警戒", "改善策", "電動車にする", "導入", "備える",
        "再開", "参加停止", "始める", "1つ", "二転三転", "乗り出す", "入る", "始まる", "塗り替える", "取引", "整理", "独占",
        "開放", "整備", "主催", "実施", "指定", "始動", "協力", "検査", "立てる", "かかる", "つくる", "ネット配信", "閲覧",
        "開く", "関する", "機会とする", "軽減", "言及", "呼びかける", "呼び掛ける", "行う", "削減", "指摘", "諮問する",
        "事態となる", "持つ", "商用化", "設ける", "増える", "追加", "底上げ", "入手", "複数掲載",
        "明らかにする", "明確にする", "入れ始める", "スタート", "始まる", "始動", "本格始動", "続ける", "終わる", "終る",
        "する", "達成", "行なう", "行う", "お知らせ", "記念", "報ずる", "参加", "成功",
        "開幕", "主催", "掲げる", "倍増", "開発", "乗り出す", "乗りだす", "着手", "取り組む",

        "申請がある", "引き出す", "深化", "推移", "開発", "活用", "工程", "構築", "作る", "作成", "実用化", "取り組む",
        "取組", "進める", "推進", "発掘", "育成", "経営", "交換", "登録", "実現", "開始",
        "調べる", "追加調査", "か調べる", "調査", "検査", "取りまとめる", "改める", "まとめる", "外す", "除外", "見送る", "変える",
        "打ち出す", "分ける", "通り", "申請受け付け", "加わる", "盛り込む", "重視", "抑え込む", "発行", "提言", "棚上げに", "呼びかける"

    ]

    # 方策内容, "決める", "戦略"
    naiyou_dic = [
        "緩和", "強化", "撤廃", "検討", "対策", "枠", "要件", "規定", "規制", "申請", "担う", "盛り込む", "改訂", "要旨"
    ]
    # O-V 規則
    o_v_naiyou_dic = {"obj": {"申請", "登録", "報告", "審査"},
                      "verb": {"不要", "必要"}
                      }

    o_v_naiyou2_dic = {"obj": {"ネガティブリスト", "候補"},
                       "verb": {"外す", "入れる", "含める"}
                       }

    o_v_naiyou3_dic = {"obj": {"規制", "決まり", "取締", "調査", "要請"},
                       "verb": {"強化", "緩和"}
                       }
    # 方策作成 , "まとめる", "掲げる", "引き下げる", "引き上げる","作る", "作成",
    sakusei_dic = [
        "一つにする", "改正", "施行", "改訂", "明記"
    ]
    # O-V 規則
    o_v_sakusei_dic = {"obj": {"規定", "規則", "決まり", "法律", "対策", "漁獲枠", "枠", "原案"},
                       "verb": {"定める", "強化", "決める", "策定", "明記"}
                       }
    o_v_sakusei2_dic = {"obj": {"報告書", "レポート", "提言"},
                        "verb": {"取りまとめる", "まとめる", "策定"}
                        }

    # 背景 (政府活動の背景。企業活動の元になる政府活動ではない)
    haikei_dic = [
        "高まる", "受ける", "踏まえる", "伸びる", "強まる", "背景", "上昇しているため", "伴う", "裏付け",

        "課題", "見据える", "及ぼす", "発生", "下回る", "経過", "直面", "必要", "必要不可欠", "不可欠", "基づく", "ため"
    ]

    # 所見　 "みる", "見る", "見通し", "なる", "目指す",, "だ"
    shoken_dic = [
        "感ずる", "思う", "考える", "感じる", "見込み", "推測", "立場", "語る",
        "断定", "断ずる", "見方", "崩す", "見積もる", "厳しい", "難しい", "見通し",
        "考え", "主張", "述べる", "認識", "否定", "評する", "予定", "必要がある",
        "力を入れる",

        "願う", "歓迎", "期待", "見込み", "見込める", "見通しとなる", "伺う", "努める", "踏まえる", "目的とする", "目的", "メドがつく",
        "和らげると"

    ]

    # 創立
    souritsu_dic = [
        "新設", "設立", "創立", "立ち上げる", "解散", "発展的解消", "開会", "閉会", "発足", "開設", "開催", "設置", "創設",
        "立ち上げる"
    ]

    # 連携
    renkei_dic = [
        "連携", "共業", "参画", "協働", "呼びかける"
    ]

    # システム管理
    system_dic = [
        "移す", "移動", "機能更新", "システム", "アプリ", "サービス", "アップデート", "バージョンアップ", "システム構築",
        "システム管理", "プログラム", "台帳", "機能", "技術"
    ]

    # 支援
    shien_dic = [
        "支援", "後押し", "後押しする", "表彰", "補助", "贈呈", "授与", "提供"
    ]

    # 募集
    boshyu_dic = [
        "募集", "誘致", "募る", "公募", "招請"
    ]

    # 融資, "つける"
    yuushi_dic = [
        "拠出", "出資", "ファンド", "融資", "資金提供", "支援", "投資", "補助", "負担"
    ]
    # O-V 規則
    o_v_yuushi_dic = {"obj": {"補助金", "補助", "援助", "救済"},
                      "verb": {"下げる", "上げる", "増加", "削減", "減少", "打ち切る", "出す", "採択", "延長", "充実", "拡充", "決定"}
                      }

    # 購入
    kounyuu_dic = [
        "購入", "落札"
    ]

    # 売却
    baikyaku_dic = [
        "売却", "捌く", "売りわたす", "売渡す", "売る", "鬻ぐ", "販売", "譲る"
    ]

    # 情報公開  "なれる", "判明",
    koukai_dic = [
        "確認", "打ち出す", "公表", "発表", "公開", "通知", "発信", "指数", "回復",
        "1位", "2位", "3位", "4位", "5位", "6位", "7位", "8位", "9位",
        "1回", "2回", "3回", "4回", "5回", "6回", "7回", "8回", "9回",
        "円", "トン", "人", "増える", "減る", "上がる", "下がる", "値上がり", "値下がり",
        "上昇", "下降", "わかる", "落ち込む", "超える", "上回る", "下回る", "上方修正", "下方修正", "増加", "減少",
        "割高", "割安", "落ちる", "上る", "昇る", "騰がる", "家計調査", "報告書", "表明", "記載", "明らかにする",
        "報告", "安い", "高い", "引き上げる", "引き下げる",

        "掲載", "公示", "周知", "宣言", "表する", "報告書", "進捗報告", "審議記録", "閣議配布", "会議の様子",
        "報告がある", "お知らせ", "参照", "明記"

    ]

    # 会談  "会議", "分科会","会談",
    kaidan_dic = [
        "開く",
        "議論", "意見交換", "聞く"
    ]
    # O-V 規則
    o_v_kaidan_dic = {"obj": {"表敬", "訪問", "来訪"},
                      "verb": {"受ける"}
                      }

    o_v_kaidan2_dic = {"obj": {"委員会", "会議", "議会", "会合", "分科会", "会談", "会"},
                       "verb": {"開催", "開く", "臨む"}
                       }

    # 派遣
    haken_dic = [
        "派遣", "表敬", "訪れる", "訪問", "立ち合う", "視察", "出張", "参加", "出席"
    ]

    # イベント
    event_dic = [
        "開催", "開始", "閉幕", "開幕", "中止", "延期"
    ]

    # 方針、計画
    houshin_dic = [
       "方針です", "方針だ", "目指す"
    ]
    # O-V 規則
    o_v_houshin_dic = {"obj": {"目標", "方針", "計画", "目的", "アプローチ", "工程", "ガイドライン", "戦略", "キャンペーン",
                               "コスト", "要旨", "ツール", "試算"},
                       "verb": {"立てる", "考える", "立案", "設定", "設ける", "掲げる", "策定", "削減", "まとめる",
                                "決める", "公表", "発表", "示す", "宣言", "策定", "明記", "試算", "通り", "盛り込む",
                                "明らかにする"}
                       }
    o_v_houshin2_dic = {"obj": {"導入", "利用", "活用"},
                        "verb": {"予定", "考える", "決める", "示す", "宣言", "策定", "明記", "試算", "盛り込む"}
                        }
    # 税制・予算
    zaisei_dic = [
        "関税", "納税"
    ]
    # O-V 規則
    o_v_zaisei_dic = {"obj": {"予算", "税務", "課税", "税優遇"},
                      "verb": {"決定", "検討", "変更", "要請", "合意", "実行", "強化", "提出", "要求"}
                      }
    o_v_zaisei2_dic = {"obj": {"関税", "予算"},
                       "verb": {"トン", "円"}
                       }
    o_v_zaisei3_dic = {"obj": {"ファンド", "税措置"},
                       "verb": {"設ける", "設置", "決定", "行う"}
                       }
    # 指数・統計, "加える"
    shisuu_dic = [
        "回復", "上がる", "下がる", "増える", "増加", "減る", "減少", "上回る", "下回る", "割高", "突破", "最小", "最少", "最大", "最多",
        "1位", "2位", "3位", "4位", "5位", "6位", "7位", "8位", "9位", "首位",
        "1回", "2回", "3回", "4回", "5回", "6回", "7回", "8回", "9回"
    ]
    # O-V 規則
    o_v_shisuu_dic = {"obj": {"比率", "比", "率", "量", "％", "トン", "円", "ドル", "人", "額", "価", "社", "安値", "高値",
                              "位", "件"},
                      "verb": {"なる", "固まる", "値下がり", "値上がり", "高い", "安い", "超える", "上昇", "下降", "落ちる",
                               "引き上げる", "引き下げる", "落ち込む", "修正", "下落", "突破", "目立つ"}
                      }

    o_v_shisuu2_dic = {"obj": {"あたり"},
                       "verb": {"超える", "落ち込む"}
                       }

    o_v_shisuu3_dic = {"obj": {"価格", "額", "量", "率", "在庫", "面積", "広さ", "数", "企業", "金"},
                       "verb": {"円", "ドル", "ユーロ", "ポンド", "元", "人", "社", "メートル", "トン", "キロ", "グラム",
                                "平米", "坪", "％", "戸"}
                       }
    o_v_shisuu4_dic = {"obj": {"者"},
                       "verb": {"超える", "突破", "上昇", "上回る", "下回る"}
                       }

    o_v_shisuu5_dic = {"obj": {"回"},
                       "verb": {"推計", "集計"}
                       }

    o_v_shisuu6_dic = {"obj": {"位", "円", "ドル"},
                       "verb": {"保つ", "保持", "維持", "キープ"}
                       }

    # その他
    others_dic = [
        "経過"
    ]
    o_v_others_dic = {"obj": {"キャンペーン"},
                      "verb": {"実施"}
                      }

    phrase_rule = [{"label": "<検討>", "words": kentou_dic},
                   {"label": "<検討>", "rule": o_v_kentou_dic},
                   {"label": "<検討>", "rule": o_v_kentou2_dic},
                   {"label": "<検討>", "rule": o_v_kentou3_dic},
                   {"label": "<検討>", "rule": o_v_kentou4_dic},
                   {"label": "<施行>", "words": sekou_dic},
                   {"label": "<施行>", "rule": o_v_sekou_dic},
                   {"label": "<改正>", "words": kaisei_dic},
                   {"label": "<改正>", "rule": o_v_kaisei_dic},
                   {"label": "<改正>", "rule": o_v_kaisei2_dic},
                   {"label": "<廃止>", "words": haishi_dic},
                   {"label": "<訓示>", "words": kunji_dic},
                   {"label": "<要請>", "words": yousei_dic},
                   {"label": "<認可>", "words": ninka_dic},
                   {"label": "<認可>", "rule": o_v_ninka_dic},
                   {"label": "<認可>", "rule": o_v_ninka2_dic},
                   {"label": "<契約>", "words": keiyaku_dic},
                   {"label": "<訴訟>", "words": sosyou_dic},
                   {"label": "<勧告>", "words": kannkoku_dic},
                   {"label": "<勧告>", "rule": o_v_kannkoku_dic},
                   {"label": "<勧告>", "rule": o_v_kannkoku2_dic},
                   {"label": "<勧告>", "rule": o_v_kannkoku3_dic},
                   {"label": "<勧告>", "rule": o_v_kannkoku4_dic},
                   {"label": "<期日>", "words": date_dic},
                   {"label": "<意思決定>", "words": decision_dic},
                   {"label": "<アクション>", "words": action_dic},
                   {"label": "<方策内容>", "words": naiyou_dic},
                   {"label": "<方策内容>", "rule": o_v_naiyou_dic},
                   {"label": "<方策内容>", "rule": o_v_naiyou2_dic},
                   {"label": "<方策内容>", "rule": o_v_naiyou3_dic},
                   {"label": "<方策作成>", "words": sakusei_dic},
                   {"label": "<方策作成>", "rule": o_v_sakusei_dic},
                   {"label": "<方策作成>", "rule": o_v_sakusei2_dic},
                   {"label": "<背景>", "words": haikei_dic},
                   {"label": "<所見>", "words": shoken_dic},
                   {"label": "<創立>", "words": souritsu_dic},
                   {"label": "<連携>", "words": renkei_dic},
                   {"label": "<システム管理>", "words": system_dic},
                   {"label": "<支援>", "words": shien_dic},
                   {"label": "<募集>", "words": boshyu_dic},
                   {"label": "<融資>", "words": yuushi_dic},
                   {"label": "<融資>", "rule": o_v_yuushi_dic},
                   {"label": "<購入>", "words": kounyuu_dic},
                   {"label": "<売却>", "words": baikyaku_dic},
                   {"label": "<情報公開>", "words": koukai_dic},
                   {"label": "<会談>", "words": kaidan_dic},
                   {"label": "<会談>", "rule": o_v_kaidan_dic},
                   {"label": "<会談>", "rule": o_v_kaidan2_dic},
                   {"label": "<派遣>", "words": haken_dic},
                   {"label": "<イベント>", "words": event_dic},
                   {"label": "<方針>", "words": houshin_dic},
                   {"label": "<方針>", "rule": o_v_houshin_dic},
                   {"label": "<方針>", "rule": o_v_houshin2_dic},
                   {"label": "<財政>", "words": zaisei_dic},
                   {"label": "<財政>", "rule": o_v_zaisei_dic},
                   {"label": "<財政>", "rule": o_v_zaisei2_dic},
                   {"label": "<財政>", "rule": o_v_zaisei3_dic},
                   {"label": "<指数>", "words": shisuu_dic},
                   {"label": "<指数>", "rule": o_v_shisuu_dic},
                   {"label": "<指数>", "rule": o_v_shisuu2_dic},
                   {"label": "<指数>", "rule": o_v_shisuu3_dic},
                   {"label": "<指数>", "rule": o_v_shisuu4_dic},
                   {"label": "<指数>", "rule": o_v_shisuu5_dic},
                   {"label": "<指数>", "rule": o_v_shisuu6_dic},
                   {"label": "<その他>", "words": others_dic},
                   {"label": "<その他>", "rule": o_v_others_dic}
                   ]

    # 補助述部でも政府活動と認めるカテゴリのルール
    sub_phrase_rule = [
        #                {"label": "<検討>", "words": kentou_dic},
        {"label": "<方策内容>", "words": naiyou_dic},
        {"label": "<方策作成>", "words": sakusei_dic},
        {"label": "<施行>", "words": sekou_dic},
        {"label": "<改正>", "words": kaisei_dic},
        {"label": "<廃止>", "words": haishi_dic},
        {"label": "<訓示>", "words": kunji_dic},
        {"label": "<要請>", "words": yousei_dic},
        {"label": "<認可>", "words": ninka_dic},
        {"label": "<契約>", "words": keiyaku_dic},
        {"label": "<訴訟>", "words": sosyou_dic},
        {"label": "<勧告>", "words": kannkoku_dic},
        {"label": "<所見>", "words": shoken_dic},
#        {"label": "<情報公開>", "words": koukai_dic},
        {"label": "<融資>", "words": yuushi_dic},
        {"label": "<指数>", "words": shisuu_dic},
        {"label": "<募集>", "words": boshyu_dic}
    ]

    # 政府の情報発信を表す述部
    press_dic = ["促す", "発表", "公表", "策定", "抑え込む", "まとめる", "向ける", "求める", "広げる", "開く", "決める",
                 "強化", "削除命令", "導入", "推進", "持つ", "改訂", "定める", "倍増", "警戒", "掲げる", "促進", "競う",
                 "実質ゼロに", "通知", "強める", "めざす", "進める", "伴う", "引き上げる", "容認", "削除要請", "延長",
                 "固める", "出す", "発令", "対象と", "見通しとなる", "つける", "全面公開", "指定", "主催", "試算", "報告",
                 "までと", "緩和", "実施", "主張", "方針です", "分かる", "明らかになる", "乗り出す", "提出", "着手", "急ぐ",
                 "誘致", "判断", "盛り込む", "協議", "力を入れる", "取りかかる", "増やすように促す", "外す", "わかる", "明記",
                 "通り", "明確に", "先送り", "推奨", "和らげると", "拡充"
                 ]

    """
    マルチラベルをシングルラベルに変換するルール
    , "<方策内容>"

    目標・計画・指針
    法整備・規制
    補助金・交付金
    税制・予算
    指数・統計
    国際会議・会合・会談
    その他
    """

    # "<アクション>",

    mokuhyou = ["<意思決定>", "<方針>"]
    houseibi = ["<検討>", "<施行>", "<改正>", "<廃止>", "<要請>", "<認可>", "<訓示>", "<訴訟>", "<勧告>", "<方策内容>", "<方策作成>"]
    hojyokin = ["<募集>", "<融資>", "<購入>", "<売却>"]
    zeisei = ["<財政>"]
    shisuu = ["<指数>"]
    kaigi = ["<会談>", "<派遣>"]
    sonota = ["<システム管理>", "<支援>", "<期日>", "<契約>", "<背景>", "<所見>", "<創立>", "<連携>", "<情報公開>", "<イベント>", "<その他>"]

    hourei = ["<検討>", "<施行>", "<改正>", "<廃止>", "<方策作成>"]
    shihou = ["<要請>", "<訓示>", "<認可>", "<契約>", "<訴訟>", "<勧告>"]

    single_rule_old = [{"single": "<法令>", "labels": hourei},
                       {"single": "<行政・司法>", "labels": shihou}
                       ]

    # 複数ラベルが出る場合は上が優先順位が高い
    single_rule = [{"single": "<税制・予算>", "labels": zeisei},
                   {"single": "<指数・統計>", "labels": shisuu},
                   {"single": "<補助金・交付金>", "labels": hojyokin},
                   {"single": "<法整備・規制>", "labels": houseibi},
                   {"single": "<国際会議・会合・会談>", "labels": kaigi},
                   {"single": "<目標・計画・指針>", "labels": mokuhyou},
                   {"single": "<その他>", "labels": sonota}
                   ]

    stat_rule = ["<検討>", "<施行>", "<改正>", "<廃止>"]
