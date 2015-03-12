import requests
from bs4 import BeautifulSoup
import re

def get_all_review_urls(movie_id):
	"""Returns an array of the URLs of every review for a given movie_id."""

	review_urls = []

	page_num = 1
	page_url = 'http://www.rottentomatoes.com/m/{0}/reviews/?page={1}&sort='.format(movie_id, page_num)
	page_content = requests.get(page_url).content
	
	# Find number of total pages on the first page.
	total_pages = int(re.search(r'Page 1 of ([0-9]+)', page_content).group(1))
	
	for page_num in xrange(1, total_pages + 1):
		page_url = 'http://www.rottentomatoes.com/m/{0}/reviews/?page={1}&sort='.format(movie_id, page_num)
		page_content = requests.get(page_url).content
		url_pattern = re.compile(r'<a href="(.*)"  target="_blank" rel="nofollow"  >Full Review</a>')
		page_urls = re.findall(url_pattern, page_content)
		for url in page_urls:
			review_urls.append(url)

	return review_urls
		
def get_review_text(url):
	content = requests.get(url).content
	soup = BeautifulSoup(content)
	ps = soup.find_all('p')
	text = ''.join([p.text for p in ps])
	return text

# print get_all_review_urls('the_dark_knight_rises')
print get_review_text('http://entertainment.time.com/2012/07/16/times-review-of-the-dark-knight-rises-to-the-depths-to-the-heights/')