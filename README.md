# Reach-Philosophy
A Python webscraping mini-project.

Extracting the 1st non-parenthesized, non-italicized link, in the main text of any Wikipedia article, and then repeating the process for subsequent articles, usually eventually get us to the Philosophy main article in Wikipedia.

## Write the script as follows:
python ReachPhilosophy.py

-this will make it use a random Wiki page.

python ReachPhilosophy.py (Wikipage's link without parenthesis)

-this will try to reach "Philosophy" page strarting from that link, printing every visited wiki page.

## There are only 3 possible outcomes:
1- It reached "Philosophy" page. [this is the normal outcome]

2- It entered an infinite loop.

3- It reached a wiki page that doesn't have any normal hyperlinks to another wiki page.
