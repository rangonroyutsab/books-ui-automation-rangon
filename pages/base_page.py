from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)

    def get_current_url(self) -> str:
        return self.page.url

    def get_title(self) -> str:
        return self.page.title()

    def expect_url(self, expected_url: str):
        expect(self.page).to_have_url(expected_url)

    def expect_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)

    def get_visible_texts(self, selector: str) -> list[str]:
        elements = self.page.locator(selector)
        texts = []

        for index in range(elements.count()):
            element = elements.nth(index)

            if element.is_visible():
                text = element.inner_text().strip()
                texts.append(text)

        return texts
