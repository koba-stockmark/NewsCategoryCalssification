import csv
from news_category_classification import CategoryClassification
from category2pest import Category2Pest

model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化
c2p = Category2Pest()

articles = csv.reader(open("data/2023-02-15(UTC) - 2023-02-22の記事マスタ - bq-results-20230222-064642-1677048559149.csv"))

out_file = csv.writer(open('data/category_result.csv', 'w'))

debug_f = False

for line in articles:
    category_list = model.news_category_classification(line[2])  # カテゴリの候補の抽出
    if debug_f:
        print(category_list)
        out_file.writerow(category_list)
    else:
        pest = c2p.category2pest(category_list)
        print(category_list + "\t" + pest)
        line.append(category_list)
        line.append(pest)
        out_file.writerow(line)
    print("--------------------\n")
    if debug_f:
        out_file.writerow("----\t----\t----\t----\t----\t----\t----\t----\t----\t----\n")
