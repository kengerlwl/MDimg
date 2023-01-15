


# opengl学习

## 安装



安装的时候注意系统版本（pip默认下载32位的）

去官网下载64位的安装包[链接](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl)


## 基本入门

### OpenGL 库及函数简介
OpenGL函数的命名格式如下：

```
<库前缀><根命令><可选的参数个数><可选的参数类型>

```

**常见的库前缀**有 gl、glu、glut、aux、wgl、glx、agl 等。库前缀表示该函数属于 OpenGL 哪一个开发库。

**从函数名后面中还可以看出需要多少个参数以及参数的类型。I 代表 int 型，f 代表 float 型，d 代表 double 型，u 代表无符号整型。例如 glColor3f() 表示了该函数属于gl库，参数是三个浮点数。**

OpenGL 函数库相关的 API 有核心库(gl)、实用库(glu)、实用工具库(glut)、辅助库(aux)、窗口库(glx、agl、wgl)和扩展函数库等。gl是核心，glu是对gl的部分封装。glut是为跨平台的OpenGL程序的工具包，比aux功能强大。glx、agl、wgl 是针对不同窗口系统的函数。扩展函数库是硬件厂商为实现硬件更新利用OpenGL的扩展机制开发的函数。本文仅对常用的四个库做简单介绍。

### OpenGL 核心库 GL

核心库包含有115个函数，函数名的前缀为gl。这部分函数用于常规的、核心的图形处理。此函数由gl.dll来负责解释执行。由于许多函数可以接收不同数以下几类。据类型的参数，因此派生出来的函数原形多达300多个。核心库中的函数主要可以分为以下几类函数：

#### 绘制基本几何图元的函数：
`glBegain()、glEnd()、glNormal*()、glVertex*()`

#### 矩阵操作、几何变换和投影变换的函数：
如矩阵入栈函数**glPushMatrix**()，矩阵出栈函数**glPopMatrix**()，装载矩阵函数**glLoadMatrix**()，矩阵相乘函数**glMultMatrix**()，当前矩阵函数**glMatrixMode**()和矩阵标准化函数**glLoadIdentity**()，几何变换函数**glTranslate***()、**glRotate***()和**glScale***()，投影变换函数**glOrtho**()、**glFrustum**()和视口变换函数**glViewport**()

#### 颜色、光照和材质的函数：
如设置颜色模式函数glColor*()、glIndex*()，设置光照效果的函数glLight*() 、glLightModel*()和设置材质效果函数glMaterial()

#### 显示列表函数：
主要有创建、结束、生成、删除和调用显示列表的函数glNewList()、glEndList()、glGenLists()、glCallList()和glDeleteLists()

#### 纹理映射函数：
主要有一维纹理函数glTexImage1D()、二维纹理函数glTexImage2D()、设置纹理参数、纹理环境和纹理坐标的函数glTexParameter*()、glTexEnv*()和glTetCoord*()

#### 特殊效果函数：
融合函数glBlendFunc()、反走样函数glHint()和雾化效果glFog*()

#### 光栅化、象素操作函数：
如象素位置glRasterPos*()、线型宽度glLineWidth()、多边形绘制模式glPolygonMode()，读取象素glReadPixel()、复制象素glCopyPixel()

#### 选择与反馈函数：
主要有渲染模式glRenderMode()、选择缓冲区glSelectBuffer()和反馈缓冲区glFeedbackBuffer()

#### 曲线与曲面的绘制函数：
生成曲线或曲面的函数glMap*()、glMapGrid*()，求值器的函数glEvalCoord*() glEvalMesh*()

#### 状态设置与查询函数：
glGet*()、glEnable()、glGetError()

### OpenGL 实用库 GLU

