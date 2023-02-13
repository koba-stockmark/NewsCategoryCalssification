from news_category_classification import CategoryClassification

ncc = CategoryClassification()

text = "脱炭素社会の実現に向け、一定規模以上の建物を新築・増改築する際に太陽光発電などの再生可能エネルギーの設置を義務化する自治体が広がりつつある。\n東京都と群馬県は２月に設置義務化に向けた条例案を議会に提出する。\n可決されれば、京都府、京都市に次ぐ事例となり、大企業はもちろん中小企業も対応を迫られることになる。\n"

text = "三菱ケミカル株式会社（本社：東京都千代田区、社長：和賀 昌之、以下「当社」）及びその連結子会社である三菱ケミカルメタクリレーツ株式会社（本社：東京都千代田区、社長：佐々木 等）は、植物由来原料を使用するMMA（メチルメタクリレート）モノマーの製造技術を開発し、この度、パイロットプラントの設計に着手したことをお知らせします。"

# 主語なし
text = "製油所をバイオ燃料や化学品原料の生産拠点といわば再定義し、廃プラ由来合成油を原料とする「再生可能化学品」などの供給拠点とする。"

text = "世界で広がる脱炭素の動きを背景に、日本や欧米、中国、韓国などを中心に燃料電池車（FCV）やトラック・バスの普及が市場をけん引するとみる。"
text = "世界的な不動産サービス会社は、「野心的な」持続可能性への取り組みを実現し、不動産がネットゼロの目標を達成できるよう支援するために、AlexandraIngramを任命しました。"
text = "繊維・ファッションが持続可能な産業になるために黒衣として支える商社ができること、果たすべき役割を経営トップに聞いた。"
text = "２０５０年までに二酸化炭素（ＣＯ2）排出量実質ゼロを目指す方針を掲げ、市民と事業者、行政が一丸となり、再生可能エネルギーの利活用やライフスタイルの変革、ごみ減量などを推進するとしている。"
text = "JFEスチールと東北大学は、カーボンニュートラル時代を見据えた研究活動の推進を目指し、共創研究所を1日付で設けた。"
text = "産学連携体制のもと、企業技術者と大学研究者の部門横断的な連携を通じて、低炭素製鉄プロセスに関する共同研究をさらに加速させるとともに、新材料開発をはじめ新規開発テーマの発掘を推進する。"
text = "この度、欧州系グローバル戦略コンサルティングファームのローランド・ベルガーと、無形資産/ESG等のデータ解析・可視化企業のアスタミューゼは、日本の脱炭素に貢献するスマートモビリティ領域に関する分析レポートの第2回を発表いたします。"
text = "信越化学工業は2月16日、シリコーン製品の生産能力を増強すると発表した。"
text = "信越化学工業株式会社（本社：東京、社長：斉藤恭彦 以下「信越化学」）は、主力事業の一つであるシリコーン事業で８００億円を超える設備投資を行い、同事業をさらに拡充します。"
text = "信越化学は、2018年9月に発表しましたシリコーン事業における1,100億円の投資計画で、中間原料であるシリコーンモノマーを日本とタイの2拠点で生産能力を増強し、従来比で約1.5倍の能力増としました。"
text = "信越化学工業株式会社（本社：東京、社長：斉藤恭彦 以下「信越化学」）は、主力事業の一つであるシリコーン事業で８００億円を超える設備投資を行い、同事業をさらに拡充します。"
text = "旭化成メディカル株式会社（本社：東京都千代田区、社長：住吉 修吾、以下「当社」）は、ウイルス除去フィルター「プラノバ™」および「プラノバ™ BioEX」の需要急増に対応して、供給体制を強化するため、宮崎県延岡市に新たに組立工場を建設することを決定しましたので、お知らせします。"
text = "液晶ポリマー（LCP）フィルムおよびラミネート市場の 見通しは非常に有望に見え、ビジネスストラテジストにとって洞察に満ちたデータの貴重な情報源です。"
text = "業界の概要と、成長分析、過去および未来のコスト、収益、需要と供給のデータ（該当する場合）を提供します。"
text = "クラレグループのクラレプラスチックス（大阪市北区）は、熱可塑性エラストマーコンパウンド「アーネストン」を紹介する新サイトを2月3日付でオープンした。"
text = "クラレグループのクラレプラスチックス（大阪市北区）は、熱可塑性エラストマーコンパウンド「アーネストン」を紹介する新サイトを2月3日付でオープンした。"
text = "ベトナムの高炉メーカー、フォルモサ・ハティン・スチール（ＦＨＳ）は、３～４月出荷分の熱延コイル販売価格を前月から９０ドル引き上げ、トン当たりＣＩＦ８４０ドル程度とすることを取引先に伝えた。"
text = "同社は今年度から新・マネジメント体制に移行するとともに、新・経営理念（パーパス、バリュー）を始動している。"
text = "沢井製薬が骨粗鬆症治療薬「テリボン」の後発医薬品を市場に投入することが15日、明らかになった。"
text = "同日付で厚生労働省から製造販売承認を取得しており、6月の薬価追補収載を目指す。"
text = "本セミナーでは、実稼働バッテリーシステムのモニタリングのためのインピーダンス測定がどうあるべきかについて考えます。"
text = "ビー・エム・ダブリューは2月16日、新型電気自動車（EV）『i4』を日本発表した。"
text = "価格は750万円からとなっている。"
text = "青森市のIT企業「フォルテ」（葛西純代表取締役）は15日、インドの部品メーカー「Nash　Industries」と合弁会社を設立し、インドでリチウムイオン電池の生産工場を運営する方針を明らかにした。"
text = "電気車(EV)バッテリーと水素などエコ技術エンジニアリング専門企業である「SKエコエンジニアリング」が15日、公式に発足した。"
text = "ビー・エム・ダブリューは2月16日、2022年ビジネス・ストラテジーおよび新型電動モデル発表会を開催する。"
text = "本セミナーでは、昨今の市場動向を踏まえ、「プロセス産業はどのように気候変動対策を行うべきか」について、実現方法を交えたクロス・トークをお聞きいただけます。"
text = "売上高は前年比46％増の1兆4196億円、営業利益872億円（同1066億円増）、経常利益869億円（同1308億円増）、純損失121億円（同642億円改善）となった。"

# の格　の直後に名詞があり、の格が動詞にかかっている場合はかかり受けの修正が必要
text = "民間に比べ遅れていた医療機関の働き方改革がようやく動き始めた。"

text = "コロナ下で株価は上昇基調だが、足元ではいくつか不安要素も出ている。"
text = "ヤマハや河合楽器製作所、ローランドなど、浜松市に拠点を置く企業を中心に、企業が競い合い、大人も満足できるデザイン性や音質を追求してきたことも人気の要因です。"
text = "帝人子会社のインフォコムで、この改革を支えるシステムの販売を担当するのが井上和人さんだ。"
text = "2020年6月に社長に就いた錦織弘信は、事業売却により富士通から東芝に移った経歴を持つ。"
text = "プライム、コード6141）DMG森精機が大幅に続伸している。前日比65円（3.7%）高の1826円を付けた。"
text = "日本マクドナルドは一時休止していたフライドポテトのM・Lサイズの販売を31日から再開する。"
#text = "国連の第26回気候変動枠組み条約締約国会議では、気候資金が争点の一つになった。"
#text = "パナソニックは30日、2022年1月に米ラスベガスで開催する技術見本市「CES2022」で予定していた記者会見を、オンラインのみでの実施に切り替えると明らかにした。"
#text = "ブース展示は実施する見通し。"
#text = "後発医薬品の供給混乱が長期化している。"
#text = "事態の打開へ、厚生労働省もメーカーに供給増などの対応を取るよう要請を始めた。"
#text = "29日の東京株式市場で日立製作所株が前日比66円安の6196円で取引を終えた。"

#text = "米中のはざまで日本企業はどう対応すべきか。"
text = "長引く新型コロナウイルス禍で営業赤字幅は想定より拡大するが、営業時間の短縮要請に伴う時短協力金57億円が利益を押し上げる。"
text = "ラーメン店「日高屋」を運営するハイデイ日高は29日、2022年2月期の単独税引き損益が17億円の黒字になる見通しだと発表した。"
text = "中国民営自動車大手の浙江吉利控股集団は29日、米アルファベットの子会社で自動車運転技術の開発を手掛ける米ウェイモの自動運転タクシー向けに専用の電気自動車を供給すると発表した。"
text = "吉利はウェイモとの連携をテコに米国の自動運転分野の先進技術を吸収するとともに、米国事業の拡大をめざす。"
text = "読者の評価が高かった記事やアクセスが多かった記事から今年の10本を選んだ。"
text = "17年に始まったガス小売り自由化により、電力会社など異業種が都市ガス事業に参入した。"
text = "12兆円にも達すると言われる市場をめぐる個人と企業の動きについてまとめました。"
text = "東京五輪でスケートボードの初代金メダリストになり、自らを動画撮影好きの「クリエーター」と認める堀米雄斗選手のインタビュー動画も、あわせてご覧ください。"

