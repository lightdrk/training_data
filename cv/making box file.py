import csv
import json


box_list = []
move_to = r'C:\Users\arch\Desktop\tessdata\combining\cordinates'
folder_path = r'C:\Users\arch\Desktop\boxfile'
file_format = '.csv'
with open(r'C:\Users\arch\Desktop\boxfile\test1_csv.csv','r') as csvFile:
    inCSV = csv.reader(csvFile)
    for row in inCSV:
        print(r'C:\Users\arch\Desktop\boxfile\{}'.format(row[0].replace(row[0][row[0].find('.'):],'.txt')))
        with open(r'C:\Users\arch\Desktop\boxfile\{}'.format(row[0].replace(row[0][row[0].find('.'):],'.txt')),'r',encoding='utf-8') as GroundTruth:
            lines = GroundTruth.readlines()[int(row[2])]
            lines = lines.rstrip("\n")
            print(int(row[2]))
            print(lines)
            print(row[3])
            cordinates =  json.loads(row[3])
            with open(r'C:\Users\arch\Desktop\boxfile\{}'.format(row[0].replace(row[0][row[0].find('.'):],'.box')),'a',encoding='utf-8') as combine:
                combine.write(f"{lines} {cordinates['x']} {cordinates['y']} {cordinates['width']} {cordinates['height']}\n")