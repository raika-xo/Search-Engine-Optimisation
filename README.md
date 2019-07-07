# Search-Engine-Optimisation
Search engine optimization (SEO) is the process of optimizing your online content so that a search engine likes to show it as a top result for searches.

# SEO Keywords
Your SEO keywords are the key words and phrases in your web content that make it possible for people to find your site via search engines. A website that is well optimized for search engines "speaks the same language" as its potential visitor base with keywords for SEO that help connect searchers to your site. Keywords are one of the main elements of SEO.
In other words, you need to know how people are looking for the products, services or information that you offer, in order to make it easy for them to find you—otherwise, they'll land on one of the many other pages in the Google results. Implementing keyword SEO will help your site rank above your competitors.
This is why developing a list of keywords is one of the first and most important steps in any search engine optimization initiative. Keywords and SEO are directly connected when it comes to running a winning search marketing campaign. Because keywords are foundational for all your other SEO efforts, it's well worth the time and investment to ensure your SEO keywords are highly relevant to your audience and effectively organized for action.

# How did this project do it ?
STEP 1:<br>
IMPORT EVERTHING YOU NEED TO USE <br>1)"BS4"<br> 2)"REQUESTS".<br> "BS4" TO SCRAPE HE WEBSITE AND "REQUESTS" TO REQUEST WEBSITE LEGALLY TO USE ITS INFO<br>
•	"lxml" IS A TREE STRUCTURE PARSER USED FOR PARSING HTML FILES<br>
•	"re" is used to get all text only from body as we are focused on "Keyword SEO"<br>
•	"counter" is a module in collection to count number of words. Used the module to reduce lenght of code.<br>
•	"xlsxwiter" to save the data in excel sheet and to make a graph<br>
•	"sqlite3" to store data as database for further use.<br>
STEP 2:<br>
MAKING REQUEST AND STORING ALL THE INFO OF WEBSITE<br>
 By using request.get() function we legally took permission from website to scrap its contents <br>

STEP 3:<br>
SAVING THE CONTENTS TO A TEXT FILE<br>
Making the information accessible in the form of a text file so as to prevent any failure of program incase of disruption of connection <br>and also making it feasible to user.

STEP4:<br>
OPENING FILE , SPLITING WORDS , FINDING MAX WORD , MAKING GRAPHS , SAVING IT TO EXCEL AND SQLITE3<br>
   Opening file and finding max word ,converting list into dictionary, deleting unnecessary words and obtaining a final list.<br>

# Description:

This program will use the following core technologies of python: <br>
●	Urllib <br>
●	beautiful soup <br>
●	xlsxwriter <br>
●	sqlite3<br>
urllib:<br>
urllib.request is a Python module for fetching URLs (Uniform Resource Locators).<br> It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on. <br>These are provided by objects called handlers and openers.
urllib.request supports fetching URLs for many “URL schemes” 
Eg:<br>
import urllib.request<br>
with urllib.request.urlopen('http://python.org/') as response:<br>
   html = response.read()<br>

beautifulsoup:<br>
Given a web-page data, we want to extract interesting information. You could use the BeautifulSoup module to parse the returned HTML data.<br>
You can use the BeautifulSoup module to:<br>
●	Extract links<br>
Web scraping is the technique to extract data from a website.<br>
The module BeautifulSoup  is designed for web scraping. The BeautifulSoup module can handle HTML and XML. It provides simple method for searching, navigating and modifying the parse tree.<br>

from BeautifulSoup import BeautifulSoup<br>
import urllib2<br>
 
 # get the contents
response = urllib2.urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')<br>
html = response.read()<br>
 
parsed_html = BeautifulSoup(html)<br>
print parsed_html.body.find('div', attrs={'class':'toc'})<br>
●	Get data in a div<br>
●	Get images from HTML<br>
To grab all images URLs from a website, we can use this code:<br>
from BeautifulSoup import BeautifulSoup<br>
import urllib2<br>
 
url = 'http://www.arstechnica.com/'<br>
data = urllib2.urlopen(url).read()<br>
soup = BeautifulSoup(data)<br>
links = soup.findAll('img', src=True)<br>
 
for link in links:<br>
    print(link["src"])<br>

xlsxwriter:<br>

XlsxWriter is a Python module that can be used to write text, numbers, formulas and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file.<br>
XlsxWriter has some advantages and disadvantages over the alternative Python modules for writing Excel files.<br>
●	Advantages:<br>
○	It supports more Excel features than any of the alternative modules.<br>
○	It has a high degree of fidelity with files produced by Excel. In most cases the files produced are 100% equivalent to files produced by Excel.<br>
○	It has extensive documentation, example files and tests.<br>
○	It is fast and can be configured to use very little memory even for very large output files.<br>
●	Disadvantages:<br>
○	It cannot read or modify existing Excel XLSX files.<br>
sqlite3:<br>
SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.<br> It is a database, which is zero-configured, which means like other databases you do not need to configure it in your system.<br>
SQLite engine is not a standalone process like other databases, you can link it statically or dynamically as per your requirement with your application. SQLite accesses its storage files directly.
Following Python code shows how to connect to an existing database. If the database does not exist, then it will be created and finally a database object will be returned.
#!/usr/bin/python

import sqlite3<br>

conn = sqlite3.connect('test.db')<br>

print "Opened database successfully";<br>


