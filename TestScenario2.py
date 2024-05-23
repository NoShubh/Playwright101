import asyncio
from playwright.async_api import Playwright, async_playwright

async def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.lambdatest.com/selenium-playground")

    await page.click("text=Drag & Drop Sliders")

    slider = await page.query_selector('input[value="15"]')

    await slider.drag_to(95)

    range_value = await page.inner_text('text=Range Value:')
    assert range_value == "95"

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())