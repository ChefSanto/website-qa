from playwright.sync_api import sync_playwright


def test_pandasail_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://pandasail.com/")

        # Check that important navigation links exist
        assert page.get_by_role("link", name="Home").is_visible()
        assert page.get_by_role("link", name="About").is_visible()
        assert page.get_by_role("link", name="Contact").is_visible()

        browser.close()
