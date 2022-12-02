import json
import re
from news_category_classification import CategoryClassification

model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化

articles = json.load(open('nikkei.json'))
articles2 = json.load(open('nikkei_5000.json'))
articles3 = json.load(open('datsutanso.json'))
articles4 = json.load(open('gyoukai.json'))

out_file = open('category_result.tsv', 'w')

for doc in articles4:
    for sep_doc in doc.splitlines():
        category_list = model.news_category_classification(sep_doc)  # カテゴリの候補の抽出
#        ret = sep_doc + '\t' + category_list + '\n'
        ret = category_list + '\n'
        print(sep_doc + '\t' + ret)
        out_file.write(ret)
out_file.close()
