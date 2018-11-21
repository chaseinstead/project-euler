import requests
from bs4 import BeautifulSoup

url = "https://projecteuler.net/problem=13"
selector = "font-family:'courier new';font-size:10pt;text-align:center;"

response = requests.get(url)
print("Site fetched with http status code {}".format(response.status_code))

html = BeautifulSoup(response.text, "lxml")
div = html.find("div", {"style": selector}).text
problem_content = [int(i) for i in div.replace("\n", " ").split()]

solution = str(sum(problem_content))[:10]
print("Solution to Euler # 13: {}.".format(solution))