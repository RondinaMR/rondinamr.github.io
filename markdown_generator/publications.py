
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


import pandas as pd
import json

# publications = pd.read_csv("sources/publications.csv", sep="\t", header=0)
with open("sources/publications.json", 'r') as f:
    publications = json.load(f)
publications = publications['publications']

# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

import os

for item in publications:
    md_filename = str(item["pub_date"]) + "-" + item["url_slug"] + ".md"
    html_filename = str(item["pub_date"]) + "-" + item["url_slug"]
    year = item["pub_date"][:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + item["title"] + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publication/""" + html_filename
    
    if len(str(item["excerpt"])) > 5:
        md += "\nexcerpt: '" + html_escape(item["excerpt"]) + "'"
    
    md += "\ndate: " + str(item["pub_date"]) 
    
    md += "\nvenue: '" + html_escape(item["venue"]) + "'"
    
    if len(str(item["preprint_url"])) > 5:
        md += "\npreprinturl: '" + item["preprint_url"] + "'"

    if len(str(item["paper_url"])) > 5:
        md += "\npaperurl: '" + item["paper_url"] + "'"
    
    if len(str(item["pdf_url"])) > 5:
        md += "\npdfurl: '" + item["pdf_url"] + "'"
    
    md += "\ncitation: '" + html_escape(item["citation"]) + "'"

    md += "\nauthors: '" + html_escape(item["authors"]) + "'"
    
    md += "\n---\n"
    
    ## Markdown description for individual page
    # if len(str(item["pdf_url"])) > 5:
    #     md += "\n\n<a href='" + item["pdf_url"] + "'>Download paper here</a>\n" 
    # elif len(str(item["paper_url"])) > 5:
    #     md += "\n\n<a href='" + item["paper_url"] + "'>Download paper here</a>\n" 

    if len(str(item["image"])) > 3:
        md += f"<p align=\"center\"><img src=\"{item['image']}\" alt=\"{item['title']}\"></p>\n"

    if len(str(item["excerpt"])) > 5:
        md += "\n<h2>Abstract</h2>\n"
        md += "\n" + html_escape(item["excerpt"]) + "\n"
        
    # md += "\nRecommended citation: " + item["citation"]
    
    md_filename = os.path.basename(md_filename)
       
    with open("_publications/" + md_filename, 'w', encoding='utf-8') as f:
        f.write(md)


