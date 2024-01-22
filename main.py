fileInput = open("input.txt", 'r')
fileOutput = open("output.txt", "w")
sp = [int(float(lines.strip('\n'))) for lines in fileInput]
fileOutput.write(str(sum(sp)))
fileOutput.close()
fileInput.close()