text = "五反田はオフィス賃料の低さや周辺の暮らしやすさが魅力の半面、会社が大きくなり渋谷や都心へ移るまでのステップにもされがちだ。"
text = "経営再建中の中国半導体大手、紫光集団の債権者会議が29日に開かれ、事業継承先に投資ファンド2社を中心とする連合を選ぶ再建案を承認した。"
#text = "傘下に入ることが決まった。"

# ginzaとja_ginza_electraの違い
text = "LINEタイ法人によると台湾のみでサービスを続けるが、その他の国・地域からは撤退する。"

text = "日本経済新聞が集計したところ、大手電力9社中5社で電子に移行した顧客の比率が3割以下にとどまった。"
text = "企業はコーポレートガバナンス・コードで株主と向き合うことを求められ、株主である投資家もスチュワードシップ・コードで企業価値向上につながる行動を求められる。"
text = "実家の母や兄と食事をしながら「新しい会社の名前をどうしようか。マルチメディアのようなかっこつけたものでなく、直球がいいのだけど」と問うと、兄の元道が「スマイル」を口にしたのです。"
text = "特にIoT、人工知能の活用だった。"

text = "積み重なる段ボールや使い捨て容器に嫌悪感を覚えることはないだろうか?"
text = "まとめて配送することで配送時の二酸化炭素排出も減らせる。"
text = "2021年はESGを重視する企業や投資家の行動が資金調達にも大きく影響した。"
text = "新型コロナウイルスの影響で客が減ったうえ、原材料価格の高騰や人材難などの悪条件が重なったことが響いたようだ。"
text = "血液検査など臨床検査受託で国内最大手のH.U.グループホールディングスは2022年1月4日、東京都あきる野市で巨大な検査拠点を稼働させる。"
text = "麦類や酪農などが前年を軒並み上回り、21年までの目標値としていた3500億円を大幅に超えた。"
text = "12月13日付で品種登録された。"
text = "食べれる。勉強できる"
text = "香川県農業試験場が育成した紫色のアスパラガス「さぬきのめざめビオレッタ」が12月13日付で品種登録された。"
text = "「さぬきのめざめビオレッタ」は他の紫色の品種に比べ、着色が不安定になりやすい夏場でも紫色が鮮やかという特徴があり、香川県は競争力を発揮してほしい"
text = "香川県は太く長い特徴を持つ緑色のアスパラガス品種「さぬきのめざめ」と合わせ、「さぬきのめざめ」シリーズとして県産野菜のブランド力強化につなげる。"
text = "住宅大手のオープンハウスは、スキー場運営に参入した。"
text = "グループ会社のみなかみ宝台樹リゾートが「群馬みなかみほうだいぎスキー場」をオープンした。"
text = "同社によれば、同スキー場はみなかみ町の中でも標高が高く積雪量が豊富なため、世界レベルのパウダースノーが楽しめるという。"
text = "冬のリフォーム需要を目前に住設機器の納期遅れが深刻化している。"
text = "TOTOは温水洗浄便座の納期が1~2カ月ほど遅れるほか、YKKAPでも高断熱窓の納期が1カ月弱遅れる。"
text = "遅れる。食べれる。早める。楽しめる、愉しめる。食べれる。食べられる。読める。調べる。調べれる。"
text = "ENEOSと実証プラント建設しリサイクル技術確立へ"
text = "売電量３年で２.８倍　脱炭素へ契約社増　とちぎふるさと電気"
text = "脱炭素と事業成長を両立　「移行計画」が不可欠に"
text = "空気中のCO2 直接回収　日本ガイシ、25年にも実験"
text = "CO2排出削減へ企業に課金　政府、GX債の償還財源に"
text = "タイに本拠を置く「再生可能エネルギー」のリーディング企業である CKPower は、2050年までに排出量ネットゼロを目標にします"
# スペース区切りには　。　を入れる
text = "再エネ使ったインド産「グリーンアンモニア」を発電所に販売。　興和、令和１０年度から"

text = "スマートシティとは？ 千葉市スマートシティ推進ビジョンを例に解説"
text = "電動バイクのウソとホント「音がしない」「加速が鈍い」「高価」「航続距離が短い」のイメージは真実なのか（モーサイ）"
text = "メルセデス・ベンツ、F1技術採用のAMG新型発表"
text = "BMW「5シリーズ」次期型「ツーリング（ワゴン）」導入確定！「M5」にも期待!!"
#text = "スズキ「Hayabusa GP EDITION」 MotoGPマシン「GSX-RR」をイメージした特別仕様車登場"
#text = "奇抜系スクーター、ドラッグスターが450ccに進化！しかもMT仕様！。イタルジェット・ドラッグスター500GP登場【EICMA2022】"
#text = "【試乗レポート】新型「CX-60」公道初試乗。マツダの新時代を築くラージアーキテクチャ第1弾の仕上がりはいかに？"
#text = "ＥＶ駆動部品を小型化。アイシン試作、電力効率向上：地域ニュース"
#text = "【ボルボ XC40 / C40 試乗記】ラインアップ追加で新たなユーザー層もくすぐるBEVに"
#text = "EVシフト全盛の時代に直6ディーゼル車で勝負する…ついに始まってしまったマツダの超逆張り戦略（プレジデントオンライン）"
#text = "グラフェンの光検出器としての有望性を実証、ゼロバイアス動作で世界最速を実現"
#text = "プロトタイプ向け切削材料で射出成形品が存在感 - 化学工業日報"
#text = "炭素原子膜グラフェンに含まれる微量元素量の計測に成功。ドーピングによるグラフェン機能制御へ大きな進展！"
#text = "韓国車の上半期世界シェアが下落＝韓国ネット「好調なのは中国だけ」「国家競争力が奈落に…」"
text = "イメージは真実なのか？（モーサイ）"
text = "日産、スズキが3～4割の大増収に業績上方修正！半導体不足による減産下で抗えた要因は？"
text = "ＴＳＭＣがアリゾナで第2の工場建設へ、投資総額は400億ドル"
text = "EdgeTech＋2022　NECグループ出展のご案内"
text = "スタートアップ開発環境マップ x 19社（10/22開催Coral Careers 2022 Fall参加企業版）"
text = "Chainy（チェイニー）：皮膚に感覚を伝える、椅子型触覚提示装置 | 知財図鑑"
text = "人の暮らしにやさしいIoTデバイスや地域・企業のDXを促進する多数の先端テックが展示"
text = "次世代多孔性炭素材料を合成する"
text = "中国におけるリチウムイオン電池用電解質リチウム塩製造会社への出資について"
text  = "活躍が広がるシャープのAI×IoT「AIoT」、新たな機能「もしもの家電」とは？‐CEATEC2022"
text = "パーキンソン病患者を対象としたBIIB122の有効性及び安全性を評価する多施設共同無作為化二重盲検プラセボ対照第IIb相試験"
text = "【オーストリア】アルプラ、再生高密度PEのみ使用の美容品容器プロトタイプ発表。CO2を71%削減 | Sustainable Japan | 世界のサステナビリティ・ESG投資・SDGs"
text = "エンビバが重工業分野における最新のバイオエネルギーの進化に関する白書を発表"
text = "YKK AP 等級6、7に対応の大開口窓を発表"
text = "企業と就活生がWin-Winの関係に！“迷走人事”を助ける情報サービス「ダシトレ」とは？"
text = "100度台でCO2をCOへ転換可能に"
text = "世界最大級の製造能力を持つメタネーション装置を受注"
text = "多孔質ナノ粒子の配列・配向制御"
text = "ADASやEVなど、自動車の電子化を支える電子部品とは"
text = "三菱総合研究所、阪急三番街で実証開始　環境配慮行動を促進アプリにデジタル地域通貨サービス「Region Ring®」を提供 | 三菱総合研究所（MRI）"
text = "広がるスマート工場化、今こそ工場ネットワークを整備しなければならない理由"
text = "データサイエンティスト×ブリヂストン DX人材が創出する新たな価値 デジタルAI・IoT企画開発部 デジタルAI開発課　武富 尚吾"
text = "自宅療養者と医療機関を“マッチング” 24時間オンライン診療や往診が受けられるセンター設置　大阪府（関西テレビ）"
text = "小児向けオンライン健康相談アプリ『キッズドクター』、オンライン診療サービスの年末年始特別営業を実施"
text = "「－１９６℃ ストロングゼロ〈みかん＆伊予柑〉」期間限定新発売"
text = "キリン｢高単価ビール苦戦｣で早くも迎えた正念場"
text = "コロナ新薬「エバシェルド筋注」、「かかりつけ以外の患者」への接種にあたり、かかりつけ医へ診療情報提供を求めて良い―厚労省"
text = "手羽先が美味しい居酒屋「酔っ手羽」恵比寿店、五反田店、船橋店　昼のみ大歓迎！『予約限定 平日０次会プラン』10月7日（金）登場"
#text = "【40代女性が選んだ】「家でハイボールを作るのにオススメのウイスキー」ランキング！　第1位は「角瓶」！（ねとらぼ）"
#text = "キユーピー首位　消費者のブランド評価、革新商品に期待"
#text = "新しいマーケティングのすすめ（17） - 知るギャラリー by INTAGE"
text = "OKIエンジニアリングが全固体電池の信頼性評価、セラミックコンデンサーとの類似性に着目 | 電波新聞デジタル"
text = "世界半導体市場、2023年上半期にかけて調整期間へ"
text = "迫力のスクリーンを目の前に！ 話題のAR技術が体験できる『Rokid Air ARグラス』をおためし"
text = "新型ウォッチ「OnePlus Nord Watch」スペックや外観がリーク"
text = "半導体不況は長期化も、サムスン電子とSKハイニックスは需要反転に備え"
text = "シャープが効率32.65％の化合物3接合型太陽電池、HAPS搭載を念頭"
text = "次世代電池の開発の裏に実験ロボットとAIの躍進あり"
text = "世界スマホ出荷、アップルのみプラス成長　7～9月期 | JDIR"
text = "減産と原材料高騰が重荷、ホンダ系部品メーカーが模索する“ホンダ以外” ニュースイッチ by 日刊工業新聞社"
text = "ＥＶ生産、インセンティブ不足で低迷か EU・自動車・二輪車"
text = "米国政府の対中半導体規制強化の中国半導体ユーザーへの影響をTrendForceが分析"
text = "米、EVに搭載の電池生産に補助金交付　「脱中国」加速を図る | 毎日新聞"
text = "三菱『ミニキャブ・ミーブ』が復活！国内メーカー唯一の軽商用EVが再び!（WEBヤングマシン）"
text = "現代自、ハイブリッドカー生産台数15%増へ"
text = "凸版印刷、物流DX推進に向けてモノフルの物流エコシステムへ参画"
text = "いよいよ始まった物流のパラダイムシフト ～異業種間連携で挑む脱炭素化向けた物流の未来～"
text = "「蓄電所」ビジネスが本格始動、再エネ移行の鍵握る－新規参入相次ぐ"
text = "【バイオアジピン酸】東レ、世界初 非可食バイオマスを原料とする糖からナイロン原料を創出"
text = "Ｇ７企業の排出削減目標、パリ協定の目標に未達＝民間調査"
text = "LG化学、アンモニア基盤の清浄水素バリューチェーン推進"
text = "出光興産ら4社/脱炭素でアンモニア供給/国内初の年間100万t体制"
text = "「遠い脱炭素」電力確保に悩むデータセンター事業者"
text = "エネルギー不足に動揺、中国が石炭生産を増加―仏メディア"
text = "風力エネルギー業界が警告：COP27に先立ち、エネルギー安全保障と気候変動危機に対処するため、各国政府は言葉ではなく行動を取るべきだ"
text = "CO2排出量 “見える化”の動き 製品の原材料調達から廃棄まで | NHK"
text = "航空機の脱炭素化に必須、次世代燃料「SAF」関連5銘柄（会社四季報オンライン）"
text = "ヤマハ発動機とCNF強化樹脂の用途開発に関する連携を開始｜ニュースリリース｜日本製紙グループ"
text = "プロトタイプ向け切削材料で射出成形品が存在感 - 化学工業日報"
text = "【ボルボ XC40 / C40 試乗記】ラインアップ追加で新たなユーザー層もくすぐるBEVに"
text = "脱炭素社会への切り札 SiCパワーデバイスについて解説（材料編）｜inrevium"

