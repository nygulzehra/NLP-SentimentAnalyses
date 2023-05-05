import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import pandas as pd


URL = []
URL.append("https://www.amazon.com/Apple-iPhone-256GB-Space-Gray/product-reviews/B07YWB338N/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")
page = "https://www.amazon.com/Apple-iPhone-256GB-Space-Gray/product-reviews/B07YWB338N/ref=cm_cr_arp_d_paging_btm_next_"
add = "?ie=UTF8&reviewerType=all_reviews&pageNumber="
for i in range(2, 909):
    URL.append(page + str(i) + add + str(i))


chrome_driver_path = "/Users/zehragul/Documents/Development/chromedriver"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
result = []
reviews = []
stars = []

for i in range(0, len(URL)):
    #  open webpage
    driver.get(URL[i])
    # driver.implicitly_wait(5)
    time.sleep(2)
    # get reviews from page
    soup = BeautifulSoup(driver.page_source, "html.parser")
    review = soup.find_all("span", {"class": "a-size-base review-text review-text-content"})
    #  get stars from page
    soup_text = soup.find_all("div", {"class": "a-section a-spacing-none reviews-content a-size-base"})
    star = soup.find_all(attrs={"data-hook": "review-star-rating"})

    #  get each star
    for j in range(0, len(star)):
        text = star[j].text
        stars.append(text[0:3])
        print(text[0:3])

    #  get each review
    for j in range(0, len(review)):
        reviews.append(review[j].text)
        print(review[j].text)



#  make a list [ review , star]
for i in range(0, len(reviews)):
    new_record = [reviews[i], stars[i]]
    result.append(new_record)

#  make a json file from list
columns = ["review", "star"]
df = pd.DataFrame.from_records(result, columns=columns)
df.to_json("review")

print(f"Total {len(URL)} page and  {len(result)} record.")
