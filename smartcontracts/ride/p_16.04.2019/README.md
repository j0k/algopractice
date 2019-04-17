# flow

0. create 3 accounts in IDE

1. deploy
```
deploy(compile(env.file()))
```


2. addU
```
broadcast(invokeScript({dappAddress:address(env.accounts[0]), call:{function:"addU", args:[{type:"string", value:"_x_"},{type:"string", value:"3MxSXigQssEnK2ffdu6cNBYq6qNQ2uFsqdX"}]}}))
```

3. send waves
```
broadcast(transfer({recipient:address(env.accounts[1]), amount:100000000, fee:500000}))
```

4. invoke addU from aside account
```
broadcast(invokeScript({dappAddress:address(env.accounts[0]), call:{function:"addU", args:[{type:"string", value:"_x_"},{type:"string", value:"helo"}]}}))
```
