from lxml import etree
import re

class teiParse:
    def __init__(self):
        self.foreignlist = []

    def parseDel(self, elem):
        # If the arg isn't a <del> element, do nothing
        if elem.tag is not "del":
            return ""

        # If the deletion is legitimate, return an empty string
        if elem.get("status") == "unremarkable":
            return ""


    def parseAdd(self, elem):
        # If the arg isn't a <add> element, do nothing
        if elem.tag != "add":
            return elem

        return "[" + elem.text + "]"


    # Postpend [sic] to element text
    def parseSic(self, elem):
        # If the arg isn't a <sic> element, do nothing
        if elem.tag != "sic":
            return ""

        return elem.text + " [sic]"


    # Mark omission with ellipses
    def parseGap(self, elem):
        # If the arg isn't a <gap> element, do nothing
        if elem.tag is not "gap":
            return elem

        return "..."


    def parseForeign(self, elem):
        # If the arg isn't a <foreign> element, do nothing
        if elem.tag != "foreign":
            return elem

        # Normalize the input for saner uniqueness of stored entries
        flang = elem.get("lang")
        ftext = elem.text.lower()
        ftext = ftext.strip()
        ftext = re.sub(r'[.,-]+$', '', ftext)

        fentry = (ftext, flang)

        # Brain-dead heuristic: if the string has 3+ spaces, it's probably a phrase. Don't italicize
        if re.search(r'[^ ]+ [^ ]+ [^ ]+ ', ftext):
            return elem.text

        # If we've seen an entry before, return the element as-is. Otherwise, add to list and italicize this instance
        if fentry in self.foreignlist:
            return elem.text
        else:
            self.foreignlist.append(fentry)
            return "<i>" + elem.text + "</i>"

