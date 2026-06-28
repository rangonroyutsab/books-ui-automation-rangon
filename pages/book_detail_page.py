from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class BookDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.locator("div.product_main h1")
        self.price = page.locator("div.product_main .price_color")
        self.product_information = page.locator("table.table.table-striped")

    def expect_loaded(self):
        expect(self.title).to_be_visible()
        expect(self.product_information).to_be_visible()

    def get_book_title(self) -> str:
        return self.title.inner_text().strip()

    def get_book_price(self) -> str:
        return self.price.inner_text().strip()