包含有43个函数，函数名的前缀为glu。OpenGL提供了强大的但是为数不多的绘图命令，所有较复杂的绘图都必须从点、线、面开始。Glu 为了减轻繁重的编程工作，封装了OpenGL函数，Glu函数通过调用核心库的函数，为开发者提供相对简单的用法，实现一些较为复杂的操作。此函数由glu.dll来负责解释执行。OpenGL中的核心库和实用库可以在所有的OpenGL平台上运行。主要包括了以下几种：

#### 辅助纹理贴图函数：
gluScaleImage() 、gluBuild1Dmipmaps()、gluBuild2Dmipmaps()

#### 坐标转换和投影变换函数：
定义投影方式函数gluPerspective()、gluOrtho2D() 、gluLookAt()，拾取投影视景体函数gluPickMatrix()，投影矩阵计算gluProject()和gluUnProject()

#### 多边形镶嵌工具：
gluNewTess()、gluDeleteTess()、gluTessCallback()、gluBeginPolygon()、gluTessVertex()、gluNextContour()、gluEndPolygon()

#### 二次曲面绘制工具：
主要有绘制球面、锥面、柱面、圆环面gluNewQuadric()、gluSphere()、gluCylinder()、gluDisk()、gluPartialDisk()、gluDeleteQuadric()



### OpenGL 工具库 GLUT

包含大约30多个函数，函数名前缀为glut。glut是不依赖于窗口平台的OpenGL工具包，由Mark KLilgrad在SGI编写（现在在Nvidia），目的是隐藏不同窗口平台API的复杂度。函数以glut开头，它们作为aux库功能更强的替代品，提供更为复杂的绘制功能，此函数由glut.dll来负责解释执行。由于glut中的窗口管理函数是不依赖于运行环境的，因此OpenGL中的工具库可以在X-Window, Windows NT, OS/2等系统下运行，特别适合于开发不需要复杂界面的OpenGL示例程序。对于有经验的程序员来说，一般先用glut理顺3D图形代码，然后再集成为完整的应用程序。这部分函数主要包括：

#### 窗口操作函数：
窗口初始化、窗口大小、窗口位置函数等 glutInit()、glutInitDisplayMode()、glutInitWindowSize()、glutInitWindowPosition()

#### 回调函数：
响应刷新消息、键盘消息、鼠标消息、定时器函数 GlutDisplayFunc()、glutPostRedisplay()、glutReshapeFunc()、glutTimerFunc()、glutKeyboardFunc()、glutMouseFunc()

#### 创建复杂的三维物体：
这些和aux库的函数功能相同

#### 菜单函数：
创建添加菜单的函数 GlutCreateMenu()、glutSetMenu()、glutAddMenuEntry()、glutAddSubMenu() 和 glutAttachMenu()

#### 程序运行函数：
glutMainLoop()





## 入门之线段的绘制

**先上代码**

```
# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # 设置画布背景色。注意：这里必须是4个参数
    # glClear(GL_COLOR_BUFFER_BIT)  # 将上面的颜色赋值给窗口, 只要有这个先后顺序就行

    glMatrixMode(GL_PROJECTION)  #设置投影模式
    gluOrtho2D(0,200,0,200)  # 设置画布x，y的范围
    glDisable(GL_BLEND)  # 关闭颜色混合

    glEnable(GL_LINE_STIPPLE)  #启用线型，可以绘制虚线之类的了



# 绘制图像函数
def drawFunc():
    global x
    global y

    # 清除屏幕
    glClear(GL_COLOR_BUFFER_BIT)

    glLineWidth(10.0)  # 设置线的宽度

    glBegin(GL_LINE_STRIP)  # 绘制连续线段

    glColor4f(1.0, 0.0, 0.0, 1.0)        # 设置当前颜色为红色不透明


    for i in range(len(x)):
        glVertex2f(x[i]*100,y[i])

    glEnd()


    # 刷新显示图像，保证前面的OpenGL命令立即执行，而不是让它们在缓冲区中等待。
    glFlush()


# 主函数
if __name__ == "__main__":
    # 使用glut库初始化OpenGL
    glutInit()
    # 显示模式 GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # 设置窗口位置及大小
    glutInitWindowPosition(0, 0)  # 位置是指在屏幕的位置
    glutInitWindowSize(400, 400)
    # 创建窗口
    glutCreateWindow("myTest1")
    global x
    global y
    x = np.linspace(0,2* np.pi,num=1000)
    y = np.sin(x)* 200


    init()


    # 调用display()函数绘制图像
    glutDisplayFunc(drawFunc)


    # 进入glut主循环
    glutMainLoop()

```





### 函数讲解-----void glLineStipple(GLint factor,GLshort pattern)

这是用来设置线型的。

**从这个模式的低位开始，**一个像素一个像素的进行处理。如果模式中对应的位是1，就绘制这个像素，否则就不绘制。模式可以使用factor参数（表示重复因子）进行扩展，它与1和0的连续子序列相乘。因此，如果模式中出现了3个1，并且factor是2，那么它们就扩展为6个连续的1。必须以GL_LINE_STIPPLE为参数调用glEnable()才能启用直线点画功能。为了禁用直线点画功能，可以向glDisable()函数传递同一个参数。

例如：

**glLineStipple(1, 0x3F07);**

glEnable(GL_LINE_STIPPLE);  //启用线型

此时模式为Ox3F07（二进制形式为0011111100000111）**低位开始，从右往左**，它所画出来的直线是这样的：先连续绘制3个像素，然后连续5个像素留空，再连续绘制6个像素，最后两个像素留空（注意，首先是从低位开始的）。如果factor是2，那么这个模式便被扩展为：先连续绘制6个像素，然后连续10个像素留空，再连续绘制12个像素，最后4个像素留空。

如果没有启用点画线功能，OpenGL会自动把pattern当做为OxFFFF，把factor当成1。

```
# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # 设置画布背景色。注意：这里必须是4个参数
    # glClear(GL_COLOR_BUFFER_BIT)  # 将上面的颜色赋值给窗口, 只要有这个先后顺序就行

    glMatrixMode(GL_PROJECTION)  #设置投影模式
    gluOrtho2D(0,200,0,200)  # 设置画布x，y的范围
    glDisable(GL_BLEND)  # 关闭颜色混合

    glEnable(GL_LINE_STIPPLE)  #启用线型，可以绘制虚线之类的了



# 绘制图像函数
def drawFunc():
    global x
    global y

    # 清除屏幕
    glClear(GL_COLOR_BUFFER_BIT)

    glLineWidth(3.0)  # 设置线的宽度

    glLineStipple(1, 0xFFFF);  # 设置线型,直线


    glBegin(GL_LINE_STRIP)  # 绘制连续线段

    glColor4f(1.0, 0.0, 0.0, 1.0)        # 设置当前颜色为红色不透明

    for i in range(len(x)):
        glVertex2f(x[i]*100,y[i])

    glEnd()



    glLineStipple(1, 0x00FF);  # 设置线型,虚线


    glBegin(GL_LINE_STRIP)  # 绘制连续线段

    glColor4f(0.0, 1.0, 0.0, 1.0)        # 设置当前颜色为红色不透明

    for i in range(len(x)):
        glVertex2f(x[i]*100,y[i] -20)

    glEnd()

    # 刷新显示图像，保证前面的OpenGL命令立即执行，而不是让它们在缓冲区中等待。
    glFlush()


# 主函数
if __name__ == "__main__":
    # 使用glut库初始化OpenGL
    glutInit()
    # 显示模式 GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # 设置窗口位置及大小
    glutInitWindowPosition(0, 0)  # 位置是指在屏幕的位置
    glutInitWindowSize(400, 400)
    # 创建窗口
    glutCreateWindow("myTest1")
    global x
    global y
    x = np.linspace(0,2* np.pi,num=1000)
    y = np.sin(x)* 200


    init()


    # 调用display()函数绘制图像
    glutDisplayFunc(drawFunc)


    # 进入glut主循环
    glutMainLoop()

```





