import pytest

xml_url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002'
xsd_url = 'https://www.cbr.ru/StaticHtml/File/92172/ValCurs.xsd'
xml_path = 'temp_xml.xml'
xsd_path = 'temp_xsd.xsd'


@pytest.fixture(scope='session')
def xml_url_fixture():
    return xml_url


@pytest.fixture(scope='session')
def xsd_url_fixture():
    return xsd_url


@pytest.fixture(scope='session')
def xml_path_fixture():
    return xml_path


@pytest.fixture(scope='session')
def xsd_path_fixture():
    return xsd_path
