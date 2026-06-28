import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from test_data.constants import MAX_IMAGE_PAGES


@pytest.mark.images
@pytest.mark.regression
def test_product_images_are_valid_across_pages(page):
    home_page = HomePage(page)

    home_page.load()

    visited_pages = 0

    while visited_pages < MAX_IMAGE_PAGES:
        images = home_page.product_images

        assert images.count() > 0

        for index in range(images.count()):
            image = images.nth(index)

            expect(image).to_be_visible()

            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            class_name = image.get_attribute("class")

            assert src is not None and src.strip() != ""
            assert alt is not None and alt.strip() != ""
            assert class_name is not None
            assert "thumbnail" in class_name

        visited_pages += 1

        if not home_page.has_next_page():
            break

        home_page.go_to_next_page()
