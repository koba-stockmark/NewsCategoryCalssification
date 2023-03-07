import csv
from news_category_classification import CategoryClassification
from category2pest import Category2Pest
from sentence_category_get import SentenceCategoryGet

model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化
c2p = Category2Pest()
sc = SentenceCategoryGet()

articles = csv.reader(open("data/2023-02-15(UTC) - 2023-02-22の記事マスタ - bq-results-20230222-064642-1677048559149.csv"))

out_file = csv.writer(open('data/category_result.csv', 'w'))

for line in articles:
    category_list = model.category_get(line[2])  # カテゴリの候補の抽出
    if sc.debug:
        print(category_list[0])
        out_file.writerow(category_list[1])
    else:
        pest = c2p.category2pest(category_list[0])
        print(category_list[0] + "\t" + pest)
        line.append(category_list[0])
        line.append(pest)
        out_file.writerow(line)
    print("--------------------\n")
    if sc.debug:
        out_file.writerow("----\t----\t----\t----\t----\t----\t----\t----\t----\t----\n")
