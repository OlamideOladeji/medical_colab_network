#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:12:50 2017

@author: Ola
"""

# split list of authors
import pandas as pd
import numpy as np
import time
import wos

n_chunks=309
authors = pd.read_csv("pis.csv", header=None)
author_chunks = np.array_split(authors, n_chunks)


text_queries=[]
for df in author_chunks:
    query = " ".join(list(df[0]))[0:-3]
    text_queries.append(query)

# Run query
def run_query(query, query_number):
    print ("Running query %s" % query_number)
    with wos.WosClient() as client:
        client.connect()
        result = wos.utils.query(client, query)
    
    # Save XML
    with open("result_%s.xml" % query_number, "w") as f:
        f.write(result)
    
    print("Done")

# Loop over remaining queries (from 10 to 309)
i = 0    
for query in text_queries[0]:
    start = time.time()
    run_query(query, i)
    i += 1
    end = time.time()
    elapsed = end - start
    if elapsed<300:
        diff=300-elapsed
        time.sleep(diff+1)
        

