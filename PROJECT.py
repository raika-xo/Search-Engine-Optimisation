#IMPORT EVERTHING YOU NEED TO USE 1)"BS4" 2)"REQUESTS". "BS4" TO SCRAPE HE WEBSITE AND "REQUESTS" TO REQUEST WEBSITE LEGALLY TO USE ITS INFO
# "lxml" IS A TREE STRUCTURE PARSER USED FOR PARSING HTML FILES
# "re" is used to get all text only from body as we are focused on "Keyword SEO"
# "counter" is a module in collection to count number of words. Used the module to reduce lenght of code.
# "xlsxwiter" to save the data in excel sheet and to make a graph
# "sqlite3" to store data as database for further use.

import bs4
from bs4 import BeautifulSoup
import requests
import lxml
import re
from collections import Counter
import xlsxwriter
import pyexcel_xls 
import sqlite3

#MAKING REQUEST AND STORING ALL THE INFO OF WEBSITE INTO A VARIABLE NAMED 'RES'.
res=requests.get(input("Enter URL to start scrapping keywords : "))

#CHECKING WHAT TYPE OF VARIABLE 'RES' IS. WELL THIS IS TYPE IS OF NO USE AS WE CAN'T USE IT TO PARSE CONTENT
"""print(type(res))"""


#WE NEED TO CHANGE THE TYPE TO BEAUTIFUL SOUP TO PARSE THE WEBSITE. SO WE MAKE A VARAIABLE 'SOUP'(ANY OF YOUR CHOICE) AND CALL BS4 WITH ITS METHOD BEAUTIFULSOUP
#IT TAKES TWO ARGUMENTS 1)THE REQUEST 2)THE TREE STRUCTURE YOU WANT IN THIS CASE lxml(pip install this)
soup = bs4.BeautifulSoup(res.text, 'lxml')
"""print(type(soup))"""

#NOW GETTING WHAT WE WANT TO GET FROM WEBSITE
#NOW HERE COMES THE HTML PART. BY GOING ON INSPECT (USING GOOGLE CHROME) WE NEED TO KNOW THE CLASS OR TAG UNDER WHICH REQUIRED INFORMATION HAS BEEN SAVED. IN THIS CASE ALL THE TEXT OR BODY WAS SAVED IN <P></P> SO CLASS P IS USED. WE USED LOOP TO GET ONLY REQUIRED CONTENT FROM THE LIST OF TUPPLES PRODUCED BY BEAUTIFULSOUP
print("Title of page opened : ")
rex=soup.select("title")
print(rex[0].getText())
"""print(soup.select("h1"))"""

#SAVING THE CONTENTS TO A TEXT FILE 


with open('web_info.txt', 'w', encoding='utf-8') as f_out:
    for i in soup.select('p'):
        k=i.text
        f_out.write(k)

#OPENING FILE , SPLITING WORDS , FINDING MAX WORD , MAKING GRAPHS , SAVING IT TO EXCEL AND SQLITE3. REAL JOB BEGINS NOW.


#opening file and finding max word ,converting list into dictionary, deleting unnecessary words and obtaining a final list.
        
words = re.findall(r'\w+', open('web_info.txt').read().lower())
g=Counter(words).most_common(60)
d=dict(g)
#print(d)
#REMOVING UNWANTED WORDS
l=('the', 'of', 'a', 'to', 'and', 'in', 'is', 'that', 'are','s', 'while','had','he','then','their', 'not','as', 'from','for', 'with', 'on', 'be','by', 'an', 'or', 'it', 'can', 'used', 'this', 'which', 'also', 'has', 'some', 'between','often', 'but', 'been')
list(map(d.__delitem__, filter(d.__contains__,l)))
#FINAL NEEDED WORDS AND THEIR FREQUENCY
#print(d)


#CONVERT DICTIONARY TO LIST

v=list(d.values())

k=list(d.keys())

#SAVE IT TO EXCEL
workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1',"       HERE IS A LIST OF MAXIMUM USED WORDS IN YOUR WEBPAGE. YOU SHOULD INCLUDE THESE WORDS IN META DESCRIPTION AND TITLE TO ATTRACT MORE USERS")
worksheet.write('A3',"Words")
worksheet.write('B3',"Frequency")
worksheet.write_column(4,0,k)

worksheet.write_column(4,1,v)

#ADDING A GRAPH

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
#chart.add_series({'values': '=Sheet1!$B$5:$B$30'})
chart.add_series({
    'categories': '=Sheet1!$A$5:$A$30',
    'values':     '=Sheet1!$B$5:$B$30',
    'points': [
        {'fill': {'color': 'green'}},
        {'fill': {'color': 'red'}},
    ],
})

# Insert the chart into the worksheet.
worksheet.insert_chart('E3', chart)
workbook.close()
#FINISHED
print("KEYWORDS HAVE BEEN SCRAPPED ALONG WITH FREQUENCY. CHECK DATA.XLSX ") 
conn=sqlite3.connect('data.db')
#print("opened sucessfuly")
conn.execute(''' CREATE TABLE IF NOT EXISTS DATA
               (ID INT NOT NULL,
               WORDS TEXT NOT NULL,
               FREQUENCY INT NOT NULL)''')

#print("table created")

"""conn.execute('''INSERT INTO DATA(ID,WORDS,FREQUENCY)
            p=1
            for i in range(len(k)):
               VALUES ( p ,k[i],v[i])
               p += 1 ''')
conn.commit()
   
#print("records created")

cursor=conn.execute(" SELECT ID,WORDS,FREQUENCY FROM DATA")
for row in cursor:
    print(" SEQ.NO. : " , row[0])
    print(" WORDS : " , row[1])
    print(" FREQUENCY : " , row[2] , "\n")

conn.close()
              
"""


























