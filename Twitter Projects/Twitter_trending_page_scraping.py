from bs4 import BeautifulSoup as bs
import datetime
import os

'''
change path of on this line to path of your html data file!
format : r"{path}"
example : r"C:\Download\folder\data.html"
'''
# reading data form file
with open(r"C:\Users\DELL\Documents\web scraping training\Twitter Projects\data files\data.html" , encoding="UTF8") as f:
    soup = bs(f , 'html.parser')

# creating small blocks of data to scan each trend's info
source = soup.find_all(class_="css-1dbjc4n r-16y2uox r-bnwqim")

# getting date and time
date = datetime.datetime.now()

# creating particular file name
file_name = f"{date.day}-{date.month}-{date.year}.txt"

'''
change path where you want to save your output file
format : r"{path}"
example : r"C:\Download\folder\text.txt"
'''
# looping over every data and writing it in file
with open(f"C:\\Users\\DELL\\Documents\\web scraping training\\Twitter Projects\\outputs\\{file_name}" , "a", encoding="UTF8") as f:

    # adds timestamp in file
    f.write(f"{date.day}-{date.month}-{date.year} {date.hour}:{date.minute}:{date.second}\n")

    # looping over every trend
    for data in source:
        
        # trending in section for / in country
        main_topic = data.find(class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
        f.write(f"\n{main_topic.text}")

        # trending topic 
        topic = data.find(class_="css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-vmopo1 r-qvutc0")
        f.write(f"\n{topic.text}")

        # number of tweets
        no_of_tweets = data.find(class_="css-901oao r-m0bqgq r-1qd0xha r-n6v787 r-16dba41 r-1cwl3u0 r-14gqq1x r-bcqeeo r-qvutc0")
        try:
            f.write(f'\n{no_of_tweets.text}')
        except:
            # some trending topic might have no tweets count so ,
            f.write("\nCounting..!!")

        f.write("\n")

    f.write("\n")
