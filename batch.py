import sys, os, base64
from urllib.parse import unquote
from urllib.parse import quote

usage = '''\nUsage: this.py [obf|deobf]\nHave a file called list.txt in your working directory,\nwhich lists your HTML files, separated by new lines.\n\nNOTE: Files deobfuscated with this tool MUST have been obfuscated with it as well.'''

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)
	
opr=sys.argv[1]
lisfile = "list.txt"
if not os.path.isfile(lisfile):
	print ('''\nCould not find list.txt!''')
	sys.exit(0)

rawlis = open(lisfile, 'r').read()
htlis = rawlis.splitlines()
if htlis == []:
	print ('''\nList.txt is empty!''')
	sys.exit(0)

begst = '''<!DOCTYPE html>
<script type="text/javascript">
document.write(decodeURIComponent(atob(\''''

endst = '''\')));
</script>
<noscript>You must enable javascript in your browser to view this webpage.</noscript>
'''


if opr == "obf":
	for file in htlis:
		if not os.path.isfile(file):
			print ('''Could not find %s!''' % file)
			continue
		data = open(file, 'r').read()
		data = quote(data)
		data = data.encode("utf-8")
		data = base64.b64encode(data)
		data = data.decode("utf-8")
		data = begst + data + endst
		out = open(file, 'w').write(data)
		print("Succesfully Obfuscated %s" % file)
	
elif opr == "deobf":
	for file in htlis:
		if not os.path.isfile(file):
			print ('''Could not find %s!''' % file)
			continue
		data = open(file, 'r').read()
		data = data[88:-102]
		data = data.encode("utf-8")
		data = base64.b64decode(data)
		data = data.decode("utf-8")
		data = unquote(data)
		out = open(file, 'w').write(data)
		print("Succesfully Deobfuscated %s" % file)
	
else:
    print(usage)
    sys.exit(0)
