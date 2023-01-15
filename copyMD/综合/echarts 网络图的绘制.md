# echarts 网络图的绘制

文档与相关资源
[官方的文档](https://github.com/pyecharts/pyecharts-gallery)
[官方样例网站](https://echarts.apache.org/examples/en/index.html#chart-type-graph)
[不错的教程](https://blog.csdn.net/LSGO_MYP/article/details/117463653)


[数据](https://echarts.apache.org/examples/data/asset/data/)

## 基本demo

代码,这里是指输入到jupyter中的输出框中
```
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK # 不能省略，解决依赖问题

nodes = [
    opts.GraphNode(name="结点1", symbol_size=10),
    opts.GraphNode(name="结点2", symbol_size=20),
    opts.GraphNode(name="结点3", symbol_size=30),
    opts.GraphNode(name="结点4", symbol_size=40),
    opts.GraphNode(name="结点5", symbol_size=50),
]
links = [
    opts.GraphLink(source="结点1", target="结点2", value=2, linestyle_opts=opts.LineStyleOpts(width=2),),
    opts.GraphLink(source="结点2", target="结点3", value=3, linestyle_opts=opts.LineStyleOpts(width=3),),
    opts.GraphLink(source="结点3", target="结点4", value=4, linestyle_opts=opts.LineStyleOpts(width=4),),
    opts.GraphLink(source="结点4", target="结点5", value=5, linestyle_opts=opts.LineStyleOpts(width=5)),
    opts.GraphLink(source="结点5", target="结点3", value=6, linestyle_opts=opts.LineStyleOpts(width=6)),
]
c = (
    Graph()
    .add("", nodes, links, repulsion=4000,
         edge_label=opts.LabelOpts(is_show=True,position="middle",formatter="{c}")
         )
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink"))
)

c.render_notebook()
```
结果

![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/74d9467d0f68679807eade1929f22c8e/d7394b4a8be8595f7371311cdbcd4ea3.png)

## 各种属性设置

上面demo中的add函数可以更改以下属性
```
def add(
    # 系列名称，用于 tooltip 的显示，legend 的图例筛选。
    series_name: str,

    # 关系图节点数据项列表，参考 `opts.GraphNode`
    nodes: Sequence[Union[opts.GraphNode, dict]],

    # 关系图节点间关系数据项列表，参考 `opts.GraphLink`
    links: Sequence[Union[opts.GraphLink, dict]],

    # 关系图节点分类的类目列表，参考 `opts.GraphCategory`
    categories: Union[Sequence[Union[opts.GraphCategory, dict]], None] = None,

    # 是否选中图例。
    is_selected: bool = True,

    # 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
    is_focusnode: bool = True,

    # 是否开启鼠标缩放和平移漫游。
    is_roam: bool = True,

    # 节点是否可拖拽，只在使用力引导布局的时候有用。
    is_draggable: bool = False,

    # 是否旋转标签，默认不旋转。
    is_rotate_label: bool = False,

    # 图的布局。可选：
    # 'none' 不采用任何布局，使用节点中提供的 x， y 作为节点的位置。
    # 'circular' 采用环形布局。
    # 'force' 采用力引导布局。
    layout: str = "force",

    # 关系图节点标记的图形。
    # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 
    # 'diamond', 'pin', 'arrow', 'none'
    # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。
    symbol: Optional[str] = None,

    # 关系图节点标记的大小
    # 可以设置成诸如 10 这样单一的数字
    # 也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为20，高为10。
    symbol_size: types.Numeric = 10,

    # 边的两个节点之间的距离，这个距离也会受 repulsion。
    # 支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长。
    edge_length: Numeric = 50,

    # 节点受到的向中心的引力因子。该值越大节点越往中心点靠拢。
    gravity: Numeric = 0.2,

    # 节点之间的斥力因子。
    # 支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
    repulsion: Numeric = 50,

     # Graph 图节点边的 Label 配置（即在边上显示数据或标注的配置）
    edge_label: types.Label = None,

    # 边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。
    # 默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol: ['circle', 'arrow']
    edge_symbol: Optional[str] = None,

    # 边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
    edge_symbol_size: Numeric = 10,

    # 标签配置项，参考 `series_options.LabelOpts`
    label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),

    # 关系边的公用线条样式。
    linestyle_opts: Union[opts.LineStyleOpts, dict] = opts.LineStyleOpts(),

    # 提示框组件配置项，参考 `series_options.TooltipOpts`
    tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,

    # 图元样式配置项，参考 `series_options.ItemStyleOpts`
    itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
)

```

### 节点属性设置
在添加的时候可以设置
```
nodes = [
    opts.GraphNode(
        name= node['name'],
        symbol_size=10, # 节点的显示大小
        value=20, #节点值，点击节点就会显示
        category=node['category'], # 种类
        x,y#属性只有在特定的layout下才能生效
    )
    for node in data['nodes']
]
```
节点的颜色可以用种类的不同区分，不同的种类会自动分配不同颜色。

### 边的属性设置
边的属性设置如下
```
links = [
    opts.GraphLink(
        source=edge['source'],
        target=edge['target'],
        value=10,# 设置线的值
        #设置线的宽度和曲度
        linestyle_opts=opts.LineStyleOpts(width=1, curve=0.2)
    )
    for edge in data['links']
]
```

### label开启标签显示
在add函数中显示
```
点的label
label_opts=opts.LabelOpts(is_show=True),

# 边的label
edge_label=opts.LabelOpts(is_show=True, position='middle', formatter='{b}的数据{c}')

```
![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/74d9467d0f68679807eade1929f22c8e/7809717571c0f8d65568ac57726720ef.png)


### 显示侧边种类
```
G.set_global_opts(
    legend_opts=opts.LegendOpts(is_show=True,orient='vertical', pos_left='2%', pos_top='20%')

)
```
![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/74d9467d0f68679807eade1929f22c8e/f804ceb357d17ee616fc07a180a815ca.png)


### 重力的设置
重力是控制所有的节点向中心聚集的引力

默认是0.2，我们改成1
![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/74d9467d0f68679807eade1929f22c8e/bbf3e9748703343c0d30120b442b0c18.png)

### 关于斥力的设置
repulsion=50：节点之间的斥力因子，支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大

