import logging
import re

from locators.registration_locators import RegistrationPageLocators
from pageobjects.base_page import BasePage
from utilities.wait_utils import WaitUtils

logging.basicConfig(
    filename="report.html",  # Output file
    filemode="w",            # Overwrites file on each run (use "a" to append)
    format="%(asctime)s - %(levelname)s - %(message)s <br>",  # Add <br> for HTML line breaks
    level=logging.INFO       # Ensure INFO logs are captured
)

class RegistrationPageActions(BasePage):

    def fill_firstname(self,firstname):
        first_name = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.first_name_locator)
        first_name.clear()
        first_name.send_keys(firstname)

    def fill_lastname(self,lastname):
        last_name = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.last_name_locator)
        last_name.clear()
        last_name.send_keys(lastname)

    def fill_dob(self,dob):
        d_o_b = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.dob_locator)
        d_o_b.clear()
        d_o_b.send_keys(dob)

    def fill_street(self,street):
        strt = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.street_locator)
        strt.clear()
        strt.send_keys(street)

    def fill_postal_code(self,postal_code):
        pc = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.postal_code_locator)
        pc.clear()
        pc.send_keys(postal_code)

    def fill_city(self,city):
        cty = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.city_locator)
        cty.clear()
        cty.send_keys(city)

    def fill_state(self,state):
        stt = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.state_locator)
        stt.clear()
        stt.send_keys(state)

    def fill_country(self,country):
        ctry = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.country_locator)
        ctry.send_keys(country)

    def fill_phone(self,phone):
        ph = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.phone_locator)
        ph.clear()
        ph.send_keys(phone)

    def fill_email(self,email):
        em = WaitUtils.wait_for_element(self.driver, RegistrationPageLocators.email_locator)
        em.clear()
        em.send_keys(email)

    def fill_password(self, password):
        pswd = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.password_locator)
        pswd.clear()
        pswd.send_keys(password)

    def submit(self):
        WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.register_button_locator).click()

    def email_already_exist_msg(self):
        txt = WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.already_registered_locator).text

        assert "A customer with this email address already exists." in txt
        logging.info(f"{txt}")


    def weak_password_msg(self):

        WaitUtils.wait_for_element(self.driver,RegistrationPageLocators.weak_password_alert_message_locator)
        lst = self.driver.find_elements(*RegistrationPageLocators.weak_password_alert_message_locator)

        for txt in lst:
            final_txt = txt.text
            logging.info(final_txt)


    def no_email_msg(self):
        txt = WaitUtils.wait_for_element(self.driver,
            RegistrationPageLocators.no_email_given_locator).text
        logging.info(txt)

    def invalid_mail_msg(self,email):
        try:
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            if re.fullmatch(email_regex, email):
                return True
            else:
                logging.info("The email entered is Invalid !")
                return False
        except Exception as e:
            return False

    def skip_email(self,email):
        em = WaitUtils.wait_for_element(self.driver, RegistrationPageLocators.email_locator)
        em.clear()

