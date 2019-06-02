import arxiv
import re
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['backend'] = "Qt5Agg"
import pandas as pd

def store_results(results):
        count = 0
        title, authors, date, summary, tags, pdf_url = [], [], [], [], [], []
        for r in results:
                title.append(r['title'].replace('\n', '').replace('  ', ' '))
                date.append(r['published'])
                summary.append(r['summary'].replace('\n', ' ').replace('  ', ' '))
                pdf_url.append(r['pdf_url'])

                authors_temp = []
                for j in range(len(r['authors'])):
                        authors_temp.append(r['authors'][j])
                authors.append(sorted(set(authors_temp)))

                tags_temp = []
                for j in range(len(r['tags'])):
                        term = r['tags'][j]['term']
                        if bool(re.search(r'\d', term)) ==  False:
                                tags_temp.append(term)
                tags.append(sorted(set(tags_temp)))

                count += 1
        return (title, authors, date, summary, tags, pdf_url)

def categorize_tags(tags):
        physics_cats = ["astro-ph", "cond-mat", "gr-qc", "hep-ex", "hep-lat",
                        "hep-ph", "hep-th", "math-ph", "nlin", "nucl-ex",
                        "nucl-th", "physics", "quant-ph"]

        astroph_prefix = "astro-ph."
        astroph_cats = ["GA", "CO", "EP", "HE", "IM", "SR"]

        condmat_prefix = "cond-mat."
        condmat_cats = ["dis-nn", "mtrl-sci", "mes-hall", "other",
                        "quant-gas", "soft", "stat-mech", "str-el",
                        "supr-con"]

        nlin_prefix = "nlin."
        nlin_cats = ["AO", "CG", "CD", "SI", "PS"]

        physics_prefix = "physics."
        physics_subcats = ["acc-ph", "app-ph", "ao-ph", "atom-ph", "atm-clus",
                        "bio-ph", "chem-ph", "class-ph", "comp-ph", "data-an",
                        "flu-dyn", "gen-ph", "geo-ph", "hist-ph", "ins-det",
                        "med-ph", "optics", "ed-ph", "soc-ph", "plasm-ph",
                        "pop-ph", "space-ph"]

        math_prefix = "math."
        math_cats = ["AG", "AT", "AP", "CT", "CA", "CO", "AC", "CV",
                     "DG", "DS", "FA", "GM", "GN", "GT", "GR", "HO",
                     "IT", "KT", "LO", "MP", "MG", "NT", "NA", "OA",
                     "OC", "PR", "QA", "RT", "RA", "SP", "ST", "SG"]

        stat_prefix = "stat."
        stat_cats = ["AP", "CO", "ML", "ME", "OT", "TH"]

        cat_counts = defaultdict(int)
        for i in range(len(tags)):
                for j in range(len(tags[i])):
                        if (tags[i][j] in physics_cats or
                            tags[i][j] in [astroph_prefix + a for a in astroph_cats] or
                            tags[i][j] in [condmat_prefix + a for a in condmat_cats] or
                            tags[i][j] in [nlin_prefix + a for a in nlin_cats] or
                            tags[i][j] in [physics_prefix + a for a in physics_subcats] or
                            tags[i][j] in [math_prefix + a for a in math_cats] or
                            tags[i][j] in [stat_prefix + a for a in stat_cats]):
                            cat_counts[tags[i][j]] += 1
        return cat_counts

def categorize_authors(authors):
        author_counts = defaultdict(int)
        for i in range(len(authors)):
                for j in range(len(authors[i])):
                        author_counts[authors[i][j]] += 1
        return author_counts

def cat_histogram(cat_counts, max_results):
        x_cat = np.arange(0, len(list(cat_counts.keys())))
        labels_cats = list(cat_counts.keys())

        plt.title("Common subjects of " + str(max_results) + " most recent publications by search term: " + search_query)
        plt.grid(True)
        plt.xticks(x_cat, labels_cats, rotation=90);
        plt.bar(cat_counts.keys(), sorted(cat_counts.values(), reverse=True))

def author_histogram(author_counts, max_results):
        x_authors = np.arange(0, len(list(author_counts.keys())))
        labels_authors = list(author_counts.keys())

        plt.title("Common authors of " + str(max_results) + " most recent publications by search term: " + search_query)
        plt.xticks(x_authors, labels_authors, rotation=90)
        plt.bar(author_counts.keys(), sorted(author_counts.values(), reverse=True))

def get_unique_authors(authors):
        unique_authors = []
        for i in range(len(authors)):
                for j in range(len(authors[i])):
                        if authors[i][j] not in unique_authors:
                                unique_authors.append(authors[i][j])
        # Sort authors by last name
        temp = []
        for a in unique_authors:
                temp.append(a.split(" ")[-1] + ", " + a.split(" ")[0])
        unique_authors = temp
        unique_authors.sort()

        authors = np.array(authors)
        unique_authors = np.array(unique_authors)
        return unique_authors

def conn_author_article(authors, unique_authors):
        conn_matrix = np.zeros((len(authors), len(unique_authors)), dtype=int)
        for i in range(len(authors)):
                temp = np.zeros((len(unique_authors)), dtype=int)
                for j in range(len(authors[i])):
                        temp += (unique_authors == authors[i][j])
                        print(temp)
                conn_matrix[i,:] = temp

        # fig = plt.figure(figsize=(10,5));
        # plt.spy(conn_matrix, marker ='s', color='chartreuse', markersize=5);
        # plt.xlabel('Authors');
        # plt.ylabel('Articles');
        # plt.title('Authors of the articles', fontweight='bold');

        return conn_matrix

search_query = "cobordism"
max_results = 50

results = arxiv.query(search_query=search_query, start=0, max_results=max_results,
                        sort_by="submittedDate", sort_order="descending")

title, authors, date, summary, tags, pdf_url = store_results(results)

cat_counts = categorize_tags(tags)

author_counts = categorize_authors(authors)

cat_histogram(cat_counts, max_results)

# author_histogram(author_counts, max_results)

unique_authors = get_unique_authors(authors)

conn_author_article = conn_author_article(authors, unique_authors)
print(conn_author_article)
#conn_coauthors = conn_coauthors(authors, unique_authors)

plt.show()
#
# import pandas as pd
#
# df = pd.DataFrame(connectivity)
# authors_conn = np.zeros((len(unique_authors), len(unique_authors)))
#
# for i in range(len(unique_authors)):
#         df = df[df.iloc[:,j] > 0]
#         sum_of_rows = np.array(df.sum())
#         authors_conn[j] = sum_of_rows
#
# fig = plt.figure(figsize=(10,10));
# plt.spy(authors_conn, marker ='s', color='chartreuse', markersize=3);
# plt.xlabel('Authors');
# plt.ylabel('Authors');
# plt.title('Authors that are co-authors', fontweight='bold');
# plt.show()
