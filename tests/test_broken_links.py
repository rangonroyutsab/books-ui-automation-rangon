import requests
import pytest

from pages.home_page import HomePage
from test_data.constants import BASE_URL
from utils.url_utils import build_absolute_url


@pytest.mark.links
@pytest.mark.regression
def test_homepage_links_are_not_broken(page):
    home_page = HomePage(page)

    home_page.load()

    hrefs = home_page.get_all_links()

    unique_urls = {
        build_absolute_url(BASE_URL, href)
        for href in hrefs
        if not href.startswith("mailto:")
    }

    broken_links = []

    for url in unique_urls:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            broken_links.append((url, response.status_code))

    assert broken_links == []
