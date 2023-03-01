import cloudscraper

url = "https://www.papara.com/"
scraper = cloudscraper.create_scraper()

response = scraper.get(url)
print(response.text)

# Get all cookies from the response

cookies = response.cookies

# Print the cookies as a dictionary
print(dict(cookies))

# Access an individual cookie by name
__cf_bm = cookies.get('__cf_bm')
__cfruid = cookies.get('__cfruid')
__cflb = cookies.get('__cflb')
