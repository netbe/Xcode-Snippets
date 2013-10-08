from xml.dom import minidom
import os
import glob

print ">> Updating README.md based on .codesnippet files"

file = open('README.md', 'w')
file.write('# CodeSnippets\n\n')
file.write('**Inspired by [jaydee3](https://github.com/jaydee3/CodeSnippets)**\n\n')
file.write('These are my Xcode 4+ CodeSnippets.  \n')
file.write('To use them, clone this repository, and execute the command:\n\n')
file.write('    ./setup.sh\n')
file.write('And you\'re ready to go.\n\n')
file.write('This README is generated automatically using `.generateDescription.py`.  \n')
file.write('This script executes automatically before each commit (pre-commit hook). You can remove the hook like this:\n\n')
file.write('    rm .git/hooks/pre-commit\n\n')
file.write('## Snippet Descriptions\n\n')

listing = os.listdir(".")
for fileName in listing:

    if not fileName.endswith(".codesnippet"):
    	continue

    xmldoc = minidom.parse(fileName)
    keyslist = xmldoc.getElementsByTagName('key')
    allChilds = xmldoc.getElementsByTagName('dict')[0].childNodes

    for x in allChilds:
    	if not x.firstChild:
    		allChilds.remove(x)

    title=""
    summary=""
    shortcut=""
    contents=""

    for key in keyslist:
    	value = key.firstChild.nodeValue
    	if (value == "IDECodeSnippetCompletionPrefix"):
    		shortcut = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetContents":
    		contents = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetSummary":
    		summary  = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetTitle":
    		title    = allChilds[allChilds.index(key)+1].firstChild.nodeValue

    file.write('**' + fileName + '**  (' + title + ')  \n')
    file.write('Shortcut: `' + shortcut + '`  \n')
    file.write(summary + '\n\n')
    file.write('    ' + contents.replace('\n', '\n    ') + '\n\n')

file.close()

