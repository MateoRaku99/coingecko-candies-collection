import pytest
import undetected_chromedriver as uc
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from myConfig import email, password, to_email


@pytest.fixture(scope="function")
def driver():
    chrome_options = uc.ChromeOptions()
    chrome_options.headless = False
    chrome_options.add_argument("--no-sandbox")

    driver = uc.Chrome(options=chrome_options, use_subprocess=True)
    driver.get("https://www.coingecko.com/")
    yield driver

    # Teardown - Close the WebDriver session after tests
    driver.quit()


failed = False
error_messages = []


def send_email():
    subject: str = "Test failure"
    fromaddr: str = email
    toaddrs: str = [to_email]
    passe: str = password
    msg = MIMEMultipart()
    # msg.attach(MIMEText(payload,"Test Failures:"))
    msg["Subject"] = subject
    msg["From"] = fromaddr
    msg["To"] = ",".join(toaddrs)

    # Add attachment to message and convert message to string
    for error in error_messages:
        msg.attach(MIMEText(error))
    text = msg.as_string()

    # Log in to server using secure context and send email
    # context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(fromaddr, passe)
        server.sendmail(fromaddr, toaddrs, text)
        print("email sent")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global failed
    report = yield
    result = report.get_result()

    if result.when == "call" and result.outcome == "failed":
        error_message = call.excinfo.getrepr(funcargs=False, showlocals=False)
        failed = True
        error_messages.append(f"Test {item.name} failed \n {error_message}")


def pytest_sessionfinish(session, exitstatus):
    if failed is True:
        send_email()
