import pytinyxml2
doc = pytinyxml2.XMLDocument()
doc.Parse("<?xml version=\"1.0\"?><element>Text</element>")
print(doc.FirstChildElement().GetText())
