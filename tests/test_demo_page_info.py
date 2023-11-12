import pytest
from lib.Demo_page import DemoPage, LoggedInSuccessfullyOnDemoPage
from conftest import driver


test_data = [
    ('Piotr', 'Rokita', 'Globallogic', 'rokita1337@gmail.com')
]


class TestPositiveScenarios:

    @pytest.mark.download_demo
    @pytest.mark.positive
    @pytest.mark.parametrize("first_name, last_name, company, email", test_data)
    def test_demo_download_positive(self, driver, first_name, last_name, company, email):
        demo_page = DemoPage(driver)
        demo_page.open()
        demo_page.execute_demonstration_version(first_name, last_name, company, email)
        demo_page_download = LoggedInSuccessfullyOnDemoPage(driver)
        assert demo_page_download.header == 'Instant demo request form', 'Instant demo request form should be displayed'
        assert demo_page_download.feedback == (
            'We have sent your demo credentials to your email please check your email to test demo website. '
            'if message not found inbox please check spam folder'), \
            'Feedback message should be displayed'
        assert demo_page_download.is_picture_displayed(), "Picture should be displayed"


