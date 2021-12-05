# -*- coding: utf-8 -*-



import sys
# python3 <fichier_encapsule> <fichier/programme_python>

print(sys.argv)
input_file=sys.argv[1]
input_prog=sys.argv[2]
OUTPUT_EXTENSION=".py"

p=open(input_prog,'r')
f=open(input_file,'rb')
bytesarray=f.read(-1)
print(bytesarray[0:10])

writetext=""
writetext="import sys\n"
writetext="import os\n"
writetext+="encapsdatas="+str(bytesarray)+"\n"


writetext+="outfile=open(\"out_encapsdatas\",'wb')\n"
writetext+="outfile.write(encapsdatas)\n"
writetext+="outfile.close()\n"


of=open(input_file+OUTPUT_EXTENSION,'w')
of.write(writetext)
of.write(p.read(-1))



of.close()
