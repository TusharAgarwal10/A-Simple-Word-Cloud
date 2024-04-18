import os
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader as pdf
import contractions

# for .pdf file type
file = open("C://Users//ASUS//Downloads//Movie Screening Survey (Responses) - Form Responses 2.pdf", "rb")
pdf_read = pdf(file)

text = ""
for page_num in range(len(pdf_read.pages)):
    page = pdf_read.pages[page_num]
    text += page.extract_text()  

# for .txt file type, convert the code block for pdf into comments and un-comming the following line of code
#text = open("file name", "r", encoding="utf-8").read() 

text = contractions.fix(text)

# this line of code excludes certain words from the word cloud. Here, "STOPWORDS" removes filler words like "the," "an," "a," etc.
fillers = STOPWORDS # .update([]) in case you want to exclude specific words #here

wc = WordCloud(stopwords = fillers, height = 1000, width = 1500).generate(text) # add background_color="" as an argument in the Wordcloud() function
# wc.recolor(colormap="") in case you want to change the color fo the 

plt.imshow(wc)
plt.axis("off")
plt.show()


