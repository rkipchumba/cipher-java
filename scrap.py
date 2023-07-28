from bs4 import BeautifulSoup
import requests

url = "https://twitter.com/home"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

elements = soup.find_all(
    class_="css-1dbjc4n r-k4xj1c r-18u37iz r-1wtj0ep")
for element in elements:
    print(element.text)
