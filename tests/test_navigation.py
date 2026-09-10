from playwright.sync_api import sync_playwright


def test_pandasail_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://pandasail.com/")

        desktop_menu = page.locator("#menu-1-da35919")

        services_link = desktop_menu.get_by_role(
            "link", name="Services"
        )

        services_link.click()

        assert page.url == "https://pandasail.com/services/"

        browser.close()
