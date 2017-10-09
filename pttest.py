from lxml import etree
import beta2unicode
import re

import pttei

tp = pttei.TeiParse()



doc = etree.parse("sample/jureng.xml")

root = doc.getroot()

txt = root.find("text")

tIter = txt.iter()

for elem in tIter:
    eTag = elem.tag

    if re.match(r'^div', eTag):
        if elem.get("type") == "chapter":
            print(elem.tag + " chapter within " + elem.getparent().tag + " " + elem.getparent().get("type"))

