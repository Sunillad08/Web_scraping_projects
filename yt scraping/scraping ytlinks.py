from bs4 import BeautifulSoup as bs
import datetime

'''
change path of on this line to path of your html data file!
format : r"{path}"
'''
with open(r"C:\Users\DELL\Documents\web scraping training\yt scraping\data.html",encoding="utf8") as f:
    soup = bs(f , "html.parser")

video_div = soup.find_all("div", class_="style-scope ytd-video-renderer" , id = "dismissible")

# getting date and time
date = datetime.datetime.now()
file_name = f"{date.day}-{date.month}-{date.year}.txt"

'''
change path where you want to save your output file
format : r"{path}"
'''
with open(f"C:\\Users\\DELL\\Documents\\web scraping training\\yt scraping\\outputs\\{file_name}" , "a" ,encoding="utf8") as f:
    
    f.write(f"{date}\n\n")

    for data in video_div:
        
        # link of video
        link = data.find(id="thumbnail", class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail")["href"]
        f.write(f"Link : https://www.youtube.com/{str(link)}\n")

        # title
        title = data.find(class_="style-scope ytd-video-renderer", id="title-wrapper").text.strip()
        f.write(f"Title : {str(title)} \n") 

        #channel name
        channel_name = data.find(class_="yt-simple-endpoint style-scope yt-formatted-string").text
        f.write(f"Channel : {str(channel_name)} \n") 

        #duration of video
        duration = data.find("span" , class_="style-scope ytd-thumbnail-overlay-time-status-renderer").text.strip()
        f.write(f"Duration : {str(duration)}\n")

        # views and upload time
        try: # if both views and upload time are in format
            views , upload_time = data.find_all("span" , class_="style-scope ytd-video-meta-block")
            f.write(f"Views : {views.text} \nUploaded : {upload_time.text}\n")
        except Exception: # if upload time is not found
            views = data.find("span" , class_="style-scope ytd-video-meta-block")
            upload_time = "Not Found"
            f.write(f"Views : {views.text} \nUploaded : {upload_time}\n")

        # Thumbnail Image
        try:
            img_src = data.find("img",class_="style-scope yt-img-shadow")["src"]
        except Exception:
            img_src = "Image source not found!"
        f.write(f"Thumbnail : {img_src}") # image link

        #end of line
        f.write("\n\n")


