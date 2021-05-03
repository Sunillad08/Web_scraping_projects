from bs4 import BeautifulSoup as bs

# opening data file to read html data
'''
change path to your html data file
format = r"{path}"
'''
with open(r'C:\Users\DELL\Documents\web scraping training\instagram scrach\data files\davyash.html' , encoding="utf8") as f:
    data = bs(f , "html.parser")

# getting section of data
info_section = data.find("section" , class_="zwlfE")

# getting username
username = info_section.find("h2")
# creating file name from usernamej
file_name = f"{username.text}.txt"

# opening file to right output
'''
change path to any desired text file
format = r"{path}"
'''
with open(f'C:\\Users\\DELL\\Documents\\web scraping training\\instagram scrach\\outputs\\{file_name}' , "w" , encoding="utf8") as f:
    # username written
    f.write(f"Username = {username.text}")

    # link of profile
    f.write(f"\n\nProfile page = https://www.instagram.com/{username.text}/")
    
    # link for profile pic
    profile_pic = data.find('img' , class_="_6q-tv")
    f.write(f"\n\nProfile pic link : {profile_pic['src']}")

    # bio written in file
    bio_info = info_section.find("div" , class_="-vDIg")
    bio = bio_info.text
    bio = bio.split("Followed")
    f.write(f"\n\nBio:\n{bio[0]}")

    # post count , followers and following 
    interaction_info = info_section.find('span' , class_="-nal3 ")
    temp = info_section.ul.find_all("li")
    temp_arr = []
    for i in temp:
        temp_arr.append(i.text)

    f.write(f"\n\nPost count : {temp_arr[0]}")
    f.write(f"\n\nFollowers : {temp_arr[1]}")
    f.write(f"\n\nFollowing: {temp_arr[2]}")
    
    # Information scanned in html file about post's of account
    f.write("\n\nPost information :")
    post_3 = data.find_all('div' , class_="Nnq7C weEfm")
    # if 0 posts
    if len(post_3) == 0:
        f.write("0 Posts")

    # going through each posts
    for posts in post_3:
        # creating sections
        f.write("\n\n--------------------------------------")

        # post link
        post_link = posts.find('a')
        link = f"https://www.instagram.com{post_link['href']}"
        try:
            f.write(f"\n\nPost link : {link}\n")
        except Exception:
            f.write(f"\n\nPost link : None")

        # Thumbnail image
        post = posts.find('div' ,  class_="KL4Bh") 
        try:
            f.write(f"\n\nThumbnail : {post.img['src']}")
        except Exception:
            f.write(f"\n\nThumbnail : None")
        
        # Post title : comment by user who uploaded
        try:
            f.write(f"\n\nPost description : {post.img['alt']}")
        except Exception:
            f.write(f"\n\nPost Title : None")