text = "手羽先が美味しい居酒屋「酔っ手羽」恵比寿店、五反田店、船橋店　昼のみ大歓迎！『予約限定 平日０次会プラン』10月7日（金）登場"
text = "不動産業界初（※1）となるARアプリ「Finding Serendipity by LIFULL HOME'S」のパブリックテストを実施"
text = "ビジネス展示会「Meet XR」ブース紹介：第3回～ハードウェア企業さらに続々"
text = "Apple、NFCチップやカメラへの他社のアクセスも認める!?"
text = "量子コンピュータについて（ChatGPTが書きました）｜IT navi｜note"

text = "TDKが車載用150度対応のパワーインダクター　シールド機能に金属磁性材料　高い直流重畳特性 | 電波新聞デジタル"
text = "世界の人口が80億人に 2050年カーボンニュートラルが急務 | 原子力産業新聞"
text = "海洋中のプラスチックごみ問題について｜泉南市ホームページ"
text = "「ユーロ７」はまるで全体主義 ICE（内燃機関）は本当に存続の危機なのか・その２（MotorFan）"
text = "石油・ガス世界大手「OGCI」、海運団体と大規模な船上CO2回収実証プロジェクトに着手(米国、スウェーデン)"
text = "日鉄溶接工業　フラックス入りワイヤ　6―9％Ni鋼に最適化"
text = "漁網由来のケミカルリサイクル繊維製品の販売開始について"
text = "マイクロ波・ミリ波分野の主要国際学会で最優秀論文賞を受賞"
text = "矢野経済研究所、人工光合成の世界市場に関する調査結果を発表"
text = "京都大学などが「安全で柔軟な」ポリマー系固体電池、電池討論会で発表"
text = "TSMCが12月29日に台南Fab 18で3nmの量産開始式典を開催予定、台湾メディア報道"
text = "11月30日（水）より「DIGITAL TWIN Conference 2022」をオンライン開催"
text = "ＥＶ電池の品質保証サービス事業化に向けた実証を開始。～中古ＥＶの価値適正化により、ＥＶ市場拡大と電池循環市場形成に貢献～"
text = "使用済みのプラスチック製ペンの「水平リサイクル」実証プロジェクトを開始"
text = "楽天エナジー、家庭用蓄電池の販売・運用を行う「楽天ちくでんち」を開始"
text = "【森永乳業】物流資材において、社内プラスチック資源循環を開始"
text = "村田の部品を使用した新しいアイデア広く募集。村田製作所が共創プロジェクト開始。|。電波新聞デジタル"
text = "カネカ、生分解プラの原料多様化、廃食油利用で実証。。。化学工業日報"
text = "明治保有の乳酸菌が小腸上皮様細胞を用いたモデル系で。腸管バリア機能を強めることを確認"
text = "チューリング社、千葉県で法人向けに自動運転車の試乗会を開始"
text = "リユースした電動車用バッテリーで大容量スイープ蓄電システムを構築し、電力系統への接続を含めた運転を開始。|。コーポレート。|。グローバルニュースルーム。|。トヨタ自動車株式会社。公式企業サイト"
text = "開発中のインスリン錠剤の有望性を動物実験で確認"
text = "株式会社ファイン、大阪国際大学との共同研究にてプロテインとファイン独自成分リキニンの同時摂取による骨格筋量、筋肉量、基礎代謝量への有意な値を確認"
text = "マツキヨココカラ／海洋プラスチックごみ問題解決に向け団体加入"
text = "2050年のカーボンニュートラル実現に向けた都市ガス業界の取り組み"
text = "自動車由来のプラスチック部品リサイクル、新装置導入で「廃プラスチックの資源循環高度化事業（経済産業省）」に採択！！"
text = "インド、半導体産業を育成。米中対立に商機狙う"
text = "産総研、セシウム原子泉時計と光格子時計でダークマターの探索領域を拡大。"
text = "COMSOL Multiphysics®。バージョン6.1をリリース"
text = "CCS（CO2の回収・貯留）のサプライチェーン構築に関する検討・調査を3社共同で実施"
text = "幕張メッセ「第2回XR総合展[秋]」にて、メタバース×ブロックチェーン。ソリューションの体験会を実施"
text = "JVCKW、冶金工、メルカリなど／本日の注目個別銘柄。| 。財経新聞"
text = "新たなフロントデザインへ進化！新型BMW Z4が発売、Amazon Alexaを搭載"
text = "双日プラネットとANAグループが航空貨物用プラスチックフィルムのリサイクルにおける資源循環型スキームを構築"
text = "国内最大のグリーン水素施設新設。再エネから、山梨県とサントリー合意"
text = "ローム、20V耐圧nチャネルMOSFETの量産開始"
text = "データ収集、検証、文書化、配布のプロセスをクラウド上で自動化。ー。EDITROOMリリース。|。東洋経済オンライン"
text = "凸版印刷、JAREC、放電精密の3者で高度マテリアルリサイクル研究会を設立"
text = "MYCITY・パナソニックエレクトリックワークス社。空間価値創出で新会社設立。。|。住宅新報web"
text = "韓国&米国のスタートアップサミット2022がニューヨークで開催"
text = "【プレスリリース】格子体積が変化しないバナジウム系高容量電池材料~実用的な全固体電池実現に前進"

