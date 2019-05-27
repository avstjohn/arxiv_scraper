import arxiv
import nltk
from nltk import word_tokenize
import re

def store_results(results):
        count = 0
        title, authors, date, summary, tags, pdf_url = [], [], [], [], [], []
        for r in results:
                title.append(r['title'].replace('\n', '').replace('  ', ' '))
                date.append(r['published'])
                summary.append(r['summary'].replace('\n', ' ').replace('  ', ' '))
                pdf_url.append(r['pdf_url'])

                #if count == 13: print(r['tags'])
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


search_query = "tqft"
max_results = 100

results = arxiv.query(search_query=search_query, start=0, max_results=max_results,
                        sort_by="submittedDate", sort_order="descending")

title, authors, date, summary, tags, pdf_url = store_results(results)

physics_cats = ["astro-ph", "cond-mat", "gr-qc", "hep-ex", "hep-lat",
                "hep-ph", "hep-th", "math-ph", "nlin", "nucl-ex",
                "nucl-th", "physics", "quant-ph"]

physics_prefix = "physics."
physics_subcats = ["acc-ph", "app-ph", "ao-ph", "atom-ph", "atm-clus",
                "bio-ph", "chem-ph", "class-ph", "comp-ph", "data-an",
                "flu-dyn", "gen-ph", "geo-ph", "hist-ph", "ins-det",
                "med-ph", "optics", "ed-ph", "soc-ph", "plasm-ph",
                "pop-ph", "space-ph"]

astroph_prefix = "astro-ph."
astroph_cats = ["GA", "CO", "EP", "HE", "IM", "SR"]

condmat_prefix = "cond-mat."
condmat_cats = ["dis-nn", "mtrl-sci", "mes-hall", "other",
                "quant-gas", "soft", "stat-mech", "str-el",
                "supr-con"]

nlin_prefic = "nlin."
nlin_cats = ["AO", "CG", "CD", "SI", "PS"]

math_prefix = "math."
math_cats = ["AG", "AT", "AP", "CT", "CA", "CO", "AC", "CV",
             "DG", "DS", "FA", "GM", "GN", "GT", "GR", "HO",
             "IT", "KT", "LO", "MP", "MG", "NT", "NA", "OA",
             "OC", "PR", "QA", "RT", "RA", "SP", "ST", "SG"]

stat_prefix = "stat."
stat_cats = ["AP", "CO", "ML", "ME", "OT", "TH"]

tags
