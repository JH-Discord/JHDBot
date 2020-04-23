from requests_html import HTML, HTMLSession
import requests
import re

session=HTMLSession()
input=input("Enter the search term\n")
url="https://www.google.com/search?q="+input
r=session.get(url)
if r.status_code==200:
    match = r.html.find('#result-stats', first=True)
    print(match.text)
    results = r.html.find('div.g')
    for i in range(6):
        if i==1:
            continue
        print(results[i].html)
        print("\n\n")
        heading = results[i].find('a', first=True)
        print(heading.html.attrs['h3'])
        print("\n\n")
        link = results[i].find('a', first=True)
        print(link.attrs['href'])
else:
    print("Sorry, unable to fetch results")
       