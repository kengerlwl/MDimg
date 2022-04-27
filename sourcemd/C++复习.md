# C++复习



### 关于写题OJ时候一些需要注意的

#### 多组数据

代表要实现循环输入输出

```
    string s;
    while(cin >> s) {
    }
    
    int n;
	while(~scanf("%d", &n)){
		
	}
```

#### 格式

英语中文得各种标点符号空格都是不一样得，要注意。

再c++中使用prinf输出**string**

- 为了与C兼容，在C中没有string类型，故必须通过string类对象的成员函数c_str()把string对象转换成C中的字符串样式。

- ```
  printf("%s\n", s.c_str());
  ```

- ```
  输入也是需要特殊处理
  string a;
  a.resize(100); //需要预先分配空间, 但是这样会使string的大小与预期不符，要注意
  scanf("%s", &a[0]);
  
  ```

- 



#### 递归得效率问题（不是说递归就拉了）

**因为函数调用本身是有开销的，所以一般认为递归会比循环的性能要差**。具体来说，相同函数的不断入栈出栈，有时间损耗。

递归得效率不高（10^6次方左右就拉了），所以再能够正推就尽量进行正推。

例如求斐波那契数列。



#### 输入输出得效率问题

cin 和cout比scanf和prinf效率要低不少，建议比赛用scanf和printf。

**scanf()使用**

```
scanf("format string",argument_list);
scanf("%d",&number);   要打上地址符号

```

**printf使用**

```
printf()函数的语法如下：
printf("format string",argument_list);  不用打上地址符号
```

常见转义符

```
\n  换行
%d int
%lld long long int
%c(字符)
%s(字符串)
%f(float)等)
```



#### 强制类型转换

```
long long lli;

int i;

lli =(long long) i * i;要给这里来个强制类型转换，否则计算结果就溢出了
```



#### 如何从一个数组中，找到最大值所在的位置的最小下标

```
```







### 基本数据类型

C++ 为程序员提供了种类丰富的内置数据类型和用户自定义的数据类型。下表列出了**七种基本的 C++ 数据类型**：

| 类型     | 关键字  |
| :------- | :------ |
| 布尔型   | bool    |
| 字符型   | char    |
| 整型     | int     |
| 浮点型   | float   |
| 双浮点型 | double  |
| 无类型   | void    |
| 宽字符型 | wchar_t |

#### **size_t**

size_t是一种无符号的整型数，它的取值没有负数，在数组中也用不到负数，而它的取值范围是整型数的双倍。sizeof操作符的结果类型是size_t，它在头文件中typedef为unsigned int类型。该类型保证能容纳实现所建立的最大对象的字节大小。



### 修饰符

类型还可以用关键字修饰

- signed
- unsigned
- short
- long

举例：

| 类型               | 位            | 范围                                                         |
| :----------------- | :------------ | :----------------------------------------------------------- |
| char               | 1 个字节      | -128 到 127 或者 0 到 255                                    |
| unsigned char      | 1 个字节      | 0 到 255                                                     |
| signed char        | 1 个字节      | -128 到 127                                                  |
| int                | 4 个字节      | -2147483648 到 2147483647                                    |
| unsigned int       | 4 个字节      | 0 到 4294967295                                              |
| signed int         | 4 个字节      | -2147483648 到 2147483647                                    |
| short int          | 2 个字节      | -32768 到 32767                                              |
| unsigned short int | 2 个字节      | 0 到 65,535                                                  |
| signed short int   | 2 个字节      | -32768 到 32767                                              |
| long int           | 8 个字节      | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807      |
| signed long int    | 8 个字节      | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807      |
| unsigned long int  | 8 个字节      | 0 到 18,446,744,073,709,551,615                              |
| float              | 4 个字节      | 精度型占4个字节（32位）内存空间，+/- 3.4e +/- 38 (~7 个数字) |
| double             | 8 个字节      | 双精度型占8 个字节（64位）内存空间，+/- 1.7e +/- 308 (~15 个数字) |
| long double        | 16 个字节     | 长双精度型 16 个字节（128位）内存空间，可提供18-19位有效数字。 |
| wchar_t            | 2 或 4 个字节 | 1 个宽字符                                                   |



### 关于&&和||运算得优先级

要注意这里面是有着短路得运算得思路得。

而且对于一个队列得判断，应该先判断这个队列是否为空，在对队列就进行引用。

`while (!working.empty() && working.top().startTime <= ts )`



