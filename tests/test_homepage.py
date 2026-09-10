from playwright.sync_api import Page


def test_pandasail_homepage(page: Page):
    page.goto("https://pandasail.com/")

    assert page.title() != ""
    assert page.locator("body").is_visible()
