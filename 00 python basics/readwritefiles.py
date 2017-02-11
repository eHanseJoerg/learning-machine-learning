fw = open('sample.txt', 'w')
fw.write('Write a first line in the text file\n')

#ich brauch das \n für den Zeilenumbruch

fw.write('I like bacon')

fw.close()


fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()

