'''
    File name: DictionaryFiller.py
    Author: lorenza12
    Date created: 4/18/2018
    Date last modified: 4/22/2018
    Python Version: 3.6.4
'''

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq



def main():

	#Change this with full directory to wordfile
	wordsIn = open("C:/Users/You/wordsIn.txt", 'r')

	dictionaryOut = open("C:/Users/You/dictionaryOut.txt", 'w')

	#for display purposes to see progress as long as wordIn is in alphabetical order
	previous_line_letter = None
	print("Running...")
	for line in wordsIn:
		#strip newline and spaces
		line_letter = line.strip()[0]

		#for display progress
		if(line_letter != previous_line_letter):
			print("Looking up", line_letter.upper(), "words")

		#make url from word
		word_url = "http://www.dictionary.com/browse/" + line.strip()
		wordtype, definition = GetDefinition(word_url)
		

		try:
			#if the word exists or wasnt an error 
		    if(wordtype != None and definition != None):
			    dictionaryOut.write(line.strip() +'|'+ wordtype +'|'+ definition+'|'+ word_url+'\n')
			    
		except Exception as e:
			#errors may be throw if encounter characters that arent supported
			print(e)
			print()

		previous_line_letter = line_letter
	
	#close files	
	wordsIn.close()
	dictionaryOut.close()
	print("Done")





def GetDefinition(url):
	#Will throw error if word not found - i.e 404 page not found
	try:
		#Opening up connection and grabbing the page
		uClient = uReq(url)
		
		#read html
		page_html = uClient.read()

		#parse html with BeautifulSoup import
		page_soup = soup(page_html, "html.parser")


		#grab the source-data tag in html which hold wordtype (verb, adjective, noun, etc.)
		wordtype_content = page_soup.findAll("div", {"class", "source-data"})
		
		#store the text of the wordtype that is nested under div->span
		wordtype_text = wordtype_content[0].div.span.text
		

		#grab the def-content tag in html which holds definition
		definition_content = page_soup.findAll("div", {"class": "def-content"})
		
		#Stored in first item of array
		definition_class = definition_content[0]

		#remove unwanted spaces
		#example sentences are provides after ':' but stop before that
		definition_text = definition_class.text.strip().replace("  ", "").partition(":")
		
		#text is stored in the first (zero) index 
		definition_text = definition_text[0]

		

		#Close client
		uClient.close()
		
		return wordtype_text,definition_text

	except:
		#if word doesnt exit or error return none
		return None, None

main()

