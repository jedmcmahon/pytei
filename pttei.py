from lxml import etree
import re


class TeiParse:
    MS_SECMARK = "ms_secmark"
    MS_SECBREAK = "ms_secbreak"
    MS_CHAPTER = "ms_chapter"

    def __init__(self):
        self.foreignlist = []

    # Evaluate/remove deleted text
    def parsedel(self, elem):
        # If the arg isn't a <del> element, do nothing
        if elem.tag is not "del":
            return ""

        # If the deletion is legitimate, return an empty string. Otherwise, pass it through
        if elem.get("status") == "unremarkable":
            return ""
        else:
            return elem.text

    # Add standard [ ] punctuation for editorial additions
    def parseadd(self, elem):
        # If the arg isn't a <add> element, do nothing
        if elem.tag != "add":
            return elem

        return "[" + elem.text + "]"

    # Postpend [sic] to element text
    def parsesic(self, elem):
        # If the arg isn't a <sic> element, do nothing
        if elem.tag != "sic":
            return ""

        return elem.text + " [sic]"

    # Mark omission with ellipses
    def parsegap(self, elem):
        # If the arg isn't a <gap> element, do nothing
        if elem.tag is not "gap":
            return elem

        return "..."

    # Italicize the first instance of a foreign word, pass subsequent ones through
    # TODO: Best location for BetaCode conversion?
    def parseforeign(self, elem):
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

    def parsemilestone(self, elem, mstype):
        # If the arg isn't a <milestone> element, do nothing
        if elem.tag != "milestone":
            return elem

    def parsenote(self, elem):
        # If the arg isn't a <note> element, do nothing
        if elem.tag != "note":
            return elem

