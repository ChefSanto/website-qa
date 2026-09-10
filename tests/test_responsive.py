
from playwright.sync_api import sync_playwright


def test_pandasail_mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page(
            viewport={"width": 390, "height": 844}
        )

        page.goto("https://pandasail.com/")

        # Make sure the page loaded
        assert page.title() != ""
        assert page.locator("body").is_visible()

        # Check that the mobile navigation exists
        mobile_nav = page.locator(".wpr-mobile-nav-menu-container")

        assert mobile_nav.count() == 1

        browser.close()