text = "東大、知的財産活動の開示へ着手 国内大学初"
text = "芝浦工業大学  ×   株式会社LiNew　 LiDARで学習効果を予測する技術の共同研究に本格着手"
text = "『機械学習のデータラベリングを自動化する』というテーマのウェビナーを開催"
text = "ウシオ、大阪大学の「メタンガスのギ酸・メタノール化」の共同開発研究へ参画"
text = "【BtoBマーケ担当者向け】「これからのBtoBビジネスの在り方 3社の役員が語る事業拡大戦略」をテーマに、「FanGrowth」が2023年1月24日（火）よりウェビナーを開催"
text = "京セラ､中期計画の作成に初めて着手した事情"
text = "【ライブ配信セミナー】硫化物系固体電解質の量産技術　12月1日（木）開催　主催：(株)シーエムシー・リサーチ"
text = "オックスフォード・インストゥルメンツ、10/5（水）「MapSweeper - EBSD最新パターンマッチング技術」ウェビナー開催"
text = "【事業企画・経営企画部門向け】ウェビナー再開催！「これからのオープンイノベーション / M&A戦略 ～世界の知的＆投資情報×自社の無形資産による共創戦略の構築～」"
text = "株式会社ナビットは、11月16日（水）～11月29日（火）まで「【売上300%UPの事例紹介】インフルエンサー活用セミナー～Instagram徹底解説～」を2週間限定配信いたします。"
text = "【2022 年 12 月 15 日（木）13︓00～14︓00 開催】リスキリング支援サービス『学びのコーチ』事業責任者の柿内、『doda』主催のオンラインセミナーに登壇"
text = "ドルンビルン国際繊維会議で講演＝米ライクラ〔ＢＷ〕：時事ドットコム"
text = "SPA化するMPAとMPA化するSPA ～TechFeed Experts Night#4 講演より"
text = "【キーワード・30秒解説】持続可能な航空燃料（ＳＡＦ） ニュースイッチ by 日刊工業新聞社"
text = "ReVision コネクテッドカー＆UXサミット2022：日立製作所、トヨタ紡織の講演より - 自動車産業ポータル マークラインズ"
text = "凸版印刷、JAREC、放電精密の3者で高度マテリアルリサイクル研究会を設立"
text = "チューリング社、千葉県で法人向けに自動運転車の試乗会を開始"
text = "中国が初の1000万トンのCCUSプロジェクトを開始、中国東部の産業企業向け脱炭素化ソリューションを探究"

text = "【PETのケミカルリサイクル】日揮HD・帝人・伊藤忠商事、ライセンスを目的とした合弁事業会社。RePEaTを設立"
text = "先端技術への挑戦【技術事業開発本部】。みずほリサーチ&テクノロジーズ"
text = "「輝き」という名の美容クリームがお得プライスで手に入るチャンス！『イオナR。ラディアンスクリーム』発売1周年記念キャンペーン"
text = "「今どっちの足で部屋に入った？。。」JAL社長が恐怖、稲盛和夫氏が謎の問いをした訳"
text = "上値が重い小野薬品、「ポストオプジーボ」の具体化が必要"
text = "人工生殖細胞で変わる。子どもの作り方。「火の鳥」の世界に近づくか"
text = "EVユーザー「次に買うクルマもEV」何割？。。。ガソリン自動車に戻す人も。全国調査で明らかに。| Merkmal"
text= "光周波数コムを用いた光フェーズドアレイ"
text = "リアルワールドデータを用いて体格指数（BMI）と心房細動アブレーションの安全性との関連を解析。プレスリリース。広報活動。国立循環器病研究センター"
text = "プラズモンを用いたエネルギーアップコンバージョン。未使用エネルギー赤外光の活用方法に道。"
text = "RetiSpec社。–。網膜検査をアルツハイマー病診断に用いるAI技術。|。医療とAIのニュース・最新記事。。 The Medical AI Times"
text = "日本版DVG/DiGAの誕生で、医療AIやSaMDに大波到来となるか。"
text = "〈社説〉ＣＯ2貯留。脱炭素化の柱になるのか"
text = "スマートホームの旗振り役にIoTで暮らしはより面白さがある"
text = "モーンガータ、廃棄化粧品を印刷用技術へ応用する。新たなアップサイクルの取り組みを開始"
text = "グーグルの3Dビデオチャット「Project Starline」を体験。。目の前にいるような臨場感"
text = "『ディスクロニア。。CA』エピソード1を先行レビュー。VRで実現した“未来の犯罪捜査”はSF好きにはたまらない至高の体験に！"
text = "EVの充電が10分でできる新技術誕生。中国メディア"
text = "水素調理器や商用水素発電所など続々誕生。「日本初」の水素技術"
text = "愛知の車部品、脱炭素に注力。多様な手段で環境対応"
text = "アルナイラム、ＲＮＡｉ薬、年内にも投入。。。化学工業日報"
text = "XRディスプレー市場、30年に1.2兆円規模へ。2022/9/29(2517号)主なヘッドライン。by。電子デバイス産業新聞"
text = "キラル金ナノ粒子アレイによる分子のキラリティーの検出"
text = "【戦略】「自分の強み×デジタル」で新たな武器を見つけよう"
text = "石油化学業界が国際化に動く中、AIアップグレードの経験を共有するため石油化学企業が集結"
text = "上値が重い小野薬品、「ポストオプジーボ」の具体化が必要"
text = "【リアル調査】手が老けていると実年齢より上に見える？ 女性の老化を感じる体のパーツは1位「顔」、2位「手・指・爪」。96％の女性が必要と感じる“手のエイジングケア”..."
text = "3次元測量アプリで点群データから平面図作成が容易になるアップデート - オプティム"
text = "【国際】上場大手より非上場大手の方がカーボンニュートラルにかなり消極的。Net Zero Tracker | Sustainable Japan | 世界のサステナビリティ・ESG投資・SDGs"
text = "新たなフロントデザインへ進化！新型BMW Z4が発売、Amazon Alexaを搭載（WEBヤングマシン）"
text = "SiCデバイス＆ウエハー、増産計画が続々と具体化｜2022/12/15(2528号)主なヘッドライン by 電子デバイス産業新聞（旧半導体産業新聞）"
text = "三重大Ｒナビ -三重大学の研究最前線-|酸性泉に適応した光合成細菌のタンパク質進化"

