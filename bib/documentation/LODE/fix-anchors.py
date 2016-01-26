#!/usr/bin/env python
"""Fix up anchors in the LD4L ontology document so that terms resolve.

The output of LODE is an HTML document with meanlingless anchors which
means that we can't readily make the ontology URIs nicely resolve the
the appropriate definitions. This script goes through the HTML looking
for terms in the ontology and rewriting anchors to be the local part of
the URI.

Note that there are cases where the one ontology term (e.g. 
http://bib.ld4l.org/ontology/note ) is described in multiple places
within the ontology (in this case as a Data Property and an
Annotation Property). The rewrite of anchors takes the first occurrance
in the HTML as the anchor to change (i.e. the Data Property in this
case).

Simeon Warner - 2016-01-22
"""

import re

html = open('ld4l-bib.html','r').read()
prefix = 'http://bib.ld4l.org/ontology/'

## Pass 1 - find anchors to change
terms = {}
seen_anchors = set()
for m in re.findall(r'''<a href="#([0-9a-f]+)" title="([^"]+)"''',html):
    anchor = m[0]
    uri = m[1]
    # Only want URIs in this ontology
    lmatch = re.match(prefix+r'''(\w+)$''', uri)
    if (lmatch):
        term = lmatch.group(1)
        if (term in terms):
            if (terms[term] != anchor and anchor not in seen_anchors):
                print "Ignoring additional anchor %s, already have %s for %s%s" % (anchor, terms[term], prefix, term)
                seen_anchors.add(anchor)
        else:
            terms[term] = anchor

## Pass 2 - implement changes
for term, anchor in terms.items():
    print "Replacing anchor %s with %s" % (anchor, term)
    html = re.sub(' id="'+anchor+'"',' id="'+term+'"',html)
    html = re.sub(' href="#'+anchor+'"',' href="#'+term+'"',html)

open('ld4l-bib-anchors.html','w').write(html)
