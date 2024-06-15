
while 1:
    print('This code is used to convert references in Pubmed form into Chinese form')
    print('Conversion may fail if full stop punctuation('\.') is included')
    print('References that fail to convert will not appear in the results, and will be displayed at the end')
    print('\n')

    filename = input("Please input filename(txt):")
    try:
        f1 = open(r'{}.txt'.format(filename), mode='r', encoding='utf-8')
    except Exception:
        print('wrong file name!')
        continue
    file = f1.readlines()
    f1.close()

    page = ''
    for i in file:
        line = ''
        z = i.split('.')
        q = z[3].split(';')
        #z[0]name；z[1]title；z[2]periodical；z[3]time；z[4]Volume and page；z[5-]doi
        line = z[0]+'.'+z[1]+'[J]'+'.'+z[2]+','+q[0][0:5]+', '+q[1]+'.'
        page += line
        page += '\n'
    print('**finish**')
    print(page)

    f2 = open(r'{}.txt'.format(filename), mode='w', encoding='utf-8')
    f2.write(page)
    f2.close()

    sttop = input('Whether to continue (press c to continue):')
    if sttop == 'c':
        continue
    else:
        break
