import json
import csv
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
articles13 = json.load(open('err_hiro.json'))
articles14 = json.load(open('oki_title.json'))
articles15 = json.load(open('tdk_title.json'))
articles16 = json.load(open('TDK_OKI_ng.json'))
articles17 = json.load(open('PoC_OKI_TDK.json'))
articles18 = json.load(open('PoC_OKI.json'))
articles19 = json.load(open('PoC_TDK.json'))
articles20 = json.load(open('New_OKI_TDK_ng.json'))
articles21 = json.load(open('harabe_tdk.json'))
articles22 = json.load(open('sakamoto_err.json'))

out_file = open('category_result.tsv', 'w')

debug_f = True

for doc in articles22:
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