text = "米エヌビディア、8～10月は17％減収。|。電波新聞デジタル"
text = "世界のＣＯ２排出量、今年は1％弱増。ＥＶ普及などで。ＩＥＡ"
text = "インドネシア、2025年に再エネ比率23％へ"
text = "Samsung、2023年のスマートフォン出荷台数は13%減少見込み"
text = "太陽誘電、下期のコンデンサー工場稼働率70％"
text = "建設現場で使う電力も100％再生可能エネルギーに"
text = "廃プラから燃料代替油、いわきの企業が実証事業。生成効率は95％"
text = "「霧」のような半透明の65%メカニカルキーボード"
text = "ワークマン、巧みなマーケティング戦略で広告宣伝費率は驚異の0.8％。高機能×低価格が可能にした｢非常識経営｣"
text = "ホットストック。機械株が堅調、Ｊマテリアル4％高。堅調な設備投資計画を好感"
text = "韓国エプソン、プロジェクターでシェア１位。。 NNA ASIA・韓国・電機"
text = "アニサキスの心配なし！海なし県発「温泉サバ」。神川で挑戦１年、全滅の悲劇越え出荷へ。今後はイベントも"
text = "パナソニック、掃除機など120品目値上げへ。最大45%"
text = "歯や口の悩み、若年層は「見た目」がトップ。10代の2人に1人が口腔の問題を経験"
text = "自動車メーカーのＥＶ・電池支出計画倍増、30年までに1.2兆ドル"
text = "三井物産、CO2地下貯留整備。アジアなどで年1500万トン"
text = "NTTドコモ、2段階定額光ブロードバンド「ドコモ光ミニ」を2025年3月31日に終了。新規申込受付は2023年3月31日終了"
text = "水素活用で新技術。東芝、レアメタル1割に。「P2G」前進。|。電波新聞デジタル"
text = "米エヌビディア、8～10月は17％減収。|。電波新聞デジタル"
text = "1剤で売上1兆円超えも。イチからわかる"
text = "リアルなニセモノ画像を大量生成、ピッキングや検査のAI構築を1日で"
text = "「ＣＣＳ市場の特性と事業機会」と題して株式会社三菱総合研究所。サステナビリティ本部。気候変動ソリューショングループ。主任研究員。野本。哲也氏のセミナーを2022年11月..."
text = "オリジナルスタイルをキープしつつフルカスタムのGSX1100S。カタナ"
text = "米エヌビディア、8～10月は17％減収。|。電波新聞デジタル"
text = "「ドゥカティのバイク」人気車種ランキングTOP10！。1位は「スクランブラーSIXTY2」【2022年10月版／グーバイク調べ】。。"
text = "自動車OEM向けのLSLiDARイメージグレード1550nm LiDAR「LSシリーズ」が発売開始－自動車の安全性を新たな高みへ"
text = "【.biz。】。。。日立、GPUなしでAI処理可能なPower10プロセッサ搭載サーバー"
text = "「原発に1兆円」アメリカの強い意志。大西康之"
text = "出光、次世代エネルギーに1900億円。25年度までの中計"
text = "出光、次世代エネに1900億円"
text = "「Microsoft×教育改革」「ベネッセ×DX人材育成」など18講演！まもなく。【オンラインラーニングフォーラム2022。本日最終日】。。※旧。eラーニングアワードフォーラム"
text = "AI自動翻訳のロゼッタ。ウェビナー『自動車生産現場のAI翻訳活用。～海外拠点とのスピーディな情報共有で進むグローバル・コミュニケーション～』11月21日(月)開催"
text = "テスラの新型SUV｢Model Y｣パフォーマンス試乗レポ…2022年を代表する1台だ"

text = "EU／意図された医療目的のない医療機器を規定する実施規則を発行 | GMP Platform"
text = "中国の｢FCV保有台数｣､2030年に200万台超えも"
text = "クロスオーバーSUVおすすめ国産車・外車人気ランキング【2022年最新版】。。。| MOBY "
text = "［地域ビズ］プラスチック専用設備新設で処理能力2倍、よりリサイクルしやすく"
text = "中国のEV輸出が急増、第1～3四半期は34万2000台。中国メディア"
text = "工場排ガスから高効率でCO2回収、昭和電工と日本製鉄ら2030年代実装へ"
text = "インドネシア、2025年に再エネ比率23％へ"
text = "GPSをONにして20時間駆動！5気圧防水対応で体脂肪率や体内水分量も計測できるGalaxy"
text = "ボーイング、2四半期ぶり最終赤字。次期大統領専用機で費用増。22年7。9月期"
text = "日本触媒、アンモニア分解触媒を事業化、２５年めど。。。化学工業日報"
text = "米、中国半導体大手に禁輸。週内にも３０社超。報道。時事ドットコム"
text = "日本におけるコーポレートPPAの先行事例3選！。イオン・ヒューリック・村田製作所"
text = "屋内外問わずあらゆる空間のデジタルツインを作成、LiDARセンサー搭載3Dカメラ。読まぬ"
text = "凸版印刷、メタバースサービス基盤「MiraVerse」で企業の商品・空間を3D再現"
text = "中国ＥＶ電池大手ＣＡＴＬ、第3四半期は3倍増益。生産拡大が寄与"
text = "MetaLifeの累計ユーザー数が30,000人突破！"
text = "住友化学がパワー半導体を狙いGaN基板量産へ、24年度に4インチ"
text = "超軽量！。Wi。Fiがなくても使える！ソーラー充電！屋外使用可能な最もスマートなAI搭載ワイヤレス4Gネットワ。ーク防犯カメラ『AIOTO GO』日本初上陸！Makuakeにて先行販..."
text = "点群とBIM/CIMで4Dデジタルツイン！。KOLC＋がタイムライナー機能を拡張。|。建設ITブログ"
text = "自社データを収益に転換するための4ステップ。安易に捨てずに保存する。| HBR.org翻訳マネジメント記事"
text = "コンチネンタルが運転支援に5nmのAI半導体、性能／電力比40倍へ"
text = "追跡機能付きプラ製品をリサイクル、三井化学ら「Pla。chain」の4社"
text = "オプティムのiPhone点群アプリ「Geo Scan」で縦横断測量！。外付けLiDARで計測距離も40mに。|。建設ITブログ"
text = "ホットストック。機械株が堅調、Ｊマテリアル4％高。堅調な設備投資計画を好感"
text = "エンプラ事業は増収増益。ダイセルの４～９月期"
text = "大ガスなど５社、太陽光８カ所新設。オフサイトＰＰＡ開始"
text = "脱化石資源研究　未来の扉開く（５）ブリヂストン　タイヤ創って売る・使う・原材料に戻す"
text = "先端の成分と技術を注ぎ込んだ未来の名品コスメ5選"
text = "3年で導入校数が666倍。リスキリングもできる驚異のAI学習アプリ"
text = "男女1,000人にメンズコスメ「スキンケア」に関する調査／男性で日焼け対策を実施している人は約6割。化粧水はニキビ予防など、日焼け止めは洗い落としやすさなどの機能..."
text = "東京／アルミ地金／ＬＭＥ軟調、６０００円安。|。日刊鉄鋼新聞。Japan Metal Daily"
text = "ワークマン、巧みなマーケティング戦略で広告宣伝費率は驚異の0.8％。高機能×低価格が可能にした｢非常識経営｣"

text = "「Z世代」特化型マーケティング　等身大の視点で企画や「トレンド開発」"
text = "「やりたいことって何だろう？」 しいたけ.さんが仕事に悩む4人にアドバイス！"
text = "【日本一のマーケッター特別講義】ラスト1％、詰めの甘い人が犯している、ベネフィット訴求の残念な盲点"
text = "天才たちの雑談　健康の鍵握る体内の「ゴミ掃除」 実は人体は謎だらけだ（Wedge（ウェッジ））。学校化する"

text = "アキュラホーム。日本初、5階建純木造モデルを開設"
text = "現場との協働でAIモデルを作成！プロジェクトを支えたノーコードAI開発手法"
text = "注目銘柄ダイジェスト（前場）:ベクトル、エーザイ、エフ・コードなど。| 。財経新聞"
text = "筑波大，中赤外線により30fsで原子や電子を観察"
text = "プラスチックからの将来の二酸化炭素排出量を減らす方法"
text = "【横須賀市様にご協力を頂き、発話音声データの収集を開始しました！！】。。発話音声から睡眠不足を検知し交通事故を減らすリスク管理DX"
text = "東工大ら，量子センサで充放電電流を高精度計測"
text = "センサーも「量子」が主役。EV電池、ダイヤで高精度計測"
text = "EV電池の米レッドウッド、4800億円投じて米国に新工場"
text = "VW、新型コンパクト電動SUV生産へ…ドイツ本社工場で。|。レスポンス"
text = "TSMC、アリゾナ新工場を4nmプロセスに切り替え。| 。財"
text = "酸素発生反応の酸化還元化学の光による切り替え"
text = "DXのゴールは“実装”。。ITとデジタルを部門統合した三井物産の組織運営"
text = "NECがDX戦略、社内人材1万人をDX人材にシフト"
text = "樹脂のバイオシフト。トヨタ工場が脱炭素時期を前倒"
text = "Paumanok Publications。「回路保護部品。世界市場、技術、機会。2022。2027年」の出版・販売のご案内"
#text = "【横須賀市様にご協力を頂き、発話音声データの収集を開始しました！！】。。発話音声から睡眠不足を検知し交通事故を減らすリスク管理DX"
text = "富士フイルムの半導体製造プロセス新拠点。安定供給と品質要求に応える。|。電波新聞デジタル"
text = "社会の期待に化学で応える、\"グローバルニッチトップ100\""
text = "水素発生効率と電化輸送特性を向上させるCOF材料の結合様式制御手法、京大などが開発"
text = "GlobalWafers、米テキサス州に300mmシリコンウェハ製造工場を起工"
text = "【AIを駆使したコンサル】。。高山博和・セカンドサイトアナリティカ社長。"
text = "関電「原子力から水素」実証／追跡技術を駆使、敦賀で。|。電気新聞ウェブサイト"
text = "光源技術とAI技術の融合による車載ナイトビジョンシステムを開発、京セラ"
text = "子宮頸部前がん病変と診断された女性の体験するスティグマのコーピングに向けた看護支援モデルの実現可能性の評価:ランダム化比較試験による看護支援の効果の検証"
text = "古河電工の電力関連事業／北海道・本州間大型案件に照準／技術開発強化・生産増強視野 | 日刊鉄鋼新聞 Japan Metal Daily"

