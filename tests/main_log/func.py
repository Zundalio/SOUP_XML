from lxml import etree
import requests
import allure


@allure.step("Загрузка файла")
def download_file(url, local_path):
    """Функция для скачивания XML документа и XSD схемы"""
    response = requests.get(url)
    response.raise_for_status()
    with open(local_path, 'wb') as f:
        f.write(response.content)


@allure.step("Валидация файла")
def validate_xml(xml_path, xsd_path):
    """Функция для валидации"""
    with open(xsd_path, 'rb') as f:
        schema_root = etree.XML(f.read())
    schema = etree.XMLSchema(schema_root)

    with open(xml_path, 'rb') as f:
        xml_doc = etree.parse(f)

    schema.assertValid(xml_doc)
