import pytest

from pages.home_page import HomePage
from test_data.constants import EXPECTED_HOME_TITLE, EXPECTED_HOME_URL


@pytest.mark.smoke
def test_homepage_loads_successfully(page):
    home_page = HomePage(page)

    home_page.load()

    home_page.expect_url(EXPECTED_HOME_URL)
    home_page.expect_title(EXPECTED_HOME_TITLE)


@pytest.mark.smoke
def test_homepage_headings_are_visible_and_not_empty(page):
    home_page = HomePage(page)

    home_page.load()

    heading_texts = home_page.get_all_heading_texts()

    assert len(heading_texts) > 0

    for text in heading_texts:
        assert text != ""


@pytest.mark.smoke
def test_homepage_books_section_is_visible_and_not_empty(page):
    home_page = HomePage(page)

    home_page.load()

    home_page.expect_books_section_visible()

    assert home_page.get_book_count() > 0
