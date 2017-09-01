dataMaster = ""
with open('All.m3u', "r", encoding="cp1252") as file:
	for data in file:
		# if "Zelda" in data:
		# 	print("yes")
		data1 = data.replace("\\", "/")
		data2 = data1.replace("C:/Users/Max/", "/storage/emulated/0/")
		if(data2.startswith("#")):
			# print(data2)
			data2 = ""
		data2 = data2.replace(".mp3.mp3", ".mp3")
		dataMaster = dataMaster + data2
	file.close()
# print(dataMaster)
with open('All.m3u', "w") as file:
	file.write(dataMaster)
	file.close()