from playwright.sync_api import sync_playwright


# def getProxy():
#     return None
#
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, proxy={getProxy()})
#     page = browser.new_page()
#     page.goto("https://kamerjam.blogspot.com/")
#     print(page.title())
#     browser.close()

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False, proxy={
        "server": 'server-address:port',
        'username': 'My_user',
        "password": 'My_password',
    })
    context = browser.newContext()
    page = context.newPage()
    page.goto('https://whoer.net')
    page.screenshot(path='whoer.png')
    browser.close()