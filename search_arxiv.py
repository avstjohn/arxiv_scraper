import sys
import arxiv
import pandas as pd

from get_data import store_results, categorize_tags, categorize_authors
from histograms import cat_histogram, author_histogram
from undirected_graph import get_unique_authors

# def conn_author_article(authors, unique_authors):
#         conn_matrix = np.zeros((len(authors), len(unique_authors)), dtype=int)
#         for i in range(len(authors)):
#                 temp = np.zeros((len(unique_authors)), dtype=int)
#                 for j in range(len(authors[i])):
#                         temp += (unique_authors == authors[i][j])
#                         print(temp)
#                 conn_matrix[i,:] = temp
#
#         # fig = plt.figure(figsize=(10,5));
#         # plt.spy(conn_matrix, marker ='s', color='chartreuse', markersize=5);
#         # plt.xlabel('Authors');
#         # plt.ylabel('Articles');
#         # plt.title('Authors of the articles', fontweight='bold');
#
#         return conn_matrix

search_query = str(sys.argv[1])
max_results = int(sys.argv[2])

results = arxiv.query(search_query=search_query, start=0, max_results=max_results,
                        sort_by="submittedDate", sort_order="descending")

title, authors, date, summary, tags, pdf_url = store_results(results)

cat_counts = categorize_tags(tags)

author_counts = categorize_authors(authors)

cat_histogram(cat_counts, search_query, max_results)

author_histogram(author_counts, search_query, max_results)

unique_authors = get_unique_authors(authors)

# conn_author_article = conn_author_article(authors, unique_authors)
# print(conn_author_article)
#conn_coauthors = conn_coauthors(authors, unique_authors)

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
