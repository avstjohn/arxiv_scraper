import arxiv
from nltk import word_tokenize

def store_results(results):
        count = 0
        title, authors, date, summary, tags = [], [], [], [], []
        for r in results:
                title.append(r['title'].replace('\n', ''))
                authors.append(r['authors'])
                date.append(r['published'])
                summary.append(r['summary'].replace('\n', ' '))

                #if count == 13: print(r['tags'])
                tags_temp = []
                for j in range(len(r['tags'])):
                        tags_temp.append(r['tags'][j]['term'])
                tags.append(tags_temp)

                count += 1
        return (title, authors, date, summary, tags)

#subjects = ["astro-ph", "cond-mat", "gr-qc", "hep-ex", "hep-lat",
#          "hep-ph", "hep-th", "math-ph", "nlin", "nucl-ex",
#          "nucl-th", "physics", "quant-ph"]


subject = "hep-th"
keyword = "topological quantum field theory"

search_query = subject + ":" + keyword
max_results = 50

results = arxiv.query(search_query=search_query, start=0, max_results=max_results,
                        sort_by="submittedDate", sort_order="descending")

title, authors, date, summary, tags = store_results(results)

tokens =