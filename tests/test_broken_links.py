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

    unique_urls = sorted(
        {
            build_absolute_url(BASE_URL, href)
            for href in hrefs
            if href
            and not href.startswith("#")
            and not href.startswith("mailto:")
            and not href.startswith("javascript:")
            and not href.startswith("tel:")
        }
    )

    broken_links = []

    for url in unique_urls:
        response = page.request.get(url, timeout=10_000)

        if response.status != 200:
            broken_links.append((url, response.status))

    assert broken_links == [], f"Broken links found: {broken_links}"
