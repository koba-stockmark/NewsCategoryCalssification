import json
from news_category_classification import CategoryClassification
from category2pest import Category2Pest

model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化
c2p = Category2Pest()

file_name = "data/bq_ajinomoto_ja_updated.json"
file_name = "data/bq_murata_ja_updated.json"

articles1 = json.load(open(file_name))
out_file_name = file_name.split(".")[0] + "_out.json"
out_file2 = open(out_file_name, 'w')

out_file = open('data/category_result_json.tsv', 'w')

debug_f = False

for news in articles1:
    category_list = model.news_category_classification(news["title"])  # カテゴリの候補の抽出
    if debug_f:
        print(category_list)
        out_file.write(news["title"] + "\t" + category_list)
    else:
        pest = c2p.category2pest(category_list)
        print(category_list + "\t" + pest)
        ret = news["title"] + '\t' + category_list + "\t" + pest + '\n'
        news["category"] = category_list
        news["PEST"] = pest
        out_file.write(ret)
    print("--------------------\n")
    if debug_f:
        out_file.write("----\t----\t----\t----\t----\t----\t----\t----\t----\t----\n")
ret = json.dumps(articles1, indent=2, ensure_ascii=False)
out_file2.write(ret)
out_file.close()
out_file2.close()
