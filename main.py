from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    page.goto('https://www.example.com')
    title = page.title()
    print(title)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)



