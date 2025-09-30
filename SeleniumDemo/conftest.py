import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # options = webdriver.ChromeOptions()
    # prefs = {
    #     "credentials_enable_service": False,
    #     "profile.password_manager_enabled": False
    # }
    # options.add_experimental_option("prefs", prefs)

    browser_name = request.config.getoption("browser_name")
    service_obj = Service(
        "C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe"
    )  # C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj, options=options)

    elif browser_name == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    yield driver  # Before test function execution

    driver.quit()  # Post your test function execution


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Extends the pytest plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(
                reports_dir, 'screenshots', report.nodeid.replace("::", "_") + ".png"
            )
            print("File name is : ", file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = ('<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
