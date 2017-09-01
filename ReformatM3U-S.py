dataMaster = ""
with open('playlist.m3u', "r") as file:
	for data in file:
		data1 = data.replace("\\", "/")
		data2 = data1.replace("C:/Users/Max/", "/storage/emulated/0/")
		if(data2.startswith("#")):
			data2 = ""
		dataMaster = dataMaster + data2
	file.close()
with open('playlist.m3u', "w") as file:
	file.write(dataMaster)
	file.close()