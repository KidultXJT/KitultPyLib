#!usr/bin/python
# -*- coding:utf-8 -*-

## --------------------------------------------------------
## Author: Kidult
## Email : junting.xie@sagene.com.cn
## Date  : 2017-09-26
## --------------------------------------------------------
## Description: 
## DownLoad Sequence From NCBI. 

# module
from optparse import OptionParser
from pandas import Series, DataFrame
import pandas as pd
import sys
import os
import re

# BioPython
from Bio import Entrez
# urllib
try:
	from urllib.error import HTTPError
except ImportError:
	from urllib2 import HTTPError

def NCBIDownLoadSeq(
		email="junting.xie@sagene.com.cn",
		orgn=None,  # DownLoad All, WhenYou provide a Unique ID for NCBI
		ID=None,    # ID can Be Everythings:: AssesionID
		Top=1,
		out=os.path.abspath(".") 
		): # Unhappy Face
	# Description:
	# Use BioPython To DownLoad NCBI Sequence By An/Some Informations, Such As "AssesionID", "GeneSymbol" and So on.
	# Try "Top" Argument, if You Don't have Enough Information, Or You might DownLoad So Many Things
	Entrez.email = str(email)
	# search Sequence
	if orgn == "":
		# Including orgn Info or Not 
		search_handle = Entrez.esearch(
				db="nucleotide",
				term="{ID}".format(ID= ID),
				usehistory="y", 
				idtype="acc")
	else:
		search_handle = Entrez.esearch(
				db="nucleotide",
				term="{orgn}[orgn] and {ID}".format(orgn=orgn,ID=ID),
				usehistory="y", 
				idtype="acc")
	search_results = Entrez.read(search_handle)
	search_handle.close()
	# Get accecpt list
	acc_list = search_results["IdList"]
	count = int(search_results["Count"])
	count == len(acc_list)
	print "There Are {count} Result in This Search !!".format(count = count)
	if int(count) > Top:
		count = Top
		print "You Select Top {Top} Sequence To DownLoad !!".format(Top = Top)
	else:
		count = count
		print "Don't Have {Top} match in The Result !! Prp To Download ALL the Result({count}) From The DB.".format(Top = Top, count = count)
	webenv = search_results["WebEnv"]
	query_key = search_results["QueryKey"]
	# DownLoad 1 sequence each Times
	batch_size = 1
	fa_out = open(os.path.abspath(out)+"/"+ID+".fa", "w")
	gb_out = open(os.path.abspath(out)+"/"+ID+".gb", "w")
	for start in range(0, count, batch_size):
		#end = min(count, start+batch_size)
		#print("Going to download record %i to %i" % (start+1, end))
		attempt = 0
		while attempt < 1:
			attempt += 1
			# It might be no item.
			try:
				fa_handle = Entrez.efetch(db="nucleotide",
										  rettype="fasta", retmode="text",
										  retstart=start, retmax=batch_size,
										  webenv=webenv, query_key=query_key,
										  idtype="acc")
				
				gb_handle = Entrez.efetch(db="nucleotide",
										  rettype="gb", retmode="text",
										  retstart=start, retmax=batch_size,
										  webenv=webenv, query_key=query_key,
										  idtype="acc")
			except HTTPError as err:
				if 500 <= err.code <= 599:
					print("Received error from server %s" % err)
					print("Attempt %i of 3" % attempt)
					time.sleep(15)
				else:
					raise
		fa = fa_handle.read()
		fa_handle.close()
		fa_out.write(fa)
		gb = gb_handle.read()
		gb_handle.close()
		gb_out.write(gb)
	fa_out.close()
	gb_out.close()


