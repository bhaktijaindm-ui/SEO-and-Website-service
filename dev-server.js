const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;

const rewrites = [
    { source: '/seo-service', destination: '/index.html' },
    { source: '/web-design-service', destination: '/index.html' },
    { source: '/seo-service/services', destination: '/services.html' },
    { source: '/web-design-service/services', destination: '/services.html' },
    { source: '/seo-service/blog', destination: '/blog.html' },
    { source: '/web-design-service/blog', destination: '/blog.html' },
    { source: '/seo-service/aboutus', destination: '/about.html' },
    { source: '/web-design-service/aboutus', destination: '/about.html' },
    { source: '/seo-service/contact', destination: '/contact.html' },
    { source: '/web-design-service/contact', destination: '/contact.html' },
    { source: '/seo-service/casestudies', destination: '/case-studies.html' },
    { source: '/web-design-service/casestudies', destination: '/case-studies.html' },
    { source: '/seo-service/pricing', destination: '/pricing.html' },
    { source: '/web-design-service/pricing', destination: '/pricing.html' }
];

const server = http.createServer((req, res) => {
    let url = req.url.split('?')[0];

    // Handle Rewrites
    const rewrite = rewrites.find(r => r.source === url);
    if (rewrite) {
        url = rewrite.destination;
    }

    // Serve Static Files
    let filePath = '.' + url;
    if (filePath === './' || filePath === './seo-service' || filePath === './web-design-service') {
        filePath = './index.html';
    }

    const extname = String(path.extname(filePath)).toLowerCase();
    const mimeTypes = {
        '.html': 'text/html',
        '.js': 'text/javascript',
        '.css': 'text/css',
        '.json': 'application/json',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.wav': 'audio/wav',
        '.mp4': 'video/mp4',
        '.woff': 'application/font-woff',
        '.ttf': 'application/font-ttf',
        '.eot': 'application/vnd.ms-fontobject',
        '.otf': 'application/font-otf',
        '.wasm': 'application/wasm'
    };

    const contentType = mimeTypes[extname] || 'application/octet-stream';

    fs.readFile(filePath, (error, content) => {
        if (error) {
            if (error.code == 'ENOENT') {
                fs.readFile('./404.html', (error, content) => {
                    res.writeHead(404, { 'Content-Type': 'text/html' });
                    res.end(content || '404 Not Found', 'utf-8');
                });
            } else {
                res.writeHead(500);
                res.end('Sorry, check with the site admin for error: ' + error.code + ' ..\n');
                res.end();
            }
        } else {
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(content, 'utf-8');
        }
    });
});

server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
    console.log(`Dashboard rewrites enabled.`);
});
