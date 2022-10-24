# -*- coding: UTF-8 -*-
import os

arqX = open('jsons\\Data_X.json', "w", encoding='utf8')
arqY = open('jsons\\Data_Y.json', "w", encoding='utf8')

for filePath in os.listdir('jsons'):
	if(filePath[-1] == 'n' and filePath[0] != 'D'):
		if(filePath[-6] == 'X'):
			print(filePath)
			print(filePath[:-6] + 'Y' + filePath[-5:])

			dataX = open('jsons\\' + filePath, "r", encoding='utf8')
			dataY = open('jsons\\' + filePath[:-6] + 'Y' + filePath[-5:], "r", encoding='utf8')
			
			for line in dataX:
				arqX.write(line)
			dataX.close()

			for line in dataY:
				arqY.write(line)
			dataY.close()

arqX.close()
arqY.close()