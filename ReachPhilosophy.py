import requests
import sys
import time
import re
from bs4 import BeautifulSoup


def reachPhilosophy(url, visited):
    """
    It opens the given URL ans enters the first link to another wiki page -if exists- and continues doing so
    till it reaches Philosophy page or it will enter an infinite loop.
    also Prints the pages traveled.

    :param url: The URL to start looking for Philosophy from it.
    :param visited: the visited links.
    :return: None
    """
    r = requests.get(url)
    parser = "html.parser"
    bs = BeautifulSoup(r.text, parser)
    headIndex = r.url.find("/wiki/")
    head = r.url[headIndex+6:]
    print(head + " : " + r.url)
    if head == "Philosophy":
        print("Philosophy Page reached after passing " + str(len(visited)) + " pages.")
        return
    # Saves the visited links.
    visited.append(r.url)

    # print(bs.prettify())  Used to see the HTML file in a well intended tree.
    # time.sleep(0.5)
    data = bs.find('div', class_="mw-parser-output")
    # This Removes boxes, italic, footnotes.
    for itr in data.findAll(['table', 'i', 'ol']):
        itr.replace_with('')

    # This Removes Table of Contents.
    for itr in data.findAll(id='toc'):
        itr.replace_with('')

    for itr in data.findAll(class_="thumbinner"):
        itr.replace_with('')

    data = bs.findAll(['p', 'ul'])
    # Making a String having the content of the Wiki page & Remove text within Parenthesis.

    text = str(data)
    cleanText = re.sub(r" ?\([^)]+\)", "", text)

    # getting the link.
    searchIndex = cleanText.find('href="/wiki/')

    if searchIndex == -1:
        print("There is no Wiki page links in the current page.")
        return
    else:
        # This bunch of code to make sure that the link is completely taken from the text.
        # To avoid deleting of Parenthesis of the link in code line (48)
        endLinkIndex = cleanText[searchIndex + 6:].find('"')
        page = cleanText[searchIndex+6:searchIndex + endLinkIndex + 6]
        startlinkIdx = text.find(page)
        endLinkIdx = text[startlinkIdx+6:].find('"')
        link = "https://en.wikipedia.org" + text[startlinkIdx:startlinkIdx+endLinkIdx+6]

        link = requests.get(link).url
        if link in visited:
            print("Entered an infinite Loop.")
            return
        else:
            reachPhilosophy(link, visited)
    return


if __name__ == '__main__':
    # In case no input URL is given, we use Random URL from Wikipedia.
    if len(sys.argv) == 1:
        firstUrl = "http://en.wikipedia.org/wiki/Special:Random"
        print("\nRandom URL used.\n")
    else:
        # it the URL and passes it to reachPhilosophy Function.
        firstUrl = sys.argv[1]
    visit = list()
    reachPhilosophy(firstUrl, visit)
