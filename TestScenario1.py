from playwright.sync_api import Page, expect

def test_simple_form_demo(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.lambdatest.com/selenium-playground")

    page.click("text=Simple Form Demo")

    expect(page).to_have_url(page.url.contains("simple-form-demo"))

    message = "Welcome to LambdaTest"

    page.fill("id=user-message", message)

    page.click("id=showInput")

    expect(page.inner_text("id=message")).to_equal(message)
    page.wait_for_timeout(3000)

    browser.close()