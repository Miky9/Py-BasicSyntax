import logging
from datetime import datetime
from urllib.parse import urlparse  # urlparse python2

import requests
from bs4 import BeautifulSoup

from constants import MRP, PRICE, IS_EMI_AVAILABLE, IS_COD_AVAILABLE, IS_PRODUCT_AVAILABLE, EMI_STARTS_AT, RATING, \
    RATING_COUNT, SNAPDEAL_MRP_CLASS, SNAPDEAL_AVAILABILITY_ITEMPROP, SNAPDEAL_EMI_CLASS, SNAPDEAL_COD_ID, \
    SNAPDEAL_EMI_CONSTANT, SNAPDEAL_MERCHANT_NAME, SNAPDEAL_PRICE_ID, RATING_VALUE_ITEMDROP, TRUE, MERCHANT, \
    SNAPDEAL_NETLOC, ERROR_VALUE, ERROR_KEY

logging.basicConfig(
    filename='/tmp/log_{datetime}'.format(datetime=datetime.utcnow().date()),
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def get_item_dict(is_product_available, mrp, price, is_emi_available, emi_starts_at, is_cod_available, rating,
                  rating_count):
    item = {
        MRP: mrp,
        PRICE: price,
        IS_EMI_AVAILABLE: is_emi_available,
        IS_COD_AVAILABLE: is_cod_available,
        IS_PRODUCT_AVAILABLE: is_product_available,
        EMI_STARTS_AT: emi_starts_at,
        RATING: rating,
        RATING_COUNT: rating_count
    }

    return item


def get_snapdeal_item_information(soup):
    try:
        price = float(soup.find('input', attrs={'id': SNAPDEAL_PRICE_ID})['value'])
    except (TypeError, AttributeError, ValueError):
        price = None
    try:
        mrp = float(soup.find('div', attrs={'class': SNAPDEAL_MRP_CLASS}).text.split()[1].replace(",", ""))
    except (TypeError, AttributeError):
        mrp = price
    is_product_available = True if soup.find('link', attrs={'itemprop': SNAPDEAL_AVAILABILITY_ITEMPROP}) else False
    is_emi_available = True if soup.find('span', attrs={'class': SNAPDEAL_EMI_CLASS}) else False
    emi_starts_at = price/SNAPDEAL_EMI_CONSTANT if (price and is_emi_available) else None
    is_cod_available = True if soup.find('input', attrs={'id': SNAPDEAL_COD_ID})['value'] == TRUE else False
    try:
        rating = float(soup.find('span', attrs={'itemprop': RATING_VALUE_ITEMDROP}).text)
    except (TypeError, AttributeError):
        rating = None
    try:
        rating_count = int(soup.find('span', attrs={'itemprop': RATING_COUNT}).text)
    except (TypeError, AttributeError):
        rating_count = 0
    item = get_item_dict(is_product_available, mrp, price, is_emi_available, emi_starts_at, is_cod_available, rating,
                         rating_count)
    item[MERCHANT] = SNAPDEAL_MERCHANT_NAME
    return item


def get_item_info_from_url(url):
    parsed_url = urlparse(url)
    response = requests.get(url, timeout = 15)
    soup = BeautifulSoup(response.text, 'lxml')
    if parsed_url.netloc == SNAPDEAL_NETLOC:
        item_information = get_snapdeal_item_information(soup)
    else:
        item_information = {ERROR_KEY: ERROR_VALUE}
    return item_information

if __name__ == "__main__":
    # sample url like - https://www.snapdeal.com/product/open-box-xiaomi-redmi-note/640411440497
    url = 'https://www.snapdeal.com/product/open-box-xiaomi-redmi-note/640411440497'
    product_information = get_item_info_from_url(url)
    print (product_information)
