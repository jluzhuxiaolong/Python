# file.py
#文件操作学习
import os;

def ReadFile(fileName): 
	file = open(fileName,"r+");
	str = file.read();
	print (str);
	
	for line in file.readlines():
		print(line);
	file.close();
	return;

def WriteFile(fileName,str): 
	file = open(fileName,"w+");
	file.write(str);
	
	file.close();
	file = open(fileName,"wb");
	file.write(str.encode(encoding='utf-8'));
	list = ["DemoDemo\n","DemoDemo\n","DemoDemo\n", ];
	file.writelines(list.encode(encoding='utf-8'));
	file.close();
	return;

def RenameFile(fileName): 
	os.rename(fileName,"rename.txt");
	return;

#ReadFile("file.txt");
#WriteFile("file.txt","Demo");
RenameFile("file.txt");
