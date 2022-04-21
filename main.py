from datetime import date, datetime


def calculate_age_nowadays(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def calculate_age_next(born,year):
    next = datetime(int(year),1,1)
    return next.year - born.year - ((next.month, next.day) < (born.month, born.day))

def splitAttributes(line, currently):
    attributes = line.split(",")
    dateAttribute = attributes[0].split("/")
    x = datetime(int(dateAttribute[2]), int(dateAttribute[1]), int(dateAttribute[0]))
    if currently:
        age = calculate_age_nowadays(x)
    else:
        age = calculate_age_next(x,2028)
    return replaceAge(line,attributes[0],age)

def replaceAge(line, currentDate, currentAge):
    return(line.replace(currentDate, str(currentAge)))

def readFile(fileArff):
    val = False
    if fileArff == "datosFict1.arff":
        val = True
    with open(fileArff,"r") as file:
        data = False
        newText = []
        for line in file:
            if line.find('@data') != -1:
                data = True
                newText.append(line)
                continue
            if data:
                newText.append((splitAttributes(line,val)))
            else:
                newText.append(line)
        return newText

def createFile(text,file):
    with open(file,'w') as file:
        for line in text:
            if line.find('date') != -1:
                file.write("@attribute age integer\n")
            else:
                file.write(line)

if __name__ == '__main__':
    text1 = readFile("datosFict1.arff")
    createFile(text1,'newDatosFict1.arff')
    text2 = readFile("datosFict2.arff")
    createFile(text2, 'newDatosFict2.arff')






