from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://0.0.0.0:8000")

    # Scroll to the contact section
    contact_section = page.locator("#contact")
    contact_section.scroll_into_view_if_needed()

    # Take a screenshot
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)