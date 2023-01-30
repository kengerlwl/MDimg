# 架构

在开发过程中，不可避免的需要下载各种程序的可执行文件。如何针对自己系统的发行版下载好久显得很重要。

如何查看系统架构

```
uname -a
```

- cpu的架构将决定其指令集，是否是RISC或者CISC。

- 公司

- - **Intel和AMD都是芯片公司**
  - Intel公司：用的架构大多是x86架构，x86_64架构，和IA64安腾架构。指令集是CISC（复杂指令集）
  - AMD也是个芯片公司，主业除了设计CPU（AMD不流片，所以没有制造）还有设计显卡（收购的ATI），**AMD设计的CPU和intel x86/x86_64系列兼容**。例如**AMD64**

## 例子



分类

- 很多时候注意看一下发行版就可以了。例如ubuntu，centos

- x86是指intel的开发的一种32位指令集
- x86_64，表示是x86指令集的64扩展（兼容32位的64位）。也兼容AMD64。（**x86_64,x64,AMD64基本上是同一个东西）**（AMD做64比intel要早）
- arm架构，用是精简指令集。M系列苹果就是arm64
- AArch64是ARMv8的一种执行状态。
- powerpc64le等，目标架构为64位[PowerPC](https://zh.m.wikipedia.org/wiki/PowerPC)和[Power Architecture](https://zh.m.wikipedia.org/wiki/Power_Architecture)处理器（很少用）



![image-20230116215725688](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/658b2b5c183fcf1e9130b23aa3785369/2af73444b80ec3a9311613ade8970541.png)







