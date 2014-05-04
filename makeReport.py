import feedparser
import google
import time

import tfidf_search

def writeDailyReport():
	date = (time.strftime("%d-%m-%Y")+'.txt')
	f = open(date, 'w')
	rss_url = "http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=m&output=rss"
	feed = feedparser.parse(rss_url)

	for item in feed.entries:
	    f.write('-'*80 + '\n')
	    title, source = item.title.split(' - ')
	    searchstring = tfidf_search.striptext(title + item.description)
	    f.write(title+'\n')
	    for score, url in tfidf_search.search(searchstring):
	        f.write(str(score) + '\n')
	        newUrl = url.replace("$", "/")
	        newUrl = "http://www.cdc.gov/" + newUrl
	        newUrl = newUrl[0:-5]
	        f.write(newUrl + '\n')
	        break
	    else:
	        f.write('No relevant URLs' + '\n')

if __name__ == "__main__":
	writeDailyReport();
