import json
import re
from phase_extractor import PhaseExtractor

model = PhaseExtractor() # KeywordExtractorのクラスのインスタンス化

articles = json.load(open('nikkei.json'))
articles2 = json.load(open('nikkei_5000.json'))
solution = open('solution_sentence2.txt')
out_file = open('phase_result.tsv', 'w')
out_file2 = open('government_result.tsv', 'w')

#"""
for doc in solution:
  for sep_doc in doc.splitlines():
    keyword_list = model.single_phase_extract(sep_doc) # キーワードの候補の抽出
    ret = sep_doc + '\t' + keyword_list + '\n'
    print(ret)
    out_file.write(ret)
out_file.close()
"""
for doc in articles:
  for sep_doc in doc.splitlines():
    keyword_list = model.single_phase_extract(sep_doc) # キーワードの候補の抽出
    ret = sep_doc + '\t' + keyword_list + '\n'
    print(ret)
    out_file2.write(ret)
out_file2.close()
"""