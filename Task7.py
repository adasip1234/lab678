def jswxml(x, y):
    data = task2(x)
    xml_data = dicttoxml(data).decode('utf-8')
    donexml(y, xml_data)
    print("utworzono nowy plik .xml")

def ymlwxml(x, y):
    data = task4(x)
    donexml(y, data)
    print("utworzono nowy plik .xml")

def donexml(x, data):
    data = {"root": data}
    xml_data = xmltodict.unparse(data)
    with open(x, 'w') as f:
        f.write(xml_data)
        
        #Dodaje tez reszte kodu bo nie ma gdzie indziej dac 
        
 def rozszerzenie():
    if file_extension == ".json":
        if file_extension_new == ".xml":
            jswxml(x, y)
        elif file_extension_new == ".yml":
            jswyml(x, y)

    elif file_extension == ".xml":
        if file_extension_new == ".json":
            xmlwjs(x, y)
        elif file_extension_new == ".yml":
            xmlwyml(x, y)

    elif file_extension == ".yml":
        if file_extension_new == ".json":
            ymlwjs(x, y)
        elif file_extension_new == ".xml":
            ymlwxml(x, y)


sciezka()
rozszerzenie()
