import pytest

from pages.book_detail_page import BookDetailPage
from pages.home_page import HomePage
from test_data.constants import RANDOM_BOOK_COUNT
from utils.random_utils import select_random_items


@pytest.mark.data
@pytest.mark.regression
def test_homepage_book_data_matches_details_page(page):
    home_page = HomePage(page)
    detail_page = BookDetailPage(page)

    home_page.load()

    books = home_page.get_books_data()
    selected_books = select_random_items(books, RANDOM_BOOK_COUNT)

    for book in selected_books:
        home_page.load()

        refreshed_books = home_page.get_books_data()
        matching_book = next(
            item for item in refreshed_books if item["title"] == book["title"]
        )

        home_page.click_book_by_index(matching_book["index"])

        detail_page.expect_loaded()

        assert detail_page.get_book_title() == book["title"]
        assert detail_page.get_book_price() == book["price"]

        page.go_back()
