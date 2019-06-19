import re
from collections import defaultdict

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
