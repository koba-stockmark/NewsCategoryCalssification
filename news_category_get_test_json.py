import json
from news_category_classification import CategoryClassification
from sentence_category_get import SentenceCategoryGet
from category2pest import Category2Pest
from category2tab import Category2Tab
from category2tech_tab import Category2TechTab


model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化
sc = SentenceCategoryGet()
c2p = Category2Pest()
c2t = Category2Tab()
c2tt = Category2TechTab()

file_name = "data/bq_ajinomoto_ja_updated.json"
file_name = "data/bq_murata_ja_updated.json"
file_name = "data/CN_ja.json"
file_name = "data/theme_log_23_03_06-12.json"
file_name = "data/views.json"
#file_name = "data/english_title.json"
#file_name = "data/english_err.json"

#file_name = "data/AI.json"
#file_name = "data/3月人気記事.json"
#file_name = "data/カーボンニュートラル.json"

file_name = "data/view_log.json"
file_name = "data/gold_data.json"

articles1 = json.load(open(file_name))
out_file_name = file_name.split(".")[0] + "_out.json"
out_file2 = open(out_file_name, 'w')

out_file = open('data/category_result_json.tsv', 'w')

def map_make(news, category):
    tags = ["イベント", "技術", "政策", "製品サービス", "社会", "レビュー", "オピニオン", "提携"]
    for ch_tag in tags:
        if ch_tag in category:
            news[ch_tag] = True
        else:
            news[ch_tag] = False
    return

for news in articles1:
    if not news["title"] and ("text" not in news or not news["text"]):
        if not news["translated_title"] and ("text" not in news or not news["translated_title"]):
            out_file.write("")
            continue
    if "translated_title" not in news or  news["translated_title"] == None or news["translated_title"] == "":
        if "text" in news:
            category_list = model.news_category_classification(news["title"], news["text"])  # カテゴリの候補の抽出
#            category_list = model.news_category_classification(news["title"], "")  # カテゴリの候補の抽出
        else:
            category_list = model.news_category_classification(news["title"], "")  # カテゴリの候補の抽出
    else:
        category_list = model.news_category_classification(model.english_taitle_clean(news["translated_title"]), "")  # カテゴリの候補の抽出
    if sc.debug:
        print(category_list[0] + "\t" + category_list[1])
        out_file.write(category_list[2])
    else:
#        pest = c2p.category2pest(category_list)
#        pest = c2t.category2tab(category_list[0])
        pest = c2tt.category2tab(category_list[0])
        print(category_list[0] + "\t" + pest)
        if not news["title"] and ("text" not in news or not news["text"]):
            ret = news["translated_title"] + '\t' + category_list[0] + "\t" + pest + '\n'
        else:
            ret = news["title"] + '\t' + category_list[0] + "\t" + pest + '\n'
        news["category"] = category_list[0]
        news["Anews"] = pest
        map_make(news, pest)
        out_file.write(ret)
    print("--------------------\n")
    if sc.debug:
        out_file.write("----\t----\t----\t----\t----\t----\t----\t----\t----\t----\n")
ret = json.dumps(articles1, indent=2, ensure_ascii=False)
out_file2.write(ret)
out_file.close()
out_file2.close()
