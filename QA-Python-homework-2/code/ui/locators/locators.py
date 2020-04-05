from selenium.webdriver.common.by import By


class BaseLocators:
    CAMPAIGNS = (By.XPATH, '//a[@href="/campaigns/list"]')
    SEGMENTS = (By.XPATH, '//a[@href="/segments"]')


class MainPageLocators(BaseLocators):
    LOGIN_BUTTON = (By.XPATH, '//div[contains(text(), "Войти")]')
    AUTH_FORM = (By.XPATH, '//h3[contains(text(), "Вход в рекламный кабинет")]')
    LOGIN_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    CONFIRM_LOGIN = (By.XPATH, '//div[contains(@class,"authForm-module-button")] ')


class CampaignsLocators(BaseLocators):

    @staticmethod
    def USER_TITLE(username):
        return By.XPATH, '//div[contains(@title,"{}")]'.format(username)

    @staticmethod
    def CAMPAIGN_NAME(name):
        return By.XPATH, '//a[@title="{}"]'.format(name)

    CREATE_CAMPAIGN_EMPTY = (By.XPATH, '//span[@class="empty-table-data-message__text"]//a[@href="/campaign/new"]')
    CREATE_CAMPAIGN_NOT_EMPTY = (By.XPATH,
                                 '//a[@class="campaigns-tbl-settings__button campaigns-tbl-settings__button_new" and'
                                 ' @href="/campaign/new"]')


class NewCampaignsLocators(BaseLocators):
    TRAFFIC = (By.XPATH, '//div[contains(text(), "Трафик")]')
    LINK_FIELD = (By.XPATH, '//input[contains(@data-translated-lit,"Enter the link")]')
    CLEAR_NAME_BUTTON = (By.XPATH,
                         '//div[contains(@class,"campaign-name")]//div[contains(@class,"input__clear js-input-clear")]')
    NAME_FIELD = (By.XPATH, '//div[contains(@class,"campaign-name")]//input')

    SEX_FIELD = (By.XPATH, '//span[contains(text(), "Мужчины, Женщины")]')
    MALE_CHECKBOX = (By.XPATH, '//input[@targeting="sex-male"]')
    FEMALE_CHECKBOX = (By.XPATH, '//input[@targeting="sex-female"]')

    AGE_FIELD = (By.XPATH, '//div[@data-scroll-name="setting-age"]')
    AGE_CHOICE = (By.XPATH,
                  '//div[@class="age-setting"]//div[@class="select__item select__item_value js-select-button"]')
    RANDOM_AGE = (By.XPATH,
                  '//span[@class="select-item__text js-list-item-text"  and contains(text(), "Произвольный набор")]')
    AGE_INPUT = (By.XPATH, '//div[@class="age-setting__text js-age-setting-text"]//textarea')

    FORMAT_TEASER = (By.XPATH, '//div[@id="149"]')

    BANNER_TITLE = (By.XPATH, '//input[@data-gtm-id="banner_form_title"]')
    BANNER_TEXT = (By.XPATH, '//textarea[@data-gtm-id="banner_form_text"]')
    UPLOAD_FILE = (By.XPATH, '//div[contains(@class,"banner-form")]//input[@type="file"]')
    ADD_ADVERT = (By.XPATH, '//div[contains(text(), "Добавить объявление")]')

    CONFIRM_CREATING = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')


class InvalidAuthLocators:
    INVALID_LOGIN = (By.XPATH, '//div[contains(text(), "Invalid login or password")]')


class SegmentsLocators(BaseLocators):
    VK_GROUPS = (By.XPATH, '//a[@href="/segments/groups_vk_list"]')

    CREATE_SEGMENT_EMPTY = (By.XPATH, '//a[@href="/segments/segments_list/new"]')
    CREATE_SEGMENT_NOT_EMPTY = (By.XPATH, '//div[contains(text(),"Создать сегмент")]')

    @staticmethod
    def SEGMENT_NAME(name):
        return By.XPATH, '//a[@title="{}"]'.format(name)

    SORT_BY_ID = (By.XPATH, '//th[@data-group-id="id" and @class="flexi-table__header-th"]')

    @staticmethod
    def DELETE(name):
        return (
            By.XPATH, '//tr[@class="flexi-table__row" and .//a[@title="{}"]]//span[@class="icon-cross"]'.format(name))

    CONFIRM_DELETE = (By.XPATH, '//div[contains(text(),"Удалить")]')


class NewSegmentsLocators(BaseLocators):
    ADD_DATA_SEGMENT = (By.XPATH, '//span[@data-loc-en="Add audience segments..."]')

    VK_DATA = (By.XPATH, '//div[@class="adding-segments-item" and contains(text(),"Группы (VK)")]')

    @staticmethod
    def CHOICE_GROUP(name):
        return (By.XPATH,
                './/span[@class="js-source-name" and text()="{}"]'
                '//ancestor::*/div[@class="adding-segments-source"]//input'.format(name))

    ADD_SEGMENT = (By.XPATH, '//div[contains(text(),"Добавить сегмент")]')
    NAME_FIELD = (By.XPATH, '//div[@class="js-segment-name"]//input')
    CONFIRM_CREATING = (By.XPATH, '//div[contains(text(),"Создать сегмент")]')


class VkGroupsLocators(BaseLocators):
    LINK_FIELD = (By.XPATH, '//div[@class="suggester-ts suggester-ts_with-loader"]//input')
    FIRST_SUGGEST = (By.XPATH, '//ul[@class="suggester-ts__items js-item-list "]/li[1 and @data-id!="_emptyItem"]')

    @staticmethod
    def GROUP_NAME_IN_TABLE(name):
        return By.XPATH, '//tr[@class="flexi-table__row"]/td[@data-id="name" and contains(text(), "{}")]'.format(name)
