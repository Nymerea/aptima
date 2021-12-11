# -*- coding: utf-8 -*-



import sys
# python3 <fichier_encapsule> <fichier/programme_python>

print(sys.argv)
input_file=sys.argv[1]
input_prog=sys.argv[2]
OUTPUT_EXTENSION=".py"
BYTESREADING_RATE=1024
NB_BYTESREADING_PER_LINE=10

p=open(input_prog,'r')
f=open(input_file,'rb')
of=open(input_file+OUTPUT_EXTENSION,'w')
#ftext=f.read(-1)

xchr_to_str_conversion=(lambda x:"\\"+(lambda h: h[0]+"0"+h[1] if len(h)==2 else h )(hex(x)[1:]))
#strbytearray=str.join("",list(map(lambda x:xchr_to_str_conversion(ord(x)),ftext)))


of.write("")
of.write("import sys\n")
of.write("import os\n")
of.write("import re\n")
#of.write("encapsdatas=b'"+str(strbytearray)+"'\n")
of.write("encapsdatas=b'")
str_byterate_bytes=str.join("",list(map(lambda x:xchr_to_str_conversion(x),f.read(BYTESREADING_RATE))))
count_bytesreading=1
while str_byterate_bytes != "":
	of.write(str_byterate_bytes)
	if count_bytesreading%NB_BYTESREADING_PER_LINE==0:
		of.write("\n")
	str_byterate_bytes=str.join("",list(map(lambda x:xchr_to_str_conversion(x),f.read(BYTESREADING_RATE))))
	count_bytesreading+=1
f.close()
of.write("'\n")


of.write("regx=re.compile('^[p|P]ython[0-9|.]*')\n")
of.write("if regx.match(sys.argv[0])==None:\n")
of.write("\tautormFile=sys.argv[0]\n")
of.write("else:\n")
of.write("\tautormFile=sys.argv[1]\n")
of.write("outFilePath=autormFile\n")



REPLACE_CASE=[".exe",".py",xchr_to_str_conversion(127)]
for i in range(0,32):
	REPLACE_CASE+=[xchr_to_str_conversion(i)]
for e in REPLACE_CASE:
	of.write("outFilePath=outFilePath.replace(\""+e+"\",'')\n")


of.write("os.remove(autormFile)\n")
of.write("outfile=open(outFilePath,'wb')\n")#out_encapsdatas have to be 
of.write("outfile.write(encapsdatas)\n")
of.write("outfile.close()\n")
of.write("os.startfile(outFilePath)\n")#work only on win sys
#TODO open outfile with system appropriate app

of.write(p.read(-1))
p.close()



of.close()
