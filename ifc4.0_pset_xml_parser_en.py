from lxml import etree
import csv
from glob import glob
import codecs

for f in glob("pset_xml/psd/*.xml"):

    tree = etree.parse("pset_xml/qto/Qto_DoorBaseQuantities.xml")
    root = tree.getroot()

    mynsmap = {}
    mynsmap = root.nsmap

    name_pset = tree.xpath('/QtoSetDef/Name')

    names_prop = tree.xpath('/QtoDef/Name')

    names_en = tree.xpath(
        '/QtoSetDef/QtoDefs/QtoDef/NameAliases/NameAlias[@lang="en"]')
    note_en = tree.xpath(
        '/QtoSetDef/QtoDefs/QtoDef/Definition')

    list_names_prop = []

    pset_list = []

    for i in range(len(names_en)):
        row = []
        row.append(name_pset[0].text)
        row.append(names_en[i].text)
        row.append(note_en[i].text)
        pset_list.append(row)

    print(pset_list)

    with codecs.open('pset_list_EN.csv', 'a', 'cp932', 'ignore') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(pset_list)