text = "本物よりもおいしい？。。ヒマワリの種やエンドウ豆の"
text = "関心高いソフトバンクGの回復はあるのか。2022年3月期「赤字トップ10社」の明暗【。。ベテラン証券マンが教える株のカラクリ】。。。。。トピックス"
text = "日々の家事と育児で、もうクタクタ。そんな時こそ試してほしい！夜、お休み前に飲むアイテム"
text = "依存症を一発で治せる薬はできる？。。"
text = "スマートシティ。地方都市における意識調査～住みやすい街づくりのためにできること"
text = "｢スマホを年中買い替える人｣に欠けている視点に会える.会場に出れる。外に出られる。"
text = "中年男、AI社会に取り残される。マサオ。note。取り残せる。食べさせる。食べられる。食べれる"
text = "コンビニ、スーパーの定番も。2022年、値上げされる食品や必需品【。。一覧】。。。東京新聞。TOKYO Web"

text = "【。。中国キーワード】。。メタバースと普通の人々の間にはどれくらい距離があるか？。。"
text = "どうしてもっと早く始めなかったのか後悔ばかり。。脳科学者が考える“追い抜かれた焦り”との付き合い方。遊べば楽しい。"
text = "神鋼加古川の降下ばいじん、目標値超過の原因特定。防じんネット目詰まりなど"
text = "メガネ外してVRしたい！じゃあゴーグルに乱視＆近視対応レンズを付ければいいじゃない。|。＆GP食べたくない。彼は大人じゃない。"
text = "「国債も株も日本銀行に買わせればいい」？"

text = "自動車用トランスミッション市場。タイプ別（手動、自動、自動マニュアル。トランスミッション。（AMT））、エンジンの種類別、車両タイプ別、および地域別。世界の需要分析と機会の見通し2023。2033年"
text = "当社グループ会社の社名変更に関するお知らせ。|。住友電工"
text = "２０２２年７月５日付。。取締役異動（案）のお知らせ２０２２年５月２５日明治安田生命保険相互会社取締役"
text = "新取締役就任に関するお知らせ"
text = "東芝林間病院の事業継承に関するお知らせ"
text = "ラクオリア創薬、Elanco Animal Health Inc.によるグレリン受容体作動薬ELURARの欧州承認申請およびマイルストン達成に伴う一時金受領のお知らせ"
text = "Laboro.AI、SCREENによる出資受け入れに関するお知らせ。|。東洋経済オンライン"
text = "AIを活用したタンパク質解析技術を持つ東工大発ベンチャー企業。aiwell株式会社との資本業務提携に関するお知らせ"
text = "アサイーは「森の血液※1」！。代替肉の品質改善目的のアサイーを用いた特許出願のお知らせ"

text = "「働くのミライ会議。vol.3」31日間期間限定アーカイブ配信のお知らせ.2022年8月1日（月）8。00～8月31日（水）23。59	"
text = "JR首都圏主要路線トレインチャンネルでの動画広告放映のお知らせ。。。太陽誘電株式会社"
text = "「サッポロ。麦とホップ」新CM放映のお知らせ	"
text = "ＨＯＹＡ[7741]。剰余金の配当（期末配当）に関するお知らせ。2022年5月26日(適時開示)。。日経会社情報DIGITAL。日本経済新聞	"
text = "ゴールデンウィーク休暇のお知らせ。2022年4月29日～5月8日。|。村田製作所	"
text = "一般競争入札のお知らせ	"
text = "日本新薬、当社製品「ビルテプソ?。。」Journal of Neuromuscular Diseases。への長期有効性および安全性データ掲載のお知らせ	"
text = "新潟工場におけるホルマリン、パラホルム、ヘキサミン生産停止のお知らせ。|。三菱ガス化学株式会社	"
text = "【。。Jackery】。。ロゴマーク更新のお知らせ。時事ドットコム	"
text = "診療所向け電子カルテ・医事会計システム事業のエムスリーグループへの譲渡に関するお知らせ	"
text = "新年度の業務改善ツールとしても最適【。。文章要約AI。タンテキ】。。精度アップのお知らせ	"
text = "HOKKAIDO BALLPARK F VILLAGE、ES CON FIELD HOKKAIDOと水辺エリアの結節点となる「THE LODGE」開業のお知らせ	"
text = "ヘリオス、住友ファーマへのユニバーサルドナーセル提供に関するお知らせ	"
text = "ブライトパス・バイオ、HER2 CAR。T細胞療法BP2301の信州大学における医師主導治験開始のお知らせ	"
text = "低圧太陽光発電所の買い取り事業開始のお知らせ	"
text = "ヘリオス、ステムアクソン社とのライセンス契約締結に向けたオプション権行使のお知らせ	"
text = "鈴茂器工。株式会社リバネス主催。テックプランター『フードテックグランプリ2022』参画のお知らせ	"
text = "超薄型/超軽量フレキシブル太陽光モジュール接着工法による風洞試験結果のお知らせ	"
text = "クッキーレス感性ターゲティング広告サービス「Trig’s」オープントライアル開始のお知らせ	"
text = "XRコンテンツの多様な活用法。。株式会社WARKからのお知らせ。note	"

text = "エネルギー需要家企業におけるGX（グリーントランスフォーメーション）実現に向けて"
#text = "2030年の住宅の省エネルギー性能の向上に向けて窓の性能表示制度を見直します！。"
#text = "ユナイテッド航空、Archer Aviation製のeVTOL購入に向け約13.5億円を前払い。。100機分"
#text = "水素サプライチェーン。脱炭素社会の実現に向けて。＜けいざい風水＞"
#text = "大阪府が民間２３社と高齢者支援、スマートシティ実現に向け。≫。Lmaga.jp"

text = "男性も使ってみよう「手首皮膚温」。。 Apple Watch基本の「き」Season 8"
text = "分子動力学計算で使う力場まとめ。tacoma。note"
text = "春の洗濯は菌の増殖に要注意！。洗濯機を脱衣かご代わりに使うのはNG"
text = "徳島県内初の人工アイススケートリンク23年度オープン。県立東部防災館に、氷使わず樹脂パネル敷き詰め。政治・行政。徳島ニュース。徳島新聞デジタル"
text = "タチエス、自動車シートを軽く。金具使わず接着剤で固定"
text = "次世代型シャワーヘッド「ミラブルzero」を使ってみた"
text = "広がるか、アバターを使った無人接客。小売テック最先端。"
text = "電源ボタンなし！。乗るだけで12項目を測定できる体重体組成計「。Smart Scale C1」を使ってみた"
text = "Python。スクリプトを使って個々のインスタンス。グループをステートフル。MIG。に移行する方法"
text = "人類がこれまで採掘してきた「金」は何に使われているのか？。。"
text = "Lenovo、スマホやPCと接続して使うメガネ型ディスプレイ"
text = "ゼロからはじめるJavaScript(17) JSも便利なGoogle ColabをPDF生成ツールとして使ってみよう！"
text = "実は半分以上は都会以外。LINE WORKSはやっぱり全国津々浦々で使われていた。"
text = "iCARE、新たな人事制度を開始。週2時間を“働くひとの健康創り”に使う"
text = "Ｊーケミカル。バイオフェノール使った接着剤。?。。。日刊木材新聞社"
text = "コマンドを使わずに理解するGit"
text = "スポンジやペーパータオルは使わない。キッチンであえて手放してよかったもの4選"
text = "７月１日。毒を薬に。一酸化炭素をホイップクリームにして治療に使う"
text = "【。。食と健康。ホントの話】。。消毒薬「ＭＡ。Ｔ」を口腔内に使い飛沫感染抑止。阪大大学院歯学研究科顎口腔機能治療学教室・阪井丘芳教授"
text = "食べて、社会課題に触れる。木粉使ったケーキ"
text = "Googleのスマートスピーカーがアップデートで使いにくく。特許問題のとばっちりで"
text = "Power Automateのデスクトップフローとクラウドフローを接続して使う〔準備編〕"
text = "3Dプリンターで錠剤用スプーン作ったよ！→商品化望む声が続々。開発者さん"
text = "全盲のわが子たちのために「居場所」を埼玉県に作った母たち、。多くの人に助けられ。たまひよ"

