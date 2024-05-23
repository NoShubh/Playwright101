from playwright.sync_api import sync_playwright

def test_input_form_submit():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.lambdatest.com/selenium-playground")
        page.locator("#inputFormSubmit").click()
        page.locator("#submit-form").click()

        error_message = page.locator("#user-message").inner_text()
        assert error_message == "Please fill in the fields."

        page.locator("#name").fill("John Doe")
        page.locator("#email").fill("johndoe@example.com")
        page.locator("#subject").fill("Test Subject")
        page.locator("#message").fill("Test Message")

        page.locator("#country").select_option("text=United States")

        page.locator("#submit-form").click()

        success_message = page.locator("#user-message").inner_text()
        assert success_message == "Thanks for contacting us, we will get back to you shortly."

        page.wait_for_timeout(3000)

        browser.close()

test_input_form_submit()