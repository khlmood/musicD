# musicD
Looking for a fast, reliable, and extremely easy-to-use music downloader? Look no further than musicD! 
With musicD, you can quickly and easily download all your favorite tunes from popular music platforms. 
Not only is musicD incredibly fast and reliable, but it's also incredibly user-friendly, making it the perfect choice for music lovers of all skill levels. 
So why wait? Give musicD a try today and start downloading your favorite music in no time!

# How to use
**Take control of your music downloads by specifying exactly where you want your tunes to be saved.**

![img2](https://user-images.githubusercontent.com/99619908/221991790-5a33b2c5-a7e5-4990-9d18-8f6917cc0f13.jpg)

**No more endless scrolling or fruitless searches. Just type in the name of the artist or songs you're after and let musicD do the rest.**

![img1](https://user-images.githubusercontent.com/99619908/221991858-0f42ff30-1bc8-4a0f-b64a-8407a15b4a96.png)

**With musicD, you're in complete control of your music library. Simply select the songs you want by ticking the boxes next to them.**

![img3](https://user-images.githubusercontent.com/99619908/221991932-2d38cb6f-9e35-4879-bfc2-923221a13639.jpg)

**Once you're happy with your selection, just hit the download button and let musicD do the rest. It's that easy!**

# How does it work?
The GUI was built using the Python library Custom Tkinter, which is a modern-looking version of the original Tkinter library. 
After entering the artist's name and clicking on the search button, a request is sent to the iTunes API website to retrieve information. 
The retrieved information is then analyzed and the relevant details are stored in an array which is displayed to the user. 
After selecting the desired songs by checking the checkboxes and clicking on the download button, 
musicD opens Google Chrome in the background and navigates to the website https://www.mp3juices.cc/2d0851 using the Selenium library for web scraping. 
The selected music files are then downloaded one by one before the browser is closed.
