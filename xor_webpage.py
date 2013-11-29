# -*- coding: utf-8 -*-

'''
Example:

/madXOR
	xor_webpage.py
	/templates
	/xor_webpage.html

We need to encrypt xor_webpage.html

>> import xor
>> x = xor.Xor()
>> x.encrypt('xor_webpage.html', 'templates/encrypted.html', 'templates/xor_webpage.key', 7)

The first param is the file to be encrytped
The second param is the output file
The third param is the key output
The forth param is the start entropy

Now start xor_webpage.py

python xor_webpage.py

Open the browser at http://127.0.0.1:5000

'''

__author__ = ["A'mmer Almadani:Mad_Dev", "penbang.sysbase.org"]
__email__  = ["mad_dev@linuxmail.org", "mail@sysbase.org"]


from flask import Flask, request, render_template
from xor import Xor
import hashlib


app = Flask(__name__)

path = app.root_path + '/templates/'
encrypted_file = '/encrypted.html'

@app.route('/')
def index():
	return '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<title>XOR-WEBPAGE</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta name="generator" content="Geany 1.22" />
	<link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>
</head>

<body style="text-align: center; background-color: #303030; color: #00a7e1; font-family: 'Open Sans Condensed', sans-serif; font-size: 25px">
	</br>
	</br>
	<a style='color: #00a7e1; size: 17px' href='/encrypted'>Encrypted Page</a></br></br>
	<div style="font-size: 15px; color: #e7e7e7">This is an example of what the end product might act like</br>
	Simply add </div><div style="font-size: 16px; color: #00a7e1">'?key=KEY'</div>	<div style="font-size: 15px; color: #e7e7e7"> and </div><div style="font-size: 16px; color: #00a7e1">'xor.decrypt()'</div><div style="font-size: 15px; color: #e7e7e7"> will decrypt the page and redirect you to the decrypted page.</br>
	The output file is md5ed ( md5(key) + .html )</br> I will work on other versions and other deployment methods</div>

	
</body>

</html>'''

@app.route('/decrypt')
def decryptHtml(ns):
	h = hashlib.md5()
	h.update(ns)
	hashKey = h.hexdigest()
	outPut_file = hashKey + '.html'
	xor.decrypt(path+encrypted_file, ns, path+outPut_file)
	return render_template(outPut_file)

@app.route('/encrypted', methods = ['GET'])
def paramTest():
	key = request.args.get('key', None)
	if key is None:
		return render_template(encrypted_file)
	else:
		return decryptHtml(key)
		 

if __name__ == '__main__':
	xor = Xor()
	app.run(debug=True)