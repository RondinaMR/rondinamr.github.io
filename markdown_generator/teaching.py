
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

teachings = pd.read_csv("../sources/teachings.csv", sep="\t", header=0)
teachings


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
for row, item in teachings.iterrows():
    year = item.date[:4]
    month = item.date[5:7]
    md_filename = year + "-" + month + "-" + item.url_slug + ".md"
    html_filename = year + "-" + month + "-" + item.url_slug

    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += """collection: teaching"""

    md += "\ntype: '" + html_escape(item.type) + "'"
    
    md += """\npermalink: /teaching/""" + html_filename
    
    # if len(str(item.excerpt)) > 5:
    #     md += "\ndescription: '" + html_escape(item.description) + "'"
    
    md += "\ndate: " + str(item.date)
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"

    md += "\nlocation: '" + html_escape(item.location) + "'"

    md += "\nrole: '" + html_escape(item.role) + "'"
    
    # if len(str(item.paper_url)) > 5:
    #     md += "\npaperurl: '" + item.paper_url + "'"
    
    # md += "\ncitation: '" + html_escape(item.citation) + "'"
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    # if len(str(item.paper_url)) > 5:
    #     md += "\n\n<a href='" + item.paper_url + "'>Download paper here</a>\n"
        
    if len(str(item.description)) > 5:
        md += "\n\n" + html_escape(item.description) + "\n"
        
    # md += "\nRecommended citation: " + item.citation
    
    md_filename = os.path.basename(md_filename)
       
    with open("../_teaching/" + md_filename, 'w', encoding='utf-8') as f:
        f.write(md)


