Process for creating and deploying a new version of the LODE documentation:

1. Generate documentation from local rdf file: http://www.essepuntato.it/lode

2. Save page as ld4l-bib.html. Save as "Web Page, HTML only", to save everything
in a single file (otherwise stylesheets and images are saved to a subdirectory). 

3. Fix anchors by running fix-anchors.py. This results in a new file 
ontology.html.

4. Modify ontology.html file as follows: 
- Change href of link on "Ontology source" from the essepuntato site to 
http://bib.ld4l.org/ontology.rdf
- Add link to ld4l.org site in first line of abstract:
This bibliographic ontology is based on Rob Sanderson's and 
<a href="http://ld4l.org/>LD4L</a>'s recommended changes...

5. Commit both files to git (though actually only ontology.html is needed).
ld4l-bib.html
ontology.html

6. scp ontology.html to the bib.ld4l.org server into the directory
/libweb/sites/bib.ld4l.org/htdocs. Presumably you will also be copying the 
ontology source to /libweb/sites/bib.ld4l.org/htdocs/ontology.rdf.