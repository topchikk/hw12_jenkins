from resource.users import new_user
from pages.registration_page import RegistrationPage
import allure


@allure.title("Заполнение тренировочной формы DemoQA")
def test_registration_form():
    with allure.step("Открытие формы регистрации"):
        registration_page = RegistrationPage()
        registration_page.open()
        registration_page.remove_banner()

    # WHEN
    with allure.step("Заполнение поля имя"):
        registration_page.fill_first_name(new_user.first_name)
        registration_page.fill_last_name(new_user.last_name)

    with allure.step("Заполнение поля email"):
        registration_page.fill_email(new_user.user_email)

    with allure.step("Выбор пола"):
        registration_page.select_gender(new_user.gender)

    with allure.step("Заполнение поля телефонный номер"):
        registration_page.fill_phone(new_user.user_number)

    with allure.step("Выбор даты рождения"):
        registration_page.fill_date_of_birth(new_user.month, new_user.year, new_user.day)

    with allure.step("Выбор предметов"):
        registration_page.fill_subject(new_user.subjects)

    with allure.step("Выбор хобби"):
        registration_page.select_hobbie(new_user.hobbies)

    with allure.step("Загрузка изображения"):
        registration_page.upload_picture(new_user.images)

    with allure.step("Заполнение полного адреса"):
        registration_page.fill_address(new_user.current_address)
        registration_page.fill_state(new_user.state)
        registration_page.fill_city(new_user.city)

    with allure.step("Отправка формы регистрации"):
        registration_page.click_submit()

    # THEN
    with allure.step("Сравнение отправленных и переданных значений"):
        registration_page.should_registered_user_info_with(new_user.first_name, new_user.last_name, new_user.user_email,
                                                       new_user.gender, new_user.user_number, new_user.day,
                                                       new_user.month, new_user.year, new_user.subjects,
                                                       new_user.hobbies, new_user.images, new_user.current_address,
                                                       new_user.state,
                                                       new_user.city)
