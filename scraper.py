# import requests
# from bs4 import BeautifulSoup
# # abc ="https://www.youtube.com/"
# # abc ="https://edunetfoundation.org/"
# # abc="https://web.whatsapp.com/"
# abc="https://sarkariresult.com.im/"
# response =requests.get(abc)
# if  response.status_code ==200:
#     print("Successfully fetchd webpage.")
# else:
#     print("Error fetching page")

# html_content = response.text
# if html_content:

#     soup = BeautifulSoup(html_content, "html.parser")
#     title=soup.title.string
#     print(title)
# #EXTRACT ALL HEADINGS (H1-H6)
# for i in range(1,7):
#     for heading in soup.find_all(f"h{i}"):
#         print(f"heading{i}{heading.get_text(strip=True)}")

#Extract all Content in Webpage
# for paragraph in soup.find_all("p"):
#     print(paragraph.get_text(strip=True))

#Extract all Links in Webpage
# for a in soup.find_all("a"):
#     text=a.get_text(strip=True)
#     href=a["href"]
#     print(text , href)

#Extract image
# for img in soup.find_all("img"):
#     src=img["src"]
#     print(src)


import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


quotes=soup.find_all("span", class_="text")
authors = soup.find_all("small", class_='author')

print("Quotes from the page:")
for q,a in zip(quotes, authors):
    print(f"{q.get_text()} - {a.get_text()}")

