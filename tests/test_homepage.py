from playwright.sync_api import sync_playwright


def test_pandasail_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://pandasail.com/")

        assert page.title() != ""
        assert page.locator("body").is_visible()

        browser.close()
