from lxml import etree
import beta2unicode

doc = etree.parse("sample/vitlat.xml")

root = doc.getroot()

txt = root.find("text")

tIter = txt.iter()

fwords = []

for elem in tIter:
    eTag = elem.tag

    if eTag not in fwords:
        fwords.append(eTag)

fwords.sort()

for f in fwords:
    print(f)
