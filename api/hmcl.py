import xml.etree.ElementTree as ET
import requests

def get_Latest_Version(channel):
    ExistingVersionXML = requests.get(
        f'https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/maven-metadata.xml').text
    ExistingVersion = ET.fromstring(ExistingVersionXML)
    element = ExistingVersion.find('versioning/latest')
    if element is not None:
        return element.text
    else:
        return None

def version_verify(channel, version):
    if requests.get(f'https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/{version}/').status_code == 404:
        return False
    else:
        return True

def version_sha1(channel, version):
    exesha1 = requests.get(f'https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/{version}/hmcl-{channel}-{version}.exe.sha1').text
    jarsha1 = requests.get(f'https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/{version}/hmcl-{channel}-{version}.jar.sha1').text
    return exesha1,jarsha1