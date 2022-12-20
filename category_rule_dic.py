class CategoryRule:
    """
    ニュースカテゴリールール

意見
意見（疑問）
見解
提案

    報告セミナー紹介

イベント
説明
セミナー

    解説
    談話・講話
    聴講・聴取
    報告・通知

    論説（本文の最後まで企業活動がない）

紹介

議案

会談
対談

業界情報

予測

    市場予測
市場データ
情報公開
レポート

    規制・制定
政府・行革
政府・認可
政府活動・宣言

    契約

    技術・製品紹介
    技術説明（リードの後に説明）
    情報提供

    技術開発
    技術利用
開発
研究開発
実験

    業績発表
業績

    経営戦略
    事業計画
経営戦略
施策
方針
目標
行動変化
企業活動（対策）

業務提携

採用利用

支援

投資

    債券発行
    資金調達
資金調達

    事業開始
    製品発表
    製品発表・販売
サービス開始
商品化
生産開始
製品化

    価格変更
価格変更
価格

    人事
人事
組織
組織設立
組織変更

    設備・組織
海外展開
設備

    設備投資

    背景・理由
技術背景
社会情勢
前提

現象
効果
背景

    """
    # 意見
    iken_dic = [
        "意見", "述べる"
    ]
    # 見解
    kenkai_dic = [
        "見解", "見る"
    ]
    # 提案
    teian_dic = [
        "提案"
    ]

    # イベント
    event_dic = [
        "イベント", "公開"
    ]
    # O-V 規則
    o_v_event_dic = {"obj": {"ベント", "催し"},
                      "verb": {"開催"}
                      }

    # セミナー
    seminar_dic = [
        "セミナー", "聞きいただける"
    ]

    # 説明
    setusmei_dic = [
        "説明"
    ]

    # 紹介
    shoukai_dic = [
        "紹介"
    ]

    # 議案
    gian_dic = [
        "議案"
    ]

    # 会談
    kaigi_dic = [
        "会談", "聴取", "出席"
    ]
    # O-V 規則
    o_v_kaigi_dic = {"obj": {"会合", "会議"},
                      "verb": {"開催"}
                      }

    # 対談
    taidan_dic = [
        "対談", "聞く"
    ]

    # 業界情報
    gyoukai_dic = [
        "業界情報", "業界の概要"
    ]

    # 予測
    yosoku_dic = [
        "予測"
    ]
    # O-V 規則
    o_v_yosoku_dic = {"obj": {"予測"},
                      "verb": {"発表"}
                      }

    # 市場データ
    shijyou_dic = [
        "市場データ", "市場の見通し"
        ]

    # 情報公開
    koukai_dic = [
        "情報公開", "報告"
        ]

    # レポート
    report_dic = [
        "レポート", ""
        ]
    # O-V 規則
    o_v_report_dic = {"obj": {"レポート"},
                      "verb": {"発表", "報告", "リリース"}
                      }

    # 政府・行革
    gyoukaku_dic = [
        "行革", "改革"
        ]
    # O-V 規則
    o_v_gyoukaku_dic = {"obj": {"政府"},
                      "verb": {"推進"}
                      }

    # 政府・認可
    ninnka_dic = [
        "認可", ""
        ]
    # O-V 規則
    o_v_ninnka_dic = {"obj": {"認可"},
                      "verb": {"出す", "取得"}
                      }

    # 政府活動・宣言
    sengen_dic = [
        "政府活動", ""
        ]
    # O-V 規則
    o_v_sengen_dic = {"obj": {"政府"},
                      "verb": {"出す", "発表", "報告", "リリース"}
                      }

    # 開発
    kaihatsu_dic = [
        "開発", "設計"
        ]

    # 研究開発
    kenkyuu_dic = [
        "研究開発", "研究"
        ]

    # 実験
    jikken_dic = [
        "実験", "実証実験"
        ]

    # 業績
    gyouseki_dic = [
        "業績", ""
        ]
    # O-V 規則
    o_v_gyouseki_dic = {"obj": {"業績", "売上", "利益"},
                      "verb": {"発表", "計上"}
                      }

    # 経営戦略
    senryaku_dic = [
        "経営戦略", ""
        ]
    # O-V 規則
    o_v_senryaku_dic = {"obj": {"事業", "人員", "工数", "経費", "予算", "リソース"},
                      "verb": {"集める", "集中"}
                      }

    # 施策
    sisaku_dic = [
        "施策", "策定"
        ]

    # 方針
    housin_dic = [
        "方針", "据える", "加速", "発掘", "打ち出す", "振り向ける", "図る", "目指す", "導入", "高める", "充実", "能力増と", "増強",
        "表明", "見込みです", "対応", "強化", "決定", "進める", "上げる", "応ずる", "転換", "始動", "示す", "掲げる", "突入"
        ]

    # 目標
    mokuhyou_dic = [
        "目標", "目指す"
        ]

    # 行動変化
    hennka_dic = [
        "変革"
        ]

    # 企業活動（対策）
    taisaku_dic = [
        "対策"
        ]
    # O-V 規則
    o_v_taisaku_dic = {"obj": {"対策"},
                      "verb": {"行う"}
                      }

    # 業務提携
    teikei_dic = [
        "提携", "連携"
        ]

    # 採用利用
    riyou_dic = [
        "採用", "利用", "活用", "導入"
        ]

    # 支援
    sien_dic = [
        "支援"
        ]

    # 投資
    tousi_dic = [
        "投資"
        ]

    # 資金調達
    sikin_dic = [
        "資金調達", "債券", "発行", "調達", "増資"
        ]

    # サービス開始
    service_dic = [
        "サービス開始"
        ]
    # O-V 規則
    o_v_service_dic = {"obj": {"サービス", "提供"},
                      "verb": {"開始", "始める", "オープン"}
                      }

    # 生産開始
    seisan_dic = [
        "生産開始", "商業生産"
        ]
    # O-V 規則
    o_v_seisan_dic = {"obj": {"生産"},
                      "verb": {"開始", "始める"}
                      }

    # 商品化
    shouhin_dic = [
        "商品化", "製品化"
        ]

    # 価格変更
    price_change_dic = [
        "価格変更", "値上げ", "値下げ"
        ]
    # O-V 規則
    o_v_price_change_dic = {"obj": {"価格", "料金"},
                      "verb": {"アップ", "ダウン", "変更", "見直し", "上昇", "割引"}
                      }

    # 価格
    price_dic = [
        "価格", "料金" , "費用"
        ]
    # O-V 規則
    o_v_price_dic = {"obj": {"円", "ドル", "ユーロ"},
                      "verb": {"なる"}
                      }
    o_v_price2_dic = {"obj": {"価格", "料金", "費用"},
                      "verb": {"円", "ドル", "ユーロ"}
                      }

    # 人事
    jinnji_dic = [
        "人事", "任命", "解任", "退任", "就任"
        ]

    # 組織
    sosiki_dic = [
        "組織", "設ける"
        ]

    # 組織設立
    seturitu_dic = [
        "組織設立", "敷く"
        ]
    # O-V 規則
    o_v_seturtu_dic = {"obj": {"部", "課", "組織", "チーム", "プロジェクト", "カンパニー", "所", "場", "店", "センター", "ラボ"},
                      "verb": {"新設","発足"}
                      }

    # 組織変更
    sohen_dic = [
        "組織変更"
        ]
    # O-V 規則
    o_v_sohen_dic = {"obj": {"部", "課", "組織", "チーム", "プロジェクト", "カンパニー", "所", "場", "店", "センター", "ラボ"},
                      "verb": {"変更","移行","廃止","改称","統合","刷新"}
                      }

    # 海外展開
    kaigai_dic = [
        "海外展開", "進出"
        ]

    # 設備
    setubi_dic = [
        "設備"
        ]
    # O-V 規則
    o_v_setubi_dic = {"obj": {"所", "場", "店", "センター", "ラボ", "施設", "オフィース", "ビル"},
                      "verb": {"構築", "拠点", "増強", "新設", "着工", "竣工", "建てる"}
                      }

    # 技術背景
    gijyutsu_dic = [
        "技術背景", "伴う"
        ]

    # 社会情勢
    shakai_dic = [
        "社会情勢", "生まれる", "取り組む"
        ]

    # 前提
    zentei_dic = [
        "前提", "踏まえる"
        ]

    # 現象
    gensyou_dic = [
        "現象", "減少", "増加"
        ]

    # 効果
    kouka_dic = [
        "効果", "果たす", "分離", "異なる", "低減", "発揮", "高性能"
        ]

    # 背景
    haikei_dic = [
        "背景", "けん引する", "主流", "格好", "題がある", "迫る", "動き出す"
        ]

