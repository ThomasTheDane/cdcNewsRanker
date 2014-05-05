import feedparser
import google
import time

import tfidf_search

def writeDailyReport():
	date = (time.strftime("%d-%m-%Y")+'.html')
	f = open(date, 'w')
	rss_url = "http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=m&output=rss"
	feed = feedparser.parse(rss_url)

	for item in feed.entries:
	    f.write("<html><body>")
	    f.write("<h4>"+('-'*80) + '</h4>\n')
	    title, source = item.title.split(' - ')
	    searchstring = tfidf_search.striptext(title + item.description)
	    f.write("<h1>"+title+'</h1>\n')
	    for score, url in tfidf_search.search(searchstring):
	        f.write('<h3>correlation score: '+str(score) + '</h3>\n')
	        newUrl = url.replace("$", "/")
	        newUrl = "<h3>http://www.cdc.gov/" + newUrl
	        newUrl = newUrl[0:-5]
	        newUrl = newUrl  + "</h3>"
	        f.write(newUrl + '\n')
	        break
	    else:
	        f.write('No relevant URLs' + '\n')
        f.write('</body></html>')

if __name__ == "__main__":
	writeDailyReport();
