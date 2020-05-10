import lxml.html.diff
import lxml.html

html1 = open('archive.html').read()
html2 = open('index.html').read()

result = lxml.html.diff.htmldiff(html1, html2)

root = lxml.html.fromstring(result)

for node in root.xpath('//*[self::ins or self::del]'):
    text = node.text
    if not text:
        continue
    if '#' in text or 'http' in text:
        node.getparent().remove(node)


styles = """
<style>
ins {
color: green;
}

ins a {
    color: green;
}

del {
text-decoration: line-through;
color: red;
}
</style>
"""

with open('diff.html', 'w') as fp:
    fp.write(lxml.html.tostring(root, encoding=str))
    fp.write(styles)
