import pytest
import allure


@allure.step("Проверка на число")
def check_numeric_values(xml_doc):
    """Проверка значения на число """
    for element in xml_doc.xpath("//Value"):
        if element.text:
            value = element.text.replace(',', '.')
            if value.replace('.', '', 1).isdigit():
                float(value)
            else:
                pytest.fail(f"Значение {element.text} не является числом.")


@allure.step("Проверка кодов валют")
def check_currency_codes(xml_doc):
    """Проверка кодов валют"""
    valid_currency_codes = []
    for s in xml_doc.xpath("//CharCode"):
        valid_currency_codes.append(s.text)

    for code in xml_doc.xpath("//CharCode"):
        if code.text not in valid_currency_codes:
            pytest.fail(f"Недействительный код валюты: {code.text}")


@allure.step("Проверка на соответствие XML документа")
def check_required_fields(xml_doc):
    """Проверка на соответствие"""
    required_fields = ['NumCode', 'CharCode', 'Nominal', 'Name', 'Value', 'VunitRate']

    for valute in xml_doc.xpath("//Valute"):
        for field in required_fields:
            if valute.find(field) is None:
                pytest.fail(f"Отсутствует обязательное поле <{field}> в элементе <Valute>")


@allure.step("Проверка на дублирующие коды")
def check_unique_currency_codes(xml_doc):
    """Проверка на уникальность валют"""
    codes = [code.text for code in xml_doc.xpath("//CharCode")]
    if len(codes) != len(set(codes)):
        pytest.fail("Обнаружены дублирующиеся коды валют.")
