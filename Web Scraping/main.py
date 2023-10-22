from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get(url='https://news.ycombinator.com/')
contents = response.text

soup = BeautifulSoup(contents, 'lxml')
article_titles_raw = soup.select('.titleline')
article_titles = [title_line.find(name='a').string for title_line in article_titles_raw]
article_links = [title_line.find(name='a').get('href') for title_line in article_titles_raw]
article_upvote = [int(score.text.split(' ')[0]) for score in soup.find_all(name='span', class_='score')]
sorted_result = [title for vote, title, link in
                 sorted(zip(article_upvote, article_titles, article_links),reverse=True)]
print(sorted_result)










# with open(file='website.html', mode='r+', encoding='utf8') as data:
#     content = data.read()
# soup = BeautifulSoup(content, 'lxml')
# print(soup.title.string)
# # print(soup.prettify())
#
# # print(soup.findAll(name='a'))
# # name = soup.find(name='h1', id='name').string
# # heading = soup.find(name='h3', class_='heading').name
#
# # company_url = soup.select_one(selector='p a')
# # company_url = soup.select_one(selector='#name')
# company_url = soup.select_one(selector='.heading')
#
# print(company_url)
