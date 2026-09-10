from playwright.sync_api import sync_playwright


def test_pandasail_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://pandasail.com/")

        # Check that the main navigation exists
        navigation = page.locator("nav")
        assert navigation.is_visible()

        browser.close()
