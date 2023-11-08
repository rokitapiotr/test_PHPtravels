import pytest
from test_PHPtravels.Pages.Demo_page import DemoPage
from test_PHPtravels.Pages.Demo_page_logged_succesfully import LoggedInSuccessfullyOnDemoPage


class TestPositiveScenarios:

    @pytest.mark.download_demo
    @pytest.mark.positive
    def test_demo_download_positive(self, driver):
        demo_page = DemoPage(driver)
        demo_page.open()
        demo_page.execute_demonstration_version('Piotr', 'Rokita', 'Tesla', 'piotrrokita@gmail.com')
        demo_page_download = LoggedInSuccessfullyOnDemoPage(driver)
        assert demo_page_download.feedback == ('We have sent your demo credentials to your email please check your email to test demo website. if message not found inbox please check spam folderr'), \
                                               'Feedback message should be displayed'
        assert demo_page_download.is_picture_displayed(), "Picture should be displayed"
        assert demo_page_download.header == 'Instant demo request form', 'Instant demo request form should be displayed'