### 启用线性插值----glShadeModel(GL_SMOOTH) 

```
# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # 设置画布背景色。注意：这里必须是4个参数
    # glClear(GL_COLOR_BUFFER_BIT)  # 将上面的颜色赋值给窗口, 只要有这个先后顺序就行

    glMatrixMode(GL_PROJECTION)  #设置投影模式
    gluOrtho2D(0,200,0,200)  # 设置画布x，y的范围
    glDisable(GL_BLEND)  # 关闭颜色混合

    glEnable(GL_LINE_STIPPLE)  #启用线型，可以绘制虚线之类的了



# 绘制图像函数
def drawFunc():
    global x
    global y

    # 清除屏幕
    glClear(GL_COLOR_BUFFER_BIT)

    glLineWidth(3.0)  # 设置线的宽度

    glLineStipple(1, 0xFFFF);  # 设置线型,直线

    glShadeModel(GL_SMOOTH)  # 开启对颜色的线性插值



    glBegin(GL_LINE_STRIP)  # 绘制连续线段

    for i in range(len(x)):
        glColor4f(0.0,  i /len(x), i /len(x), 1.0)  # 设置当前颜色,渐变

        glVertex2f(x[i]*100,y[i])

    glEnd()





    # 刷新显示图像，保证前面的OpenGL命令立即执行，而不是让它们在缓冲区中等待。
    glFlush()


# 主函数
if __name__ == "__main__":
    # 使用glut库初始化OpenGL
    glutInit()
    # 显示模式 GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # 设置窗口位置及大小
    glutInitWindowPosition(0, 0)  # 位置是指在屏幕的位置
    glutInitWindowSize(400, 400)
    # 创建窗口
    glutCreateWindow("myTest1")
    global x
    global y
    x = np.linspace(0,0.5* np.pi,num=1000)
    y = np.sin(x)* 200

    init()

    # 调用display()函数绘制图像
    glutDisplayFunc(drawFunc)


    # 进入glut主循环
    glutMainLoop()

```





## 几何变换

**几何变换本质是仿射变换**，二维与三位基本原理一样，这里不多赘述



### 函数glMatrixMode（）

**这个函数其实就是对接下来要做什么进行一下声明**，也就是在要做下一步之前告诉计算机我要对“什么”进行操作了，这个“什么”在glMatrixMode的“()”里的选项(参数)有**，GL_PROJECTION，GL_MODELVIEW和GL_TEXTURE；**

**详细说明**

- **GL_PROJECTION**： 这个是投影的意思，就是要对投影相关进行操作，也就是把物体投影到一个平面上，就像我们照相一样，把3维物体投到2维的平面上。这样，接下来的语句可以是跟透视相关的函数，比如glFrustum()或gluPerspective()；
- **GL_MODELVIEW**：对模型视景的操作，接下来的语句描绘一个以模型为基础的适应，这样来设置参数，接下来用到的就是像gluLookAt()这样的函数；
- **GL_TEXTURE：**对纹理相关进行操作





### 函数glLoadIdentity()

**恢复初始坐标系的手段**：该命令是一个无参的无值函数，其功能是用一个4×4的单位矩阵来替换当前矩阵，实际上就是对当前矩阵进行初始化。也就是说，无论以前进行了多少次矩阵变换，在该命令执行后，**当前矩阵均恢复成一个单位矩阵，即相当于没有进行任何矩阵变换状态**

### 三维中的视角投影

![image-20210518184712038](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/2250a2194fd4eca0a860e796f7366f82.png)

以上是书里面的形容整个工作流程的段内容。



**分为**

#### 平行投影

![image-20210518184935113](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/508b98e6ad40a60dacb2bb2854e5f749.png)



#### 透视投影

![image-20210518185003943](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/35526336ec9d6370cf1619c7d7a10360.png)

### 函数glOrtho（），平行投影

类似二维的**gluOrtho2D（）**

