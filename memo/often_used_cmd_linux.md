1. 添加ssh秘钥：

```bash
ssh-add ~/.ssh/XXX.pem
```

~~~flow
```flow
st=>start: typo
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```
~~~