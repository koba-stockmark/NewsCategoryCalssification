import json
from news_category_classification import CategoryClassification
from category2pest import Category2Pest

model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化
c2p = Category2Pest()

articles = json.load(open('data/nikkei.json'))
articles2 = json.load(open('data/nikkei_5000.json'))
articles3 = json.load(open('data/datsutanso.json'))
articles4 = json.load(open('data/gyoukai.json'))
articles5 = json.load(open('data/title.json'))
articles6 = json.load(open('data/category_ng.json'))
articles7 = json.load(open('data/category_ng2.json'))
articles8 = json.load(open('data/all_title.json'))
articles9 = json.load(open('data/cat_err.json'))
articles10 = json.load(open('data/all_ng.json'))
articles13 = json.load(open('data/err_hiro.json'))
articles14 = json.load(open('data/oki_title.json'))
articles15 = json.load(open('data/tdk_title.json'))
articles16 = json.load(open('data/TDK_OKI_ng.json'))
articles17 = json.load(open('data/PoC_OKI_TDK.json'))
articles18 = json.load(open('data/PoC_OKI.json'))
articles19 = json.load(open('data/PoC_TDK.json'))
articles20 = json.load(open('data/New_OKI_TDK_ng.json'))
articles21 = json.load(open('data/harabe_tdk.json'))
articles22 = json.load(open('data/sakamoto_err.json'))

out_file = open('data/category_result.tsv', 'w')

debug_f = False

for doc in articles20:
    for sep_doc in doc.splitlines():
        category_list = model.news_category_classification(sep_doc)  # カテゴリの候補の抽出
        if debug_f:
            print(category_list)
            out_file.write(category_list)
        else:
            pest = c2p.category2pest(category_list)
            print(category_list + "\t" + pest)
            ret = sep_doc + '\t' + category_list + "\t" + pest + '\n'
            out_file.write(ret)
    print("--------------------\n")
    if debug_f:
        out_file.write("----\t----\t----\t----\t----\t----\t----\t----\t----\t----\n")
out_file.close()
