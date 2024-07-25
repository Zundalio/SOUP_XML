from lxml import etree
from tests.main_log.check import check_numeric_values, check_currency_codes, check_required_fields, \
    check_unique_currency_codes
from tests.main_log.func import download_file, validate_xml
import allure


@allure.feature("Test")
@allure.story("API")
@allure.title("Валидация XML док ЦБ")
def test_valid_xml(xml_path_fixture, xsd_path_fixture, xml_url_fixture, xsd_url_fixture):
    download_file(xml_url_fixture, xml_path_fixture)
    download_file(xsd_url_fixture, xsd_path_fixture)
    validate_xml(xml_path_fixture, xsd_path_fixture)
    xml_doc = etree.parse(xml_path_fixture)
    check_numeric_values(xml_doc)
    check_currency_codes(xml_doc)
    check_required_fields(xml_doc)
    check_unique_currency_codes(xml_doc)

