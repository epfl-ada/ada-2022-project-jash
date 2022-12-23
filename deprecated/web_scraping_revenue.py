import pandas as pd
import numpy as np
import argparse

import requests
from bs4 import BeautifulSoup
import re

def scraping_values(soup, attributes):
    """This function is used to scrape particular attributes from webpages."""
    attribute_dict = {}
    normal = True  # flag to show whether the value is in dollar.
    empty = True # flag to show whether the movie has budget or gross data.

    for i in range(len(attributes)):
        try:
            value = soup.find_all('li', attrs={'data-testid': f'title-boxoffice-{attributes[i]}'})[0].div.ul.li.label.text.split(" ")[0]
            if value.startswith("$"):
                attribute_dict[attributes[i]] = int(value[1:].replace(",", ""))
            else:
                attribute_dict[attributes[i]] = value
                normal = False
            empty = False
        except:
            attribute_dict[attributes[i]] = "NA"
    
    return attribute_dict, empty, normal

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', required=True, type=int)

    config = parser.parse_args()

    dataset = pd.read_csv('./data/actor_movie_combi.csv', sep=',')
    filtered_movies = list(dataset[dataset["startYear"] >= 1977]["tconst"].unique())
    temp_dataset = filtered_movies[config.index*10000:(config.index+1)*10000]

    headers = {
        'authority': 'www.imdb.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'ubid-main=134-2457033-3328462; _gcl_au=1.1.1240392916.1671623441; uu=eyJpZCI6InV1MTljYjBjN2M2NGIxNDM3MGFmOWMiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-id=132-9104638-2602903; _uetsid=b201d760812511edb1c173c28205e682; _uetvid=b2023d60812511eda00d4bfa409b648d; session-id-time=2082787201l; session-token=fR2NwJcCdHJ6KfiMWEo4Z19rX4XCLsIxF9LEnomVgw1g8mO4qGfF0ChE2EzG5PEbMJfv/bb2DT95oo3WDdicZTEm3gjoiQjdKHD6TvOxFc4BnIHNB3+noazoV5MxcO8cJK5cvxf0x2iI2tmb47Qh/nStfNAO3B12YJhjUg529J3LeTjLdTijnYP5CYgdWKksJ/Kdgk+AxFoazRf98G+9Hw==; csm-hit=tb:PM6ZQFAWZD0JK3RETJVW+s-PM6ZQFAWZD0JK3RETJVW|1671659311034&t:1671659311034&adb:adblk_no',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    attributes = ["budget", "grossdomestic", "openingweekenddomestic", "cumulativeworldwidegross"]
    movies = []
    outliers = []

    for i in range(len(temp_dataset)):
        movie_id = temp_dataset[i]
        response = requests.get(f'https://www.imdb.com/title/{movie_id}/', headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        attribute_values, empty, normal = scraping_values(soup, attributes)
        if not empty:
            attribute_values["tconst"] = movie_id
            if normal:
                movies.append(attribute_values)
            else:
                outliers.append(attribute_values)

    if len(movies) > 0:
        revenue_data_per_movie = {}
        attributes += ["tconst"]
        for attr in attributes:
            revenue_data_per_movie[attr] = [movie[attr] for movie in movies]

        revenue_data_per_movie = pd.DataFrame(revenue_data_per_movie)
        revenue_data_per_movie.to_csv(f"data/revenue_data_per_movie_{config.index}.csv")
    else:
        print("No movie has revenue data in this sweep.")

    if len(outliers) > 0:
        revenue_outliers = {}
        if "tconst" not in attributes:
            attributes += ["tconst"]
            
        for attr in attributes:
            revenue_outliers[attr] = [outlier[attr] for outlier in outliers]

        revenue_outliers = pd.DataFrame(revenue_outliers)
        revenue_outliers.to_csv(f"data/revenue_outliers_{config.index}.csv")

if __name__ == '__main__':
    main()