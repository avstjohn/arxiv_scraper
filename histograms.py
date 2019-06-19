import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['backend'] = "Qt5Agg"

def cat_histogram(cat_counts, search_query, max_results):
        x_cat = np.arange(0, len(list(cat_counts.keys())))
        labels_cats = list(cat_counts.keys())

        plt.title("Common subjects of " + str(max_results) + " most recent publications by search term: " + search_query)
        plt.grid(True)
        plt.xticks(x_cat, labels_cats, rotation=90);
        plt.bar(cat_counts.keys(), sorted(cat_counts.values(), reverse=True))
        plt.show()

def author_histogram(author_counts, search_query, max_results):
        x_authors = np.arange(0, len(list(author_counts.keys())))
        labels_authors = list(author_counts.keys())

        plt.title("Common authors of " + str(max_results) + " most recent publications by search term: " + search_query)
        plt.xticks(x_authors, labels_authors, rotation=90)
        plt.bar(author_counts.keys(), sorted(author_counts.values(), reverse=True))
        plt.show()
