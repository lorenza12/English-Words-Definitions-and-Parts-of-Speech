# English-Words-Definitions-and-Parts-of-Speech
A text file containing English words, along with the definition, parts of speech (noun,verb,adjective,etc.), and a link to the url where the definition was found.

A csv file that is sepetated with the '|' character due to commas causing problems when used the definitions. The order of the values goes: <br> 
word | part of speech | definition (according to dictionary.com) | url

When trying to find a file that had all of these things, I was unable to get everything I wanted. In order to achieve this, a python program was written to load in a word file with a list of words, go to dictionary.com/browse/EACHWORD, parse the html with the BeautifulSoup pyhton module, and store the definition and part of speech. The results are then written to a csv file as mentioned above.

<br>
The python file is also included, but in order for it to work, BeautifulSoup must be installed by using 'pip install beautifulsoup4'. you then need to change both the 'wordsIn' and 'dictionaryOut' variables to point to the location of your desired word file and the location you want the output.
It is important to note that some words will not be found, and they are simply skipped in that case. Words will also be skipped if a non-supported charater is read in through the html. Sometimes the html is read defferently which causes the output to be funny, so double check your results. This obviously makes tons of web requests so speed to vary based on internet speed. 

<br>

+ wordDictionary.txt contains the csv file of all the words, definitions, parts of speech, url
+ DictionaryFiller.py is the python file used to pull the information

<br>
<br>
Please note: This program is not perfect and will throw some errors sometimes that result in funky output to your output file.
The words in wordDictionary.txt file are, for the most part, basic words. I wanted a bunch of words and definitions for a childrens hangman app I am making, so there isn't anything that complex.
