from playwright.sync_api import sync_playwright


def test_mobile_navigation_inspection():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page(
            viewport={"width": 390, "height": 844}
        )

        page.goto("https://pandasail.com/")

        print("\nMOBILE NAVIGATION ELEMENTS:")

        for nav in page.locator("nav").all():
            print(
                " - CLASS:",
                nav.get_attribute("class"),
                "| VISIBLE:",
                nav.is_visible()
            )

        browser.close()