text = "配膳ロボ　なぜほとんどが中国製	"
text = "マスクなしの昼寝で園児クラスター、電気通信大など調査。"
text = "「導電性インク。世界市場2026年予測」最新調査リリース。"
text = "世界の風疹診断検査業界の市場調査2030年。"
text = "インテル、ノートブックおよびデスクトップPCの市場シェアをAMDから奪還。マーキュリーの最新調査報告書。"

text = "80%の人がメタバースは現実の生活よりも包括的な空間、調査結果で明らかに。"
text = "アップル上級幹部、「iPhone」のUSB。C対応の意向を明らかに。"
text = "攻撃者が試すパスワードの上位が明らかに。。デフォルトの認証情報は変更を。"
text = "Appleが米FCCに申請し注目浴びた謎の通信機器、その姿が明らかに。"
text = "iPhone 14シリーズでは国内で「5G SA」が使えず。ドコモとソフトバンクが明らかに。"
#text = "化学物質を使ってヒト幹細胞を作製。中国の研究チーム。"
#text = "アスリートの知恵を、ブレイクに使うな。|。ウェブ電通報。"
#text = "グローバルVRボックス市場の収益、市場規模、販売量、売上高、価格の分析レポート2022。2028。"
#text = "DXは余裕がある会社じゃないとできない。"
text = "リクガメからウミガメに”変形”できる「水陸両用カメ型ロボ」。"
text = "自分なりにできること。自分なりにできたもの。"
#text = "太郎がラーメンを食べることを次郎は楽しい"
#text = "そのことを開発したこと"
text = "「家で最期を迎えたい」患者の願いに寄り添い10年。那須烏山・訪問看護ステーションあい。"
text = "モチベーションのカギは「1 on 1」。部下を依存させない理想的なスタイルとは〈AERA〉（AERA dot.）。"
text = "試さない。試せない。試される。試されない。"
text = "うまくいかない。"
text = "チョコミントアイスのようなブルーピンクとホワイトの２カラー！臭わない・散らからないドーム型。「コンテナ猫トイレ」。miraiON。"
text = "【。。精神科医が教える】。。どんな困難もプラスにできる人、マイナスにしかならない人。ネガティブ思考から抜け出せない人が“決定的に見落としていること”。"
text = "中国の習主席。軍に戦闘準備に専念するよう指示。"
text = "「家で最期を迎えたい」患者の願いに寄り添い10年。那須烏山・訪問看護ステーションあい。"
text = "試さない。試せない。試される。試されない。"
text = "試される。試されない。"
text = "部下を依存させない。使えず。"

text = "80%の人がメタバースは現実の生活よりも包括的な空間、調査結果で明らかに。"
text = "ガンを引き起こしやすい野菜が明らかに"
text = "ブラックホールによりスパゲッティ状態となった星の末路が明らかに。"

text = "製造業ＰＭＩ、7月は52.2に小幅低下。前月は52.7。ａｕじぶん銀・Ｓ＆Ｐグローバル。"
text = "中国の科学技術人材は1億1234万人。40歳未満が75％、女性が4割。"
text = "【。。お口の殺菌と善玉菌の意識調査】。。お口の殺菌は84％の人が大切と回答。しかし善玉菌が消えてまで殺菌したい人は27％、分からない人が39%に。殺菌と菌活のバランスが求め...。"
text = "ルノー、７。９月期増収も投資家の懸念拭えず。株価下落（Bloomberg）。"
text = "今からでも抑えておきたい、国分グループが提案する2022食の10大トレンドとは。_小売・物流業界。ニュースサイト【ダイヤモンド・チェーンストアオンライン】。"
text = "ラズパイでメッシュネットワークを作成する。構築編その2。名刺サイズの超小型PC「ラズパイ」で遊ぶ（第65回）。"
text = "「ドイツ版エネルギーの５Ｄとビジネスの境界線」と題して、ＵＭＷＥＲＬＩＮ。ＵＧ代表／ドイツ在住エネルギー関連調査・政策コンサルタントによるセミナーを2022年8月9...。"
text = "財新の中国サービス部門ＰＭＩ、11月は46.7。半年ぶり低水準。"
text = "ブラザー、9/20廃棄品をプリントでリユースするプロジェクトのイベントに協賛。"
text = "時計の目利き+編集部のイチ押しはこの26本──その2。"
text = "BOC、737。8を40機追加発注。"
text = "ラズパイでメッシュネットワークを作成する。準備編その2 (ITmedia NEWS)。"
text = "TmaxSoft社、2022。年。ISG Provider Lens(TM)。クアドラント。レポートで、2年連続でメインフレームのモダナイゼーション・ソフトウェアのリーダーに選出！。"
text = "Z世代・アルファ世代のリアル。テックネイティブな未来の消費者を紐解く④～テックネイティブとテレビとの新しい関係～。。。知るギャラリー。by INTAGE。"
text = "AMLで移植を受けた患者の補助療法と維持療法として免疫調節薬KRP。203を評価するフェーズ2b/3が2022。"
text = "「Google Home」刷新、スマートホーム相互運用時代を見据えて使いやすさで勝負。"
text = "【。。堀江貴文】。。「シミとたるみはメンテナンス感覚で、定期的にやっつける」──連載「金を使うならカラダに使え！」Vol.3。"
text = "三井物産など設立のT2 26年度からトラ自動運転。東京。大阪を皮切り。|。輸送経済新聞社。"
text = "中国でコロナ再燃、経済に暗雲。行動制限、緩和求める声も。"
text = "Ｇ７エネ相が共同声明、石炭廃止は年限明示せず／原子力「基幹電源に」。|。電気新聞ウェブサイト。"
text = "ニコン初のＶｌｏｇ向けカメラに歓迎の声。ファインダーレスのコンパクトさが好評。サブ機として検討するユーザーも。。。記事詳細。Infoseekニュース。"

text = "コロナ禍後もテレワークを望む人9割超、一方で長時間労働にストレスの声も"
text = "LG OLED evo TV、世界最小型の42インチ台披露。"
text = "目玉は電動技術、コマツ・日立建機などが国際建機見本市で披露する技術力（ニュースイッチ）。"
text = "ダイソン、家事を助けるロボットの「手」披露。食器やおもちゃの片付けも。"
text = "最後のジャンボ機、ボーイングがお披露目。アトラス向け747。8F貨物機、23年納入。"
text = "アマゾン。商品の仕分けできるAI活用した最新ロボット初披露。| NHK。"
#text = "マスク氏、人型ロボット披露。「ターミネーター化」防止を約束。"
#text = "電子部品大手ニチコン。京都・亀岡に「家産家消」開発披露。。。ニュース。KBS京都。"
#text = "電子部品大手ニチコン。京都・亀岡に「家産家消」モデルハウス披露。。。ニュース。KBS京都。"

#text = "中国、コロナ感染の日次データ公表中止－地方の発表と食い違い"

text = "快適なハイブリッドワーク実現のカギは“まるでフェースツーフェース”のような環境づくり――半導体・ICT商社が行き着いた改善策とは：昭和スタイルが残る会社が目指したのは「働き方、働く環境のDX」"
text = "丸井とキリンHD、ウェルビーイングで「手挙げ」「多様性」を推進"

