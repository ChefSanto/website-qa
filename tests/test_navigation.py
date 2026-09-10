from playwright.sync_api import sync_playwright


def test_pandasail_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://pandasail.com/")

        print("\nPAGE TITLE:", page.title())
        print("\nLINKS:")

        for link in page.get_by_role("link").all():
            text = link.inner_text().strip()
            href = link.get_attribute("href")

            if text or href:
                print(f" - TEXT: {text!r} | HREF: {href!r}")

        browser.close()