##################################################################################




    """
    カテゴリ処理の対象になる格 "副詞的", 
    """
    category_analyze_case = ["を", "に", "にも", "の", "について", "などに", "などを", "なども", "に対して", "に関して",
                          "までを", "も", "にて", "でも", "が", "として", "は", "により", "で",
                          "され", "ましたので", "れましたので", "では", "から", "と"
                          ]

    phrase_rule = [
        {"label": "<意見>", "words": iken_dic},
        {"label": "<見解>", "words": kenkai_dic},
        {"label": "<提案>", "words": teian_dic},
        {"label": "<イベント>", "words": event_dic},
        {"label": "<イベント>", "rule": o_v_event_dic},
        {"label": "<セミナー>", "words": seminar_dic},
        {"label": "<説明>", "words": setusmei_dic},
        {"label": "<紹介>", "words": shoukai_dic},
        {"label": "<議案>", "words": gian_dic},
        {"label": "<会議>", "words": kaigi_dic},
        {"label": "<会議>", "rule": o_v_kaigi_dic},
        {"label": "<対談>", "words": taidan_dic},
        {"label": "<業界情報>", "words": gyoukai_dic},
        {"label": "<予測>", "words": yosoku_dic},
        {"label": "<予測>", "rule": o_v_yosoku_dic},
        {"label": "<市場データ>", "words": shijyou_dic},
        {"label": "<情報公開>", "words": koukai_dic},
        {"label": "<レポート>", "words": report_dic},
        {"label": "<レポート>", "rule": o_v_report_dic},
        {"label": "<政府・行革>", "words": gyoukaku_dic},
        {"label": "<政府・行革>", "rule": o_v_gyoukaku_dic},
        {"label": "<政府・認可>", "words": ninnka_dic},
        {"label": "<政府・認可>", "rule": o_v_ninnka_dic},
        {"label": "<政府・宣言>", "words": sengen_dic},
        {"label": "<政府・宣言>", "rule": o_v_sengen_dic},
        {"label": "<開発>", "words": kaihatsu_dic},
        {"label": "<研究>", "words": kenkyuu_dic},
        {"label": "<実験>", "words": jikken_dic},
        {"label": "<業績>", "words": gyouseki_dic},
        {"label": "<業績>", "rule": o_v_gyouseki_dic},
        {"label": "<戦略>", "words": senryaku_dic},
        {"label": "<戦略>", "rule": o_v_senryaku_dic},
        {"label": "<施策>", "words": sisaku_dic},
        {"label": "<方針>", "words": housin_dic},
        {"label": "<目標>", "words": mokuhyou_dic},
        {"label": "<行動変化>", "words": hennka_dic},
        {"label": "<対策>", "words": taisaku_dic},
        {"label": "<対策>", "rule": o_v_taisaku_dic},
        {"label": "<提携>", "words": teikei_dic},
        {"label": "<利用・採用>", "words": riyou_dic},
        {"label": "<支援>", "words": sien_dic},
        {"label": "<投資>", "words": tousi_dic},
        {"label": "<資金>", "words": sikin_dic},
        {"label": "<サービス開始>", "words": service_dic},
        {"label": "<サービス開始>", "rule": o_v_service_dic},
        {"label": "<生産開始>", "words": seisan_dic},
        {"label": "<生産開始>", "rule": o_v_seisan_dic},
        {"label": "<商品化>", "words": shouhin_dic},
        {"label": "<価格変更>", "words": price_change_dic},
        {"label": "<価格変更>", "rule": o_v_price_change_dic},
        {"label": "<価格>", "words": price_dic},
        {"label": "<価格>", "rule": o_v_price_dic},
        {"label": "<価格>", "rule": o_v_price2_dic},
        {"label": "<人事>", "words": jinnji_dic},
        {"label": "<組織>", "words": sosiki_dic},
        {"label": "<設立>", "words": seturitu_dic},
        {"label": "<設立>", "rule": o_v_seturtu_dic},
        {"label": "<組織変更>", "words": sohen_dic},
        {"label": "<組織変更>", "rule": o_v_sohen_dic},
        {"label": "<海外進出>", "words": kaigai_dic},
        {"label": "<設備投資>", "words": setubi_dic},
        {"label": "<設備投資>", "rule": o_v_setubi_dic},
        {"label": "<技術背景>", "words": gijyutsu_dic},
        {"label": "<社会情勢>", "words": shakai_dic},
        {"label": "<前提>", "words": zentei_dic},
        {"label": "<現象>", "words": gensyou_dic},
        {"label": "<効果>", "words": kouka_dic},
        {"label": "<背景>", "words": haikei_dic}
    ]

    # 補助述部でも政府活動と認めるカテゴリのルール
    sub_phrase_rule = [
#        {"label": "", "words": }
    ]

    """
    時制に関する補助用言
    """
    kako = [""]
    genzai = [""]
    mirai = ["予定", "計画", "目指す"]
