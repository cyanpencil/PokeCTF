const express     = require('express');
const http        = require('http');
const formidable  = require('formidable');
const path        = require('path');
const crypto      = require('crypto');
const querystring = require('querystring');
const Browser     = require('zombie');

const app       = express();
const host      = '0.0.0.0';
const port      = 5004;
const uploadDir = 'uploaded_files';
const key       = crypto.randomBytes(32);
process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;

// Landing page
app.get('/', (req, res) => {

	res.send(
`
<form action='upload' method='post' enctype='multipart/form-data'>
	<input type='file' name='filetoupload'/><br>
	<input type='submit' value='Upload file'/>
</form>
<form action='click' method='get'>
	<code>http:\/\/www.cyanpencil.xyz:5004/</code><input type='text' name='path'/><br>
	<input type='submit' value='Submit link'/>
</form>
`	)

});

// File upload
app.post('/upload', (req, res) => {

	let form = new formidable.IncomingForm();
	form.maxFileSize = 10*1024;
	form.uploadDir = uploadDir;
	form.parse(req, (err, fields, files) => {
		if (files.filetoupload) {

			let uid = path.basename(files.filetoupload.path);
			res.send(
`
<p>File uploaded <a href='/files/${uid}'>here!</a></p>
`			)
		} else {
			res.sendStatus(403);
		}
	});
});

// Generate a secure download token
app.get('/files/:uid', (req, res) => {

	let uid = req.params.uid;
	let params = generateDownloadParams(uid);
	res.redirect('/download?' + querystring.stringify(params));

});

// Generates encrypted and signed parameters to access a file
generateDownloadParams = uid => {

	let headers = querystring.stringify({
		d : 'attachment',
		t : 'text/plain',
		id: uid
	});
	let iv = crypto.randomBytes(16);
	let cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
	let headers_encrypted = Buffer.concat([cipher.update(headers), cipher.final()]);
	let mac = crypto.createHmac('sha256', key).update(headers_encrypted);
	return {
		iv     : iv.toString('base64'),
		headers: headers_encrypted.toString('base64'),
		mac    : mac.digest('base64')
	};

}

// File download
app.get('/download', (req, res) => {

	let iv = Buffer.from(req.query.iv,'base64');
	let headers_encrypted = Buffer.from(req.query.headers,'base64');

	// Reject the query if the headers were tampered with
	let mac = req.query.mac;
	let mac_check = crypto.createHmac('sha256', key).update(headers_encrypted);
	if(mac != mac_check.digest('base64')) {
		res.sendStatus(403);
		return;
	}

	// Otherwise, decipher the headers
	let cipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
	let headers = querystring.parse(Buffer.concat([cipher.update(headers_encrypted), cipher.final()]).toString('utf-8'));

	// Set the headers
	res.set('Content-Disposition', headers.d);
	res.set('Content-Type', headers.t);
	res.sendFile(uploadDir + '/' + headers.id, {root: __dirname});
});

// URL click
app.get('/click', (req, res) => {
	let url = 'http://www.cyanpencil.xyz:5004/' + req.query.path;
	const browser = new Browser();
	browser.setCookie({
		name: 'flag',
		value: 'poke{Wha7_1s_7his_CO0ki3_4boUt}',  // flag redacted from source code :P
		domain: 'cyanpencil.xyz'
	});
	browser.visit(url, () => {});
	res.sendStatus(200);
});

app.listen(port, host, () => console.log(`App listening on ${host}:${port}`));
