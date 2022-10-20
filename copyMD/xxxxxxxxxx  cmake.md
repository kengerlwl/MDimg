```
 cmake .. -DENABLE_CJSON_UTILS=On -DENABLE_CJSON_TEST=Off -DCMAKE_INSTALL_PREFIX=$PWD



make DESTDIR=$pkgdir install


 PATH=$PATH:/root/Polar-Fuzz/Polar-AFL
```

