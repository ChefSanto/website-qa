from playwright.sync_api import sync_playwright


def test_pandasail_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://pandasail.com/")

        services_link = page.get_by_role("link", name="Services")

        services_link.click()

        assert page.url == "https://pandasail.com/services/"

        browser.close()
