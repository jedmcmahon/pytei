from lxml import etree

class teiParse:
    def __init__(self, name):
        self.name = name
        self.foreignlist = []

    def parseDel(elem):
        # If the arg isn't a <del> element, do nothing
        if not isinstance(elem, etree.Element):
            return elem
        if elem.tag is not "del":
            return elem

        # If the deletion is legitimate, return an empty string
        if elem.get("status") == "unremarkable":
            return ""


    def parseAdd(elem):
        # If the arg isn't a <del> element, do nothing
        if not isinstance(elem, etree.Element):
            return elem
        if elem.tag is not "add":
            return elem

        return "[" + elem.text + "]"


    def parseGap(elem):
        # If the arg isn't a <del> element, do nothing
        if not isinstance(elem, etree.Element):
            return elem
        if elem.tag is not "gap":
            return elem

        return "..."


    def parseForeign(self, elem):
        # If the arg isn't a <del> element, do nothing
        if not isinstance(elem, etree.Element):
            return elem
        if elem.tag is not "foreign":
            return elem

        flang = elem.get("lang")
        ftext = elem.text.lower()
        ftext = ftext.strip()

        fentry = (ftext, flang)

        if fentry in self.foreignlist:
            return elem.text
        else:
            self.foreignlist.append(fentry)
            return "<i>" + elem.text + "</i>"