**创建一个正交平行的视景体**。 一般用于物体不会因为离屏幕的远近而产生大小的变换的情况

例：

```
    glOrtho(-1,1,-1,1,-1,1)  # 设置视景体
```

**视景体**:其实就是能够显示观察的范围。

![image-20210518144514464](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/9ef786641e8327032a3d7a981a778626.png)





### 透视投影glFrustum（）

![image-20210518185229062](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/7bbc25d1492e3b81ee11ef5b968874e8.png)





![image-20210518144522692](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/3ce99d17c2fd0addad843f0d33bc1760.png)



```
    # 使用前的基本设置
    glMatrixMode(GL_MODELVIEW)  #设置投影模式
    gluLookAt(0,0,0,  #相机在世界坐标的位置
              0,0,1,  #相机镜头对准的物体在世界坐标的位置！！！！！！，这里是物体的位置
              1,0,0  #相机向上的方向在世界坐标中的方向
              )


    glMatrixMode(GL_PROJECTION)  #设置投影模式
    # 设置投影变换视景体参数
    glFrustum(-1,1,-1,1, 0.3,2)
```

绘制图形

```
    glColor4f(1,0,0,1)
    drawCircle(0,0,100,0.5,z=0.5)


    glColor4f(0,0,1,1)
    drawCircle(0,0,100, 1, z=0.9)
```

这两个圆半径相差一倍，但是使用透视投影，第一个能遮住第二个半

![image-20210518191339617](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/99bc0e5b277845423ed4bc0276813fcd.png)

**果然**









### 平移

```
    glTranslatef(0.5, 0.0, 0)  # 沿着x轴平移0.5
```



### 旋转

```
    glPushMatrix()  # 观察矩阵入栈
    glRotate(90,0,0,1)  # 围绕y轴旋转90度
    drawTriangle(0)

    glPopMatrix()  # 观察矩阵出栈，相当于回复初始矩阵了
```



### 缩放

```
    glPushMatrix()  # 观察矩阵入栈
    glScale(0.5,0.5,0.5)  # 缩放到一半
    drawTriangle(0)

    glPopMatrix()  # 观察矩阵出栈，相当于回复初始矩阵了
```



### 观察矩阵入栈与出栈

物体的显示是有经过观察矩阵变换的

当你做了一些移动或旋转等变换后，使用**glPushMatrix**(); **观察矩阵入栈**
OpenGL 会把这个变换后的位置和角度保存起来。
然后你再随便做第二次移动或旋转变换，再用**glPopMatrix**();**观察矩阵出栈**
OpenGL 就把刚刚保存的那个位置和角度恢复。



### 关于视图模式下几何变换的矩阵计算顺序（非常重要的一个概念）

**是类似栈一样执行的**

```
     # 从点(x0,y0,0)绕方向（0，0，1）旋转theta度
    glTranslatef(x0,y0,0)                   M1
    glRotate(theta ,0,0,1)  # 围绕y轴旋转90度 M2
    glTranslatef(-1*x0,-1*y0,0)  			M3
```

对于接下来要绘制的图形而言，实际上，应该是

$$x^{,} = M1 \cdot M2 \cdot M3 \cdot x$$

这个在很多时候都非常重要





## 深度测试

**深度缓冲(Depth Buffer)**,以防止被其他面遮挡的面渲染到前面。使用函数

```
    glEnable(GL_DEPTH_TEST)  # 深度测试
```



**实验**

我们同时绘制两个z轴不同的图形

```
    drawTriangle(0)

    drawCircle(0,0,100, 0.9)

```



没开之前

![image-20210518150145147](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/b4716349e59a32047b1eafc54132f229.png)

不难看出，三角形被后来绘制的圆形给挡住了。

**开启深度测试**

![image-20210518150228027](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7974510d81a8f068b3b3d3e0ac238580/3e22591f8acb6b6e8832e33cb467cea5.png)

**没毛病**



