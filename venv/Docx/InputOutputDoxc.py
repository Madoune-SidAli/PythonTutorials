#install pydocx package

import docx

doc = docx.Document('python.docx')
#Reading
print(doc.paragraphs[0].text)        #return the First line
print(doc.paragraphs[1].text)        #return the First line

#to detect the different type of writings for exemple bold, italic or underline one we use runs functions
print(doc.paragraphs[0].runs[0].text)        #return My name            => simple
print(doc.paragraphs[0].runs[1].text)        #return Madoune            =>  bold
print(doc.paragraphs[1].runs[0].text)        #return I am               => simple again
print(doc.paragraphs[1].runs[1].text)        #return Software Engineer  => italic
print(doc.paragraphs[1].runs[2].text)        #return the first run      => simple again
print(doc.paragraphs[1].runs[3].text)        #return Python             => underlined


#Writing ,Creating a new docx
doc = docx.Document()

doc.add_paragraph("This is a new Doc")                       #this will add paragraph in new line
paraObject = doc.add_paragraph("I am Madoune Sid Ali,")      #add second line
paraObject.add_run("and i am a swimmer")                     #this will be added in the second line
#add pic to our doc
doc.add_picture("swimmer.jpg",width=docx.shared.Inches(4),height =docx.shared.Inches(3))
#save doc
doc.save('new.docx')