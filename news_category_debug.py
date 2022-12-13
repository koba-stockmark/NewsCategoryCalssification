from news_category_classification import CategoryClassification

ncc = CategoryClassification()

text = "脱炭素社会の実現に向け、一定規模以上の建物を新築・増改築する際に太陽光発電などの再生可能エネルギーの設置を義務化する自治体が広がりつつある。\n東京都と群馬県は２月に設置義務化に向けた条例案を議会に提出する。\n可決されれば、京都府、京都市に次ぐ事例となり、大企業はもちろん中小企業も対応を迫られることになる。\n"

text = "三菱ケミカル株式会社（本社：東京都千代田区、社長：和賀 昌之、以下「当社」）及びその連結子会社である三菱ケミカルメタクリレーツ株式会社（本社：東京都千代田区、社長：佐々木 等）は、植物由来原料を使用するMMA（メチルメタクリレート）モノマーの製造技術を開発し、この度、パイロットプラントの設計に着手したことをお知らせします。"


# ニュースのカテゴリ分類のチェック
government_phase = ncc.news_category_classification(text)
print(government_phase)