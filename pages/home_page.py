from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from test_data.constants import BASE_URL


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.headings = page.locator("h1, h2, h3, h4, h5, h6")
        self.books = page.locator("article.product_pod")
        self.book_links = page.locator("article.product_pod h3 a")
        self.book_prices = page.locator("article.product_pod .price_color")
        self.product_images = page.locator("article.product_pod img")
        self.next_button = page.locator("li.next a")

    def load(self):
        self.navigate_to(BASE_URL)

    def expect_books_section_visible(self):
        expect(self.books.first).to_be_visible()

    def get_book_count(self) -> int:
        return self.books.count()

    def get_all_heading_texts(self) -> list[str]:
        texts = []

        for index in range(self.headings.count()):
            heading = self.headings.nth(index)

            if heading.is_visible():
                texts.append(heading.inner_text().strip())

        return texts

    def get_books_data(self) -> list[dict]:
        books = []

        for index in range(self.books.count()):
            book = self.books.nth(index)
            link = book.locator("h3 a")
            price = book.locator(".price_color")

            books.append(
                {
                    "title": link.get_attribute("title").strip(),
                    "price": price.inner_text().strip(),
                    "href": link.get_attribute("href"),
                    "index": index,
                }
            )

        return books

    def click_book_by_index(self, index: int):
        self.books.nth(index).locator("h3 a").click()

    def get_all_links(self) -> list[str]:
        links = []

        anchors = self.page.locator("a")

        for index in range(anchors.count()):
            href = anchors.nth(index).get_attribute("href")

            if href:
                links.append(href)

        return links

    def has_next_page(self) -> bool:
        return self.next_button.count() > 0 and self.next_button.is_visible()

    def go_to_next_page(self):
        self.next_button.click()