### typedef 声明

您可以使用 **typedef** 为一个已有的类型取一个新的名字。下面是使用 typedef 定义一个新类型的语法：

```
typedef type newname; 
```

### 枚举类型

枚举类型(enumeration)是C++中的一种派生数据类型，它是由用户定义的若干枚举常量的集合。

如果一个变量只有几种可能的值，可以定义为枚举(enumeration)类型。所谓"枚举"是指将变量的值一一列举出来，变量的值只能在列举出来的值的范围内。

创建枚举，需要使用关键字 **enum**。枚举类型的一般形式为：

```
enum 枚举名{ 
     标识符[=整型常数], 
     标识符[=整型常数], 
... 
    标识符[=整型常数]
} 枚举变量;
    
```

如果枚举没有初始化, 即省掉"=整型常数"时, 则从第一个标识符开始。





### C++ 中的变量声明

变量声明向编译器保证变量以给定的类型和名称存在，**这样编译器在不需要知道变量完整细节的情况下也能继续进一步的编译**。变量声明只在编译时有它的意义，在程序连接时编译器需要实际的变量声明。



```
// 函数声明
int func(); // 如果没有这句就会报错
 
int main()
{
    // 函数调用
    int i = func();
}
 
// 函数定义
int func()
{
    return 0;
}
```

### 变量作用域

**全局变量**

**在所有函数外部定义的变量（通常是在程序的头部），称为全局变量**。全局变量的值在程序的整个生命周期内都是有效的。

全局变量可以被任何函数访问。也就是说，全局变量一旦声明，在整个程序中都是可用的。下面的实例使用了全局变量和局部变量：

**全局变量初始化**

```
long long memo[1000001];// 全局备忘录默认是0，局部就拉了。 
```



### 常量#define 和 const

**宏定义 #define 和常量 const 的区别**

**类型和安全检查不同**

宏定义是字符替换，没有数据类型的区别，同时这种替换没有类型安全检查，可能产生边际效应等错误；

const常量是常量的声明，有类型区别，需要在编译阶段进行类型检查

**编译器处理不同**

宏定义是一个"编译时"概念，在预处理阶段展开，不能对宏定义进行调试，生命周期结束与编译时期；

const常量是一个"运行时"概念，在程序运行使用，类似于一个只读行数据

**存储方式不同**

宏定义是直接替换，不会分配内存，存储与程序的代码段中；

const常量需要进行内存分配，存储与程序的数据段中

**定义域不同**

```
void f1 ()
{
    #define N 12
    const int n 12;
}
void f2 ()
{
    cout<<N <<endl; //正确，N已经定义过，不受定义域限制
    cout<<n <<endl; //错误，n定义域只在f1函数中
}
```

**定义后能否取消**

宏定义可以通过#undef来使之前的宏定义失效

const常量定义后将在定义域内永久有效



### goto语句

C++ 中 **goto** 语句的语法：

```
goto label;
..
.
label: statement;
```





### 函数参数

如果函数要使用参数，则必须声明接受参数值的变量。这些变量称为函数的**形式参数**。

形式参数就像函数内的其他局部变量，在进入函数时被创建，退出函数时被销毁。

当调用函数时，有三种向函数传递参数的方式：

| 调用类型                                                     | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [传值调用](https://www.runoob.com/cplusplus/cpp-function-call-by-value.html) | 该方法把参数的实际值赋值给函数的形式参数。在这种情况下，修改函数内的形式参数对实际参数没有影响。 |
| [指针调用](https://www.runoob.com/cplusplus/cpp-function-call-by-pointer.html) | 该方法把参数的地址赋值给形式参数。在函数内，该地址用于访问调用中要用到的实际参数。这意味着，修改形式参数会影响实际参数。 |
| [引用调用](https://www.runoob.com/cplusplus/cpp-function-call-by-reference.html) | 该方法把参数的引用赋值给形式参数。在函数内，该引用用于访问调用中要用到的实际参数。这意味着，修改形式参数会影响实际参数。 |



### C++ 随机数

在许多情况下，需要生成随机数。关于随机数生成器，有两个相关的函数。一个是 **rand()**，该函数只返回一个伪随机数。生成随机数之前必须先调用 **srand()** 函数。

下面是一个关于生成随机数的简单实例。实例中使用了 **time()** 函数来获取系统时间的秒数，通过调用 rand() 函数来生成随机数：

实例

```
#include <iostream>
#include <ctime>
#include <cstdlib>
 
using namespace std;
 
int main ()
{
   int i,j;
 
   // 设置种子
   srand( (unsigned)time( NULL ) );
 
   /* 生成 10 个随机数 */
   for( i = 0; i < 10; i++ )
   {
      // 生成实际的随机数
      j= rand();
      cout <<"随机数： " << j << endl;
   }
 
   return 0;
}
```

### 数组


在 C++ 中要声明一个数组，需要指定元素的类型和元素的数量，如下所示：

```
type arrayName [ arraySize ];
```

**初始化数组**

```
double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};
```

**多维数组**

```
type name[size1][size2]...[sizeN];
```



### 字符串

这里只讲**string**

| 序号 | 函数 & 目的                                                  |
| :--- | :----------------------------------------------------------- |
| 1    | **strcpy(s1, s2);** 复制字符串 s2 到字符串 s1。              |
| 2    | **strcat(s1, s2);** 连接字符串 s2 到字符串 s1 的末尾。连接字符串也可以用 **+** 号，例如: `string str1 = "runoob"; string str2 = "google"; string str = str1 + str2;` |
| 3    | **strlen(s1);** 返回字符串 s1 的长度。                       |
| 4    | **strcmp(s1, s2);** 如果 s1 和 s2 是相同的，则返回 0；如果 s1<s2 则返回值小于 0；如果 s1>s2 则返回值大于 0。 |
| 5    | **strchr(s1, ch);** 返回一个指针，指向字符串 s1 中字符 ch 的第一次出现的位置。 |
| 6    | **strstr(s1, s2);** 返回一个指针，指向字符串 s1 中字符串 s2 的第一次出现的位置。 |

注意，**字符和字符串不一样**

```
char c = 'c';
string s= "string";
char a = s[0];
```

一个单引号，一个双。



#### **字符串分割**

```
		s.substr(s.begin(), s.begin() +5)
```

#### **字符串反转**

```
		reverse(s.begin(), s.end());
```

#### 字符串切割spilt

通过使用string的find函数。

```

 
vector<string>  split(const string& str,const string& delim) { //将分割后的子字符串存储在vector中
	vector<string> res;
	if("" == str) return  res;
	
	string strs = str + delim; //*****扩展字符串以方便检索最后一个分隔出的字符串
	size_t pos; //size_t 类型 
	size_t size = strs.size();
 	int i =0 ;
	while(i < size){ 
		pos = strs.find(delim, i); //pos为分隔符第一次出现的位置，从i到pos之前的字符串是分隔出来的字符串,这个是从i开始找，包括i。返回的是匹配到的第一个的首index。 
		if( pos < size) { //如果查找到，如果没有查找到分隔符，pos为string::npos
			string s = strs.substr(i, pos - i);//*****从i开始长度为pos-i的子字符串
			res.push_back(s);//两个连续空格之间切割出的字符串为空字符串，这里没有判断s是否为空，所以最后的结果中有空字符的输出，
			i = pos + delim.size() - 1;
		}
		i = pos+ delim.size();
		
	}
	
	
	return res;	
}


int main(){
	string a = "1,2,。3,。4,5,。";
	vector<string> ans;
	ans = split(a, ",。");
	cout << ans.size() << endl; 
	for(int i =0; i < ans.size(); i++){
		cout << ans[i] << endl;
	}
	
}
```





### 字符串转换成数字

- stoi() string类型字符串转换为int

- stod() string类型字符串转换为double

- to_string() 重载方法，将一些整形，浮点型等转换为string类型字符串(好像不能用了)

- 换个能用得{}

  - ```
    #include<sstream> //为了使用 stringstream ss
    #include<stdlib.h>  //为了使用 c_str() 函数 
    
    
    
    string i_s(int n)//int 转 string 
    {
    	string s;
    	stringstream ss;
    	ss<<n;
    	ss>>s;
    	return s;
    }
    ```

    



### cctype 数据类型判断

- isalnum() 判断一个字符是不是alphanumeric，即大小写英文字母或是数字
- isalpha() 判断一个字符是不是alphabetic，即英文字母
- isdigit() 判断一个字符是不是数字
- tolower() 将大写转换为小写
- toupper() 将小写转换为大写

### 指针

#### 定义

**指针**是一个变量，其值为另一个变量的地址，即，内存位置的直接地址。就像其他变量或常量一样，您必须在使用指针存储其他变量地址之前，对其进行声明。指针变量声明的一般形式为：

```
type *var-name;
```

```
int    *ip;    /* 一个整型的指针 */
double *dp;    /* 一个 double 型的指针 */
float  *fp;    /* 一个浮点型的指针 */
char   *ch;    /* 一个字符型的指针 */
```



#### 关于&和*

符号&代表取值，符号*代表解引用：

| 符号 | 意义   |
| ---- | ------ |
| &    | 取地址 |
| *    | 解引用 |



#### **指针与数组**

我们知道，一维数组名本身就是一个指针

```cpp
int arr[] = {1, 2, 3, 4, 5};
int* p1 = arr;
int* p2 = &arr[0];
int* p3 = &arr;    //报错
```

在定义了指向数组首元素的指针变量后，我们可以通过这个指针变量来访问数组元素：

```cpp
 int arr[] = { 1,2,3,4,5 };
  int* p1 = arr;
  int length = sizeof(arr) / sizeof(int);
  for (int i = 0; i < length; i++)
  {
    cout << p1[i] << endl;
    cout << *(p1 + i) << endl;
  }
```



**数组名作为函数传递的时候，会退化成一个指针**



### 引用

引用变量是一个别名，也就是说，它是某个已存在变量的另一个名字。一旦把引用初始化为某个变量，就可以使用该引用名称或变量名称来指向变量。

```
实例
#include <iostream>
 
using namespace std;
 
int main ()
{
   // 声明简单的变量
   int    i;
   double d;
 
   // 声明引用变量
   int&    r = i;
   double& s = d;
   
   i = 5;
   cout << "Value of i : " << i << endl;
   cout << "Value of i reference : " << r  << endl;
 
   d = 11.7;
   cout << "Value of d : " << d << endl;
   cout << "Value of d reference : " << s  << endl;
   
   return 0;
}
```

引用传递得意思。



### 标准IO

| 头文件     | 函数和描述                                                   |
| :--------- | :----------------------------------------------------------- |
| <iostream> | 该文件定义了 **cin、cout、cerr** 和 **clog** 对象，分别对应于标准输入流、标准输出流、非缓冲标准错误流和缓冲标准错误流。 |
| <iomanip>  | 该文件通过所谓的参数化的流操纵器（比如 **setw** 和 **setprecision**），来声明对执行标准化 I/O 有用的服务。 |
| <fstream>  | 该文件为用户控制的文件处理声明服务。我们将在文件和流的相关章节讨论它的细节。 |







### STL模板

C++ 标准模板库的核心包括以下三个组件：

| 组件                | 描述                                                         |
| :------------------ | :----------------------------------------------------------- |
| 容器（Containers）  | 容器是用来管理某一类对象的集合。C++ 提供了各种不同类型的容器，比如 deque、list、vector、map 等。 |
| 算法（Algorithms）  | 算法作用于容器。它们提供了执行各种操作的方式，包括对容器内容执行初始化、排序、搜索和转换等操作。 |
| 迭代器（iterators） | 迭代器用于遍历对象集合的元素。这些集合可能是容器，也可能是容器的子集。 |



#### 字典

**内部实现机理**

- map： **map内部实现了一个红黑树**，该结构具有自动排序的功能，因此map内部的所有元素都是有序的，红黑树的每一个节点都代表着map的一个元素，因此，**对于map进行的查找，删除，添加等一系列的操作都相当于是对红黑树进行这样的操作，故红黑树的效率决定了map的效率。**
- unordered_map: unordered_map内部实现了一个哈希表，因此其元素的排列顺序是杂乱的，无序的

#### map红黑树使用

**存入**

```
map<int,int> count;
count[i]=1;
```

**查找**

```
如果key存在，则find返回key对应的迭代器，如果key不存在，则find返回尾后迭代器 .end()。可以参考下面的示例来判断key值是否存在

if (mymap.find(key) == mymap.end())
    cout << "没有这个key" << endl;
```

**统计次数**

```
count函数
count函数用于统计key值在map中出现的次数，map的key不允许重复，因此如果key存在返回1，不存在返回0

if (mymap.count(key) == 0)
```

**取值**

Map中元素取值主要有at和[ ]两种操作，at会作下标检查，而[]不会。

如果[]取值index是不存在的元素，那么直接返回0；

```
	for(int i=0; i < 10; i++){
		if(m.find(i) == m.end()){
			m[i] =1;
		}else{
			m[i]++;
		}
	}
	
	map<int,int>::iterator iter1 = m.begin(); // 红黑树按照顺序打印出来
	while(iter1 != m.end()){
		cout << (*iter1).first;
		iter1++;
	}
	
	cout << endl;
	
	
	cout << m[10];//  返回0
```





**删除**

- 通过迭代器删除
- 通过key值删除

```
// 删除迭代器指向位置的键值对，并返回一个指向下一元素的迭代器
iterator erase( iterator pos )

// 删除一定范围内的元素，并返回一个指向下一元素的迭代器
iterator erase( const_iterator first, const_iterator last );

// 根据Key来进行删除， 返回删除的元素数量，在map里结果非0即1
size_t erase( const key_type& key );

// 清空map，清空后的size为0
void clear();
```



**遍历**

```
 map<int, int>::iterator iter;
    iter = _map.begin();
    while(iter != _map.end()) {
        cout << iter->first << " : " << iter->second << endl;
        iter++;
    }
```





#### vector 使用

**初始化大小**

```
vector<int> ans(10,0); 10个0
vector(begin,end):复制[begin,end)区间内另一个数组的元素到vector中// 相当于切片
```

**插入**


- void push_back(const T& x):向量尾部增加一个元素X
- iterator insert(iterator it,const T& x):向量中迭代器指向元素前增加一个元素x



**遍历**

```
    cout<<"直接利用数组："; 
    for(int i=0;i<10;i++)//方法一 
    {
        cout<<obj[i]<<" ";
    }
 
    cout<<endl; 
    cout<<"利用迭代器：" ;
    //方法二，使用迭代器将容器中数据输出 
    vector<int>::iterator it;//声明一个迭代器，来访问vector容器，作用：遍历或者指向vector容器的元素 
    for(it=obj.begin();it!=obj.end();it++)
    {
        cout<<*it<<" ";
    }
```





**删除函数**

- iterator erase(iterator it):删除向量中迭代器指向元素
- iterator erase(iterator first,iterator last):删除向量中[first,last)中元素
- void pop_back():删除向量中最后一个元素

- iterator insert(iterator it,const_iterator first,const_iterator last):向量中迭代器指向元素前插入另一个相同类型向量的[first,last)间的数据



**切片复制**

```
   	srand( (unsigned)time(NULL) );
	for(int i =0; i < 10; i++){
		double tmp = 1.0 * rand() / RAND_MAX;
		cout << tmp << " ";
		pq.push_back(tmp);
	}
	cout << endl;
	
	
//	vector<double> a(pq.begin(), pq.begin()+5);  第一种复制的思路

	vector<double>a;  // 第二种复制的思路
	a.insert(a.begin(),pq.begin(), pq.begin()+5);
	for(int i = 0; i < a.size(); i++){
		cout << a[i] << " ";
	}

```

属于深拷贝



**拷贝**

```
	vector<int> a(10,0);
	
	vector<int> b =a; // 这俩是不一样得函数，
	b[0]=1;
	show(a);
	show(b);
	
	//同样，对于push_back函数
	a.push_back(b)// 假如b是一个vector,那么也是深拷贝，是俩不一样得。不是push得指针。
```





#### set 库

**存入**

```
a.insert(i);
```

**统计**

**count()** 用来查找set中某个某个键值出现的次数。这个函数在set并不是很实用，因为一个键值在set只可能出现0或1次，这样就变成了判断某一键值是否在set出现过了。

**查找**

```
find()  ，返回给定值值得定位器，如果没找到则返回end()。
```





**查找邻近元素**

```
**lower_bound、upper_bound**返回迭代器是相同

- 关键字val在集合中不存在，二者返回结果一样，都是按照集合实例化时给定的Compare比较，不在val之前的第一个元素（亦即之后或者等于，如果按照默认的比较类型less，函数返回的是≥val的最小的元素）；
- 如果关键在val在集合中存在，**lower_bound返回val关键字本身的迭代器，upper_bound返回关键字val下一个元素迭代器**
```





**删除**

```
erase(iterator)  ,删除定位器iterator指向的值

erase(first,second),删除定位器first和second之间的值

erase(key_value),删除键值key_value的值
```

**遍历**

```
	cout << "便利集合"<< endl; 
	set<double>::iterator iter = s.begin();
	while(iter != s.end()){
		cout << *iter << endl;
		iter++; 
	}
```



**边际查找**

**lower_bound、upper_bound**返回迭代器是相同

- 关键字val在集合中不存在，二者返回结果一样，都是按照集合实例化时给定的Compare比较，不在val之前的第一个元素（亦即之后或者等于，如果按照默认的比较类型less，函数返回的是≥val的最小的元素）；
- 如果关键在val在集合中存在，**lower_bound返回val关键字本身的迭代器，upper_bound返回关键字val下一个元素迭代器**





```
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <ctime>
using namespace std;
typedef long long int  lli;
const int a = 1000000007;

set<double> s;

int main(){
	
	
   	srand( (unsigned)time(NULL) );
	for(int i =0; i < 10; i++){
		double tmp =  rand() % 100;
//		cout << tmp << " ";
		s.insert(tmp);
	}
	
	cout << "便利集合"<< endl; 
	s.insert(50);

	set<double>::iterator iter = s.begin();
	while(iter != s.end()){
		cout << *iter << endl;
		iter++; 
	}
	
	set<double>::iterator iter2 = s.upper_bound(50);
	
	cout<< "比50大的元素是" ;
	while(iter2!= s.end()) {
		cout << *iter2<< " ";
		iter2++;
	}
	cout << endl; 
	
	set<double>::iterator iter3 = s.lower_bound(50);
	
	cout<< "比50小的元素是" ;
	while(iter3!= s.end()) {
		cout << *iter3<< " ";
		iter3--;
	}
} 
```





#### 栈

和其他序列容器相比，stack 是一类存储机制简单、所提供操作较少的容器。下面是 stack 容器可以提供的一套完整操作：

- top()：返回一个栈顶元素的引用，类型为 T&。如果栈为空，返回值未定义。
- push(const T& obj)：可以将对象副本压入栈顶。这是通过调用底层容器的 push_back() 函数完成的。
- push(T&& obj)：以移动对象的方式将对象压入栈顶。这是通过调用底层容器的有右值引用参数的 push_back() 函数完成的。
- pop()：弹出栈顶元素。
- size()：返回栈中元素的个数。
- empty()：在栈中没有元素的情况下返回 true。
- emplace()：用传入的参数调用构造函数，在栈顶生成对象。
- swap(stack<T> & other_stack)：将当前栈中的元素和参数中的元素交换。参数所包含元素的类型必须和当前栈的相同。对于 stack 对象有一个特例化的全局函数 swap() 可以使用。



#### 优先级队列（默认是最大堆）

```
#include <queue>
```

具体方法

和队列基本操作相同:

- top 访问队头元素
- empty 队列是否为空
- size 返回队列内元素个数
- push 插入元素到队尾 (并排序)
- emplace 原地构造一个元素并插入队列
- pop 弹出队头元素
- swap 交换内容

定义：`priority_queue<Type, Container, Functional>`

**默认是最大堆**

**最后一个参数是比较函数**

```
#include <iostream>
#include <queue>
using namespace std;

//方法1
struct tmp1 //运算符重载<
{
    int x;
    tmp1(int a) {x = a;}
    bool operator<(const tmp1& a) const
    {
        return x < a.x; //大顶堆
    }
};

//方法2
struct tmp2 //重写仿函数
{
    bool operator() (tmp1 a, tmp1 b) 
    {
        return a.x < b.x; //大顶堆
    }
};

int main() 
{
    tmp1 a(1);
    tmp1 b(2);
    tmp1 c(3);
    priority_queue<tmp1> d;
    d.push(b);
    d.push(c);
    d.push(a);
    while (!d.empty()) 
    {
        cout << d.top().x << '\n';
        d.pop();
    }
    cout << endl;

    priority_queue<tmp1, vector<tmp1>, tmp2> f;
    f.push(c);
    f.push(b);
    f.push(a);
    while (!f.empty()) 
    {
        cout << f.top().x << '\n';
        f.pop();
    }
}

```



#### 迭代器
#####  顺序容器
对于序列式容器(如vector,deque)，序列式容器就是数组式容器，删除一个元素导致后面所有的元素会向前移动一个位置。
```
#include<vector>
#include<iostream>
#include<ctime>
using namespace std;

int main(){

	vector<int> v;
	for(int i = 1; i<= 10; i++){
		v.push_back(i);
	}

	vector<int>::iterator iter = v.begin();

	iter +=5;

	cout << "current point is  ";
	cout << (*iter) << endl;

	vector<int>::iterator next = 	v.erase(iter);
	cout << "after delete , the point is  ";
	cout << (*iter) << endl;	

	cout << (iter == next);
}
```


##### 关联式容器
对于关联容器(如map, set,multimap,multiset)，删除当前的iterator，仅仅会使当前的iterator失效，只要在erase时，递增当前iterator即可。这是因为map之类的容器，使用了红黑树来实现，插入、删除一个结点不会对其他结点造成影响。erase迭代器只是被删元素的迭代器失效，**但是返回值为void**，经过该操作后的迭代器基本失效，不能用了。
```
#include<vector>
#include<iostream>
#include<ctime>
#include<set>
using namespace std;

void p(set<int> &se){
	set<int>::iterator i = se.begin();
	while(i!= se.end()){
		cout << (*i) << "  ";
		i++;
	}
	cout << endl;
}

int main(){

	set<int> s;
	for(int i = 1; i<= 10; i++){
		s.insert(i);
	}
	p(s);
	set<int>::iterator iter = s.begin();

	iter++;

	cout << "current point is  ";
	cout << (*iter) << endl;

	s.erase(iter);

	p(s);

	cout << "after delete , the point is  ";
	cout << (*iter) << endl;	
}
```


#### 运算符重载与容器（优先级队列）的自定义运算法则

这里注意，默认来说，STL了里面的比较一般都是<或者==；所以一般只用重载这两个函数。
或者直接选择重载比较函器。

注意要保证内外运算的变量的一致性。
同理，这里的重载方式，也可用在其他STL容器中应用。
例如：
- sort排序
- set集合中的比较
```
#include<vector>
#include<iostream>
#include<ctime>
#include<queue>
using namespace std;

class node{
public:
	int val;
	bool const operator == (const node& n)  const {
		bool f =this->val == n.val;
		return f;
	}

	// 这里的两个 const都要才能实现对priority的运算符重载，因为内外要一致 
	bool const operator < (const node& n)  const {
		bool f =this->val < n.val;
		return f;
	}
};


int main(){
	priority_queue<node> pq;
	for(int i = 1; i<= 10; i++){
		node t;
		t.val =11- i;
		pq.push(t);
	}
	while(!pq.empty()){
		std::cout << pq.top().val << "  ";
		pq.pop();
	}

}
```







### algorithm库得方法

#### **排序**



以下思路对vector等容易也有用

```
vector
bool compare(int a,int b) 
{ 
    return a< b; //升序排列，如果改为return a>b，则为降序 
} 
int a[20]={2,4,1,23,5,76,0,43,24,65},i; 
for(i=0;i<20;i++) 
    cout<< a[i]<< endl; 
sort(a,a+20,compare);
sort(a.begin(), a.end(), cmp) //或者



```

**sort与二维数组vector<vector<int>>**

与python是一样的。按照先左后右的排序思路排序下去。



#### **反转**vector

```
reverse(ans.begin(), ans.end());
```

这里是引用过去得，相当于直接改变了



#### 二分查找

**lower_bound：**

功能：查找非递减序列[first,last) 内第**一个大于或等于**某个元素的位置。

- 意思就是，先看有没有等于的，如果有，那么就返回左边第一个等于的，
- 如果没有，那么返回第一个比target大的。

返回值：如果找到返回找到元素的地址否则返回last的地址。（这样不注意的话会越界，小心）

用法：int t=lower_bound(a+l,a+r,key)-a；(a是数组)。

**upper_bound:**

功能：查找非递减序列[first,last) 内**第一个大于**某个元素的位置。

- 直接找第一个比target大的。

返回值：如果找到返回找到元素的地址否则返回last的地址。（同样这样不注意的话会越界，小心）

用法：int t=upper_bound(a+l,a+r,key)-a；(a是数组)。

**使用思路**

```
#include <iostream>
#include <algorithm>
 
using namespace std;
 
int board[5] = {1,2,3,4,5};
 
int main(){
	
	sort(board,board+5);
	int* t1 = lower_bound(board,board+5,3); //返回的是地址 
	int index = t1 - board; // 计算出索引
	
	cout<<*t1<<' '<< t1 - board<<endl;
	
	return 0;
}
```

**vector二分**

```
   vector<int> v = matrix[i];    		
   vector<int>::iterator t = lower_bound(v.begin(), v.end(), target) ;
   int index == t - v.begin()； //计算出索引。
```



### cmath库得使用

#### 取整

```
#include<cmath>
ceil()
floor()
```

