import requests
r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
from xml.etree import ElementTree as ET
tree = ET.parse(r.raw)
root = tree.getroot()
namespaces = {'ex': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}
for cube in root.findall('.//ex:Cube[@currency]', namespaces=namespaces):
    print(cube.attrib['currency'], cube.attrib['rate'])
