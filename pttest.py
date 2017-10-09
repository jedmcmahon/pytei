from lxml import etree
import beta2unicode

import pttei

tp = pttei.teiParse()



doc = etree.parse("sample/jugeng.xml")

root = doc.getroot()

txt = root.find("text")

tIter = txt.iter()

fwords = []

for elem in tIter:
    eTag = elem.tag

    if eTag == "foreign":
        print(tp.parseForeign(elem))

