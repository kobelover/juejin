# juejin
这是通过python SDK的形式，来展示掘金种的数据

# install
```
git clone https://github.com/ryan-bin/juejin.git
cd juejin
python setup.py install
```

# Usage
```
from juejin import get_juejin
for i in get_juejin():
    print(i.decode('utf-8'))
    print("\n")
```
默认是展示20条数据，分类为全部，文章类型为hot(hot=热门， new=最新)
src为sixgold(sixgold返回数据中有条数，web没有条数)

# 分类说明
Category.Android    安卓

Category.Frontend	前端

Category.IOS		iOS

Category.Backend	后端

Category.Design		设计

Category.Product	产品

Category.Freebie	工具资源

Category.Article	阅读

Category.AI 		人工智能

Category.All    	所有