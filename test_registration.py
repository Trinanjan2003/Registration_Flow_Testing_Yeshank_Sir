import time
import pytest
from conftest import skip_registration_details
from data.configuration import Configuration
from pageobjects.registration_actions import RegistrationPageActions

import logging

logging.basicConfig(level=logging.INFO)



class TestFile:

    @pytest.mark.run(order=1)
    @pytest.mark.registration
    def test_01_registration(self,fill_registration_details):
        try:

            self.driver = fill_registration_details
            logging.info("Registraion Successful ! ! !")
            time.sleep(5)
        except Exception as e:
            raise AssertionError(f"Something went wrong : {e}")
        finally:
            self.driver.quit()


    @pytest.mark.run(order=2)
    @pytest.mark.registration
    def test_02_already_registered(self,fill_registration_details):
        self.driver = fill_registration_details
        reg = RegistrationPageActions(driver=self.driver)

        try:
            reg.email_already_exist_msg()
            time.sleep(5)
        except Exception as e:
            raise AssertionError(f"Something went Wrong !! : {e}")
        finally:
            self.driver.quit()


    @pytest.mark.run(order=3)
    @pytest.mark.registration
    def test_03_weak_password(self,fill_registration_details):

        self.driver = fill_registration_details
        reg = RegistrationPageActions(driver=self.driver)
        try:

            reg.fill_password(Configuration.weak_password)

            reg.submit()
            time.sleep(5)
            reg.weak_password_msg()

        except Exception as e:
            raise AssertionError(f"Something went wrong : {e}")
        finally:
            self.driver.quit()


    @pytest.mark.run(order=4)
    @pytest.mark.registration
    def test_04_skip_email(self,skip_registration_details):

        self.driver = skip_registration_details
        reg = RegistrationPageActions(driver=self.driver)
        try:

            time.sleep(5)
            reg.no_email_msg()
        except Exception as e:
            raise AssertionError(f"Something went wrong : {e}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=5)
    @pytest.mark.registration
    def test_05_invalid_mail(self,invalid_registration_details):

        self.driver = invalid_registration_details
        reg = RegistrationPageActions(driver=self.driver)
        check = reg.invalid_mail_msg(Configuration.invalid_email)
        try:
            if not check:
                self.driver.quit()
            else:
                time.sleep(5)
                self.driver.quit()
        except Exception as e :
            raise AssertionError(f"Something went wrong : {e}")


