# -*- coding: utf-8 -*-



import sys
# python3 <fichier_encapsule> <fichier/programme_python>

print(sys.argv)
input_file=sys.argv[1]
input_prog=sys.argv[2]
OUTPUT_EXTENSION=".py"

p=open(input_prog,'r')
f=open(input_file,'r')
ftext=f.read(-1)

xchr_to_str_conversion=(lambda x:"\\"+(lambda h: h[0]+"0"+h[1] if len(h)==2 else h )(hex(x)[1:]))
strbytearray=str.join("",list(map(lambda x:xchr_to_str_conversion(ord(x)),ftext)))
writetext=""
writetext+="import sys\n"
writetext+="import os\n"
writetext+="import re\n"
writetext+="encapsdatas=b'"+str(strbytearray)+"'\n"

writetext+="regx=re.compile('^[p|P]ython[0-9|.]*')\n"
writetext+="if regx.match(sys.argv[0])==None:\n"
writetext+="\tautormFile=sys.argv[0]\n"
writetext+="else:\n"
writetext+="\tautormFile=sys.argv[1]\n"
writetext+="outFilePath=autormFile\n"



REPLACE_CASE=[".exe",".py",xchr_to_str_conversion(127)]
for i in range(0,32):
	REPLACE_CASE+=[xchr_to_str_conversion(i)]
for e in REPLACE_CASE:
	writetext+="outFilePath=outFilePath.replace(\""+e+"\",'')\n"


writetext+="os.remove(autormFile)\n"
writetext+="outfile=open(outFilePath,'wb')\n"#out_encapsdatas have to be 
writetext+="outfile.write(encapsdatas)\n"
writetext+="outfile.close()\n"
#TODO open outfile with system appropriate app


of=open(input_file+OUTPUT_EXTENSION,'w')
of.write(writetext)
of.write(p.read(-1))



of.close()
