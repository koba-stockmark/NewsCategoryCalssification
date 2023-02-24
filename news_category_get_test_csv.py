import csv
from news_category_classification import CategoryClassification

model = CategoryClassification()    # CategoryClassificationのクラスのインスタンス化

articles = csv.reader(open("2023-02-15(UTC) - 2023-02-22の記事マスタ - bq-results-20230222-064642-1677048559149.csv"))

out_file = csv.writer(open('category_result.csv', 'w'))

debug_f = False

for line in articles:
    category_list = model.news_category_classification(line[2])  # カテゴリの候補の抽出
    print(category_list)
    if debug_f:
        out_file.writerow(category_list)
    else:
        if "\t" in category_list:
            line.append(category_list.split("\t")[0])
            line.append(category_list.split("\t")[1])
        out_file.writerow(line)
    print("--------------------\n")
    if debug_f:
        out_file.writerow("----\t----\t----\t----\t----\t----\t----\t----\t----\t----\n")