text = "「２０３０年の発電コスト「曲解」に懸念。統合コストや前提も変動。"
text = "コンテナ船ONE、トヨタに次ぐ利益。一本足打法に懸念も。"
text = "AT&Tとベライゾン、5G運用開始を延期。米航空当局が懸念。"
text = "［スキャナー］ウクライナ侵攻、世界の物価高に拍車。露制裁「返り血」で景気後退の懸念。。。経済。。。ニュース。"
text = "「ここはアメリカではなく中国だ！」身に覚えもないのになぜ。上海の日本人社会で急浮上した新たな懸念。"
ato_text = "EUで使用禁止の食品添加物ナノ粒子・二酸化チタン、日本で広く使用。毒性に懸念。"
text = "ＥＶ化に揺れる日本の自動車産業源流の地。静岡の中小部品存続懸念も。"
text = "Google、AI寡占化の懸念再び。40億枚もの画像学習。"
text = "アメリカ景気後退の懸念。NYダウ3万ドル割れ、原油・半導体も急減速"
text = "国内大手8社が参画する次世代半導体新会社「Rapidus（ラピダス）」への「懸念事項」。。。記事詳細。Infoseekニュース。"
text = "新型エクストレイル、日産九州「半導体不足の懸念ない」。"
text = "中国の新規感染者は2日連続で3万人超え。経済への悪影響に懸念拡がる。中国人民銀行は預金準備率を引き下げへ（幻冬舎ゴールドオンライン）。"
text = "東芝再建、経営陣の処遇で買い手候補に相違。維持案は銀行も懸念。"
text = "津軽線､被災して見えた｢もし鉄道がなかったら｣。"
text = "33%OFF。iOS向け本格動画編集ツール「LumaFusion」ほか［4月16日版］セール・お得情報。"
text = "“印刷で”配線・接合“銅ナノペースト”。貴金属代替へ【。。三井金属鉱業】。。。| AEG自動車技術者のための情報サイト。Automotive Engineers’。Guide。"
text = "「#高速道路定額化。による地域活性化について」の情報交換会。。。。石田一也（イシダカズヤ）。"
text = "「すごく問題解決力のある人」が常にアンテナを張っている“3つの情報”。"
text = "｢財閥系に落ちたら日本に行くしかない｣高齢者が稼ぎ､若者は失業する韓国のいびつな構造。。。文政権の失策は将来禍根を残す恐れ。(PRESIDENT Online。プレジデント社の総合情報サイト)。"
text = "｢商売だけではいかん｣松下幸之助が財界の先輩たちの前で経験した""42歳の大恥"" 。。そして奥深い教養を身に着けた。(PRESIDENT Online。プレジデント社の総合情報サイト)。"
text = "「植えない田植え」普及に本腰。JA広島中央、作業量やコスト軽減。|。中国新聞デジタル。|。広島を中心とした中国地方のニュース・情報サイト。"
text = "【。。マツダ。CX。60】。。直6＋48Vマイルドハイブリッドも設定、後輪駆動（レスポンス）(ヘッドライン) |。自動車情報サイト【。。新車・中古車】。。。。 carview!。"
text = "JIS規格20フィート・40フィートコンテナ【。。建築確認申請が通るコンテナ】。。の販売開始のお知らせ【。。ハレコンテナ】。。。食品卸、問屋の業績、人事、企業合併など、最新情報。ニュース。フーズチャネル。"
text = "Twitter、サードパーティ製クライアントAPI停止は「意図的」との内部情報（PHILE WEB）。"
text = "インタビュー／富士電機社長兼ＣＯＯ・近藤史郎氏。持続成長へ情報感度上げ変化捉える。"
text = "グローバルサプレッションコンデンサに関する市場レポート, 2017年。2028年の推移と予測、会社別、地域別、製品別、アプリケーション別の情報。"
text = "スタートアップの取締役就任の20代。強みは情報収集。"
text = "テキサス州、Metaを提訴。。Facebookの顔認識による情報収集で。"
text = "バイク用ヘルメットにナビ情報。"
text = "バッテリーEV戦略に関する説明会【。。トヨタ自動車】。。。| AEG。自動車技術者のための情報サイト。Automotive Engineers’。Guide。"
text = "ホンダ初の電動SUV「ホンダ。プロローグ」2024年に市場デビュー。すべての情報！（AUTO BILD JAPAN Web）。"
text = "マーケティングとクリエイティブの総合情報。新事業に役立つ。"
atotext = "リンク価値を爆上げする「関連性4本柱」はどんな業種のアイデア発想にも使えるフレームワーク（前編）。| Moz 。 SEOとインバウンドマーケティングの実践情報。"
text = "委託研究公募に関する情報。。。調達情報。| NIMS。"
text = "英国、HTGR実証炉建設計画の入札に先立ち産業界と情報交換。|。原子力産業新聞。"
text = "海保の無人航空機「シーガーディアン」で得た情報。海上自衛隊との共有する方向で検討。"
text = "堤防決壊、センサーで正確に把握。住民への情報伝達スムーズに。"
text = "東レ工場火災、逃げ遅れやけが人の情報なし。"
text = "突き付けられる日本市場の地盤沈下。。ゼロ成長で強まる生産性への意識。|。日刊薬業。。。医薬品産業の総合情報サイト。"
text = "日本国際賞に光通信網大容量化、光感受タンパク質による神経研究の4氏。| Science Portal 。。科学技術の最新情報サイト「サイエンスポータル」。"

text = "ペンタブレットの「ワコムストア」、個人情報14万7000人分漏えいの恐れ。"
text = "カズレーザー、野口聡一氏も恐れる博識ぶり。「僕が一生懸命考えた問題を全部解かれた」。紀伊民報AGARA。"
text = "来年の世界自動車販売5.6％増、需要減退が打撃に。Ｓ＆Ｐ。"
text = "ホンダ５割減・マツダ６割減。米国市場が伸び悩み、日系車メーカーに大打撃。ニュースイッチ。by。日刊工業新聞社。"
text = "実は日本企業にとって大打撃。政府が「脱石炭」に賛同できぬ深い闇。"
text = "EUエネルギー政策、現実路線に。30年55%排出減に前進（写真=ロイター）。"
text = "アニオン交換膜を利用した水電解による。高性能、高耐久、低コストの水素製造システム。水素社会の実現へ大きく前進。"
text = "パナソニックがテスラ向け大容量バッテリーを2023年に生産開始との報道。"
text = "海洋水産技術協議会、洋上風力と共存の道標。"
text = "三菱電機｢知財の武器｣から始まる縦割り打破の道。| IT･電機･半導体･部品。"
text = "自動車7社の21年度上期決算、部品不足で生産回復は道半ば。"
text = "人の動きで抗菌する繊維「PIECLEX」、製品化が軌道に。"
text = "中国の半導体/装置メーカー勤務の米国人は帰国か米国籍離脱かの選択に直面、海外紙報道。"
text = "米政府がArF液浸露光装置の中国への輸出禁止を日蘭政府に要請か？。。、米紙報道。"
text = "『東芝』に会社分割案が浮上。事実上の“解体”が現実味。"
text = "EUエネルギー政策、現実路線に。30年55%排出減に前進（写真=ロイター）。"
text = "マツダ、白紙に戻った広島の電池ライン。巨額負担に現実路線。"
text = "政策が非現実的すぎる。脱原発で絶賛されたドイツが危機を迎えている事態。"
text = "中国が隠す「人口問題」に“衝撃の新事実”。習近平が恐れる「中国経済大崩壊」がついに現実へ！（藤。和彦）。@moneygendai。"
text = "日本には「クソどうでもいい仕事」が多すぎる。もうすぐ韓国にも抜かれる日本のヤバい現実（池田。清彦）。@gendai_biz。"
text = "多すぎる食事を食べる。泳ぎすぎる。食べすぎる。"
text = "米最大規模の油田で大量のメタン排出／露断絶で「スプリンターネット」が現実味。"
text = "Intelが３次元集積でTSVより高性能な新技術、組み立て受託を視野に。"
text = "デンソー、半導体部門の分社化も視野。外部販売に商機とＣＴＯ。"
text = "新パワー半導体「縦型GaN」、シリコン並みコストが視野。"
text = "産業用検査ロボットを5Gで遠隔監視、将来は宇宙への挑戦も視野に。"
text = "ミキティ。“義母がなかなか帰ってくれない。”悩みに神回答。ファン絶賛「無敵」「最高すぎる!」。。。記事詳細。Infoseekニュース。"
text = "村田製作所、4～9月連結は売上高が過去最高。|。電波新聞デジタル。"
text = "台湾半導体生産、21年は過去最高。日本勢に投資呼びかけ。"
text = "中国ゼロコロナ機能不全を露呈。経済犠牲でも感染者最高。"
text = "日本郵船の経常益1兆円規模。22年3月期、国内海運で最高。"
text = "半導体装置の受注残2.8倍で過去最高、増える需要に追いつかぬ生産。ニュースイッチ。by。日刊工業新聞社。"

text = "話題の先端にフィルターが付いたストローでコーヒーを飲んでみた！"

text = "韓国政府が急加速「電気自動車の生産450万台」。今日加速「電気自動車の生産450万台」"
text = "効率的な放熱を実現する伝熱異方性を持つ複合フィルムを開発<br>～二次元フィルムの多様な放熱パターンの設計と持続的な利用につながる成果～。東京"
text = "世界の潮流と人事の変化【“人的資本経営”の最前線を知る#1。セミナーレポート"
text = "「成果をだす人」が絶対に採用しない“ルール”ーー真面目なリーダーほど陥る「士気爆下げ」の危険（東洋経済オンライン）。"
text = "また土下座？。。。冷静だった妻の怒りが爆発した夫の身勝手な一言とは【され妻なつこ。Vol.77】。"
text = "なぜ「円高時に儲かること」をするのか？"

text = "新任部長の苦悩。優秀な直属部下2人がまったく指示を聞かない場合どうする？。。"

text = "「静かな退職」阻止は経営者の責務。ダボス会議パネルで専門家指摘。"
text = "「三星がＴＳＭＣに立ち向かうには李在鎔氏が全面的に乗り出すべき」。英誌が指摘。"

# ニュースのカテゴリ分類のチェック
government_phase = ncc.news_category_classification(text)
print(government_phase)