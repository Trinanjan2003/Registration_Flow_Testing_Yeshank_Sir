from selenium.webdriver.common.by import By


class RegistrationPageLocators:

    first_name_locator = (By.ID, 'first_name')
    last_name_locator = (By.ID, 'last_name')
    dob_locator = (By.ID, 'dob')
    street_locator = (By.ID, 'street')
    postal_code_locator = (By.ID, 'postal_code')
    city_locator = (By.ID, 'city')
    state_locator = (By.ID, 'state')
    phone_locator = (By.ID, 'phone')
    email_locator = (By.ID, 'email')
    password_locator = (By.ID, 'password')
    register_button_locator = (By.XPATH, "//button[@data-test='register-submit']")
    country_locator = (By.XPATH, "//select[@id='country']")

    # test 02
    already_registered_locator = (By.XPATH,"//div[@class='help-block']")

    #test 03
    weak_password_alert_message_locator = (By.XPATH,"//div[@class='alert alert-danger mt-3']/div")

    #test 04
    no_email_given_locator = (By.XPATH, "(//div[@class='form-group mb-3']/div)[1]/div")

    #test 05
    invalid_email_locator = (By.XPATH, "//div[@class='alert alert-danger mt-3']")
