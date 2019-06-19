import numpy as np

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
