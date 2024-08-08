
# coding: utf-8

# # Teaching markdown generator for academicpages
# 
# Takes a CSV of teachings with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
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


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:
# teachings = pd.read_csv("../sources/teachings.csv", sep="\t", header=0)
import json
with open("sources/teachings.json", 'r') as f:
    teachings = json.load(f)
teachings = teachings['courses']
# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

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
# This is where the heavy lifting is done. This loops through all the rows in the CSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

import os
import json

# open the

for course in teachings:
    course['editions'] = sorted(course['editions'], key=lambda e: e['date'], reverse=True)
    for edition in course['editions']:
        md_filename = f"{course['url_slug']}-{edition['academic-year']}.md"

        ## YAML variables
        md = "---\ntitle: \"" + course['title'] + '"\n'
        md += """collection: teaching"""
        md += "\ntype: '" + html_escape(course['type']) + "'"
        md += """\npermalink: /teaching/""" + course['url_slug'] + "-" + edition['academic-year']
        # if len(str(item.excerpt)) > 5:
        #     md += "\ndescription: '" + html_escape(item.description) + "'"
        md += "\nvenue: '" + html_escape(course['venue']) + "'"
        md += "\nlocation: '" + html_escape(course['location']) + "'"
        
        
        md += "\ndate: " + edition["date"]
        md += "\nrole: '"+ html_escape(edition["role"]) + "'"
        md += "\nacademic-year: '" + html_escape(edition['academic-year']) + "'"
        md += "\n---"    

        ## Markdown description for individual page
        md += "\n\n"
        if len(str(course['description'])) > 5:
            md += html_escape(course['description']) + "\n"
        # for edition in course['editions']:
        #     md += "\n* " + str(edition['academic-year']) + ", " + html_escape(edition['role'])

        md_filename = os.path.basename(md_filename)
        with open("_teaching/" + md_filename, 'w', encoding='utf-8') as f:
            f.write(md)


    



