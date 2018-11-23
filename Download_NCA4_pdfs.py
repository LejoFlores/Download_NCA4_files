#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:39:32 2018

@author: lejoflores (lejoflores@boisestate.edu)

"""

import bs4 # BeautifulSoup4
import urllib.request 
import urllib.parse

# Base name for NCA4 report
NCA4_url_base = 'https://nca2018.globalchange.gov'

# Local path to where this code lives
LocalPath = '/Users/lejoflores/Download_NCA4_pdfs'

# A subfolder within LocalPath where the outputs will be downloaded
OutputDir = '/NCA4_files/'

# Open the URL for the doanloads directory
nca4_html = urllib.request.urlopen(NCA4_url_base+'/downloads/')

# Store output in a BeautifulSoup class
nca4_soup = bs4.BeautifulSoup(nca4_html,'lxml')


# Loop through all the 'a' refs in the HTML
for link in nca4_soup.findAll('a'):
    filelink = link.get('href') # Get the link of the URL
    
    # Check to see if this URL link contains either .pdf or .pptx
    if((filelink.find('.pdf')>0) | (filelink.find('.pptx')>0)):
        print('Downloaded from: '+filelink)
        print('Downloaded to: '+LocalPath+OutputDir+filelink.split('/')[-1])
        
        # Download the PDF or PPTX file... catch exceptions (as of 11/23 some links were dead) 
        try:
            urllib.request.urlretrieve(NCA4_url_base+filelink,LocalPath+OutputDir+filelink.split('/')[-1])
        except urllib.request.URLError as e:
            print(e)
            continue
        
        
        