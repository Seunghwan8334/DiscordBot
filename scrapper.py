import requests
from bs4 import BeautifulSoup

response = requests.get("https://solved.ac",
    headers={
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

STATUS_CODE = response.status_code

soup = BeautifulSoup(response.content, "html.parser")  