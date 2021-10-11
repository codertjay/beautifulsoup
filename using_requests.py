from bs4 import BeautifulSoup
import requests

#
# i am supppose to use requests in this place is just because i am working offline
# so if i am using requests it would be
#
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'html.parser')
print(soup.prettify)

"""the article i am using is just a variable so dont get confused when using it
is just for the name=ing convention

"""

# this is to get the whole article tag in the html but i am using  find so it would
#  find only the first article tag but if i used find all it would find the first article
article = soup.find('article')
# print(article.prettify())


# this is just to print all the text in the a tag which is under the article with no div
headline = article.h2.a.text
#print(headline)


# to get the summary which is in a div i would use find and the class name of the div
# to search for the summary
summary = article.find('div',class_='entry-content').p.text
#print(summary)


# the video is in an iframe so we get it by using the article.find('iframe',which
# is in a class called youtube-player) so we only need the src from the iframe so we put src in
# front of the bracket
vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

#in here beacause the youtube link src file contains parameters which are not
#  associated with the video so we have to use the split function and use [num]
# to get thec fdile from the list
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

# so in here i am using a formatted string to input the vid_id in the youtube link
yt_link = f'https://youtube.com/watch?v={vid_id}'
""""""




"""
 now to print the whole headline which is in the article.h2.a.text tag
 the paragraph text which is in the div class which have a class name entry-content
 and the video which is in an iframe and a class of youtube player using a for loop
 in here i am going to use the try except in video so that if a video is missing 
 there wont be any error which can destroy my program
 
 in here i am going to open a csv file i dont know what a csv file means but i would 
 check a csv file is use to save the contrent i am getting from the website
 
"""
"""
csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

at the bottom of this project i would put

csv_writer.writerow([headline,summary,yt_lunk])
csv_file.close()
"""


for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        print(vid_id)

        yt_link = f'https://youtube.com/watch?v={vid_id}'
        print(yt_link)
    except Exception as a:
        yt_link = None

































