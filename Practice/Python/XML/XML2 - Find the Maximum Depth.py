import xml.etree.ElementTree as etree

maxdepth = 0
def depth(element, level):
    global maxdepth
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in element:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
