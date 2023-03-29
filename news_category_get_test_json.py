import json
from news_category_classification import CategoryClassification
from sentence_category_get import SentenceCategoryGet
from category2pest import Category2Pest
from category2tab import Category2Tab


model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化
sc = SentenceCategoryGet()
c2p = Category2Pest()
c2t = Category2Tab()

file_name = "data/bq_ajinomoto_ja_updated.json"
file_name = "data/bq_murata_ja_updated.json"
file_name = "data/CN_ja.json"
file_name = "data/theme_log_23_03_06-12.json"
file_name = "data/views.json"

articles1 = json.load(open(file_name))
out_file_name = file_name.split(".")[0] + "_out.json"
out_file2 = open(out_file_name, 'w')

out_file = open('data/category_result_json.tsv', 'w')

for news in articles1:
    if not news["title"] and ("text" not in news or not news["text"]):
        out_file.write("")
        continue
    if "text" in news:
        category_list = model.news_category_classification(news["title"], news["text"])  # カテゴリの候補の抽出
    else:
        category_list = model.news_category_classification(news["title"], "")  # カテゴリの候補の抽出
    if sc.debug:
        print(category_list[0] + "\t" + category_list[1])
        out_file.write(news["title"] + "\t" + category_list[0] + "\t" + category_list[1])
    else:
#        pest = c2p.category2pest(category_list)
        pest = c2t.category2tab(category_list[0])
        print(category_list[0] + "\t" + pest)
        ret = news["title"] + '\t' + category_list[0] + "\t" + pest + '\n'
        news["category"] = category_list[0]
        news["Anews"] = pest
        out_file.write(ret)
    print("--------------------\n")
    if sc.debug:
        out_file.write("----\t----\t----\t----\t----\t----\t----\t----\t----\t----\n")
ret = json.dumps(articles1, indent=2, ensure_ascii=False)
out_file2.write(ret)
out_file.close()
out_file2.close()
