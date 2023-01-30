import json
import re
from news_category_classification import CategoryClassification

model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化

articles = json.load(open('nikkei.json'))
articles2 = json.load(open('nikkei_5000.json'))
articles3 = json.load(open('datsutanso.json'))
articles4 = json.load(open('gyoukai.json'))
articles5 = json.load(open('title.json'))
articles6 = json.load(open('category_ng.json'))
articles7 = json.load(open('category_ng2.json'))
articles8 = json.load(open('all_title.json'))
articles9 = json.load(open('cat_err.json'))
articles10 = json.load(open('all_ng.json'))

out_file = open('category_result.tsv', 'w')

debug_f = True

for doc in articles10:
    for sep_doc in doc.splitlines():
        category_list = model.news_category_classification(sep_doc)  # カテゴリの候補の抽出
        print(category_list)
        if debug_f:
            out_file.write(category_list)
        else:
            ret = sep_doc + '\t' + category_list + '\n'
            out_file.write(ret)
    print("--------------------\n")
    if debug_f:
        out_file.write("----\t----\t----\t----\t----\t----\t----\t----\t----\t----\n")
out_file.close()
