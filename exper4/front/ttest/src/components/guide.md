# 开发手册
> ## 组件创建和引用
>> ### 创建
>>> 假设我们把导航栏组件放在了一个叫做menu.vue的文件中，这个组件将会以默认导出的形式被暴露给外部。所以我们不需要手动创建。<br/>
>>> 参数设置需要使用defineProps函数。比如我要设置2个名为A,B的参数。<br/>
>>> ```const props = defineProps(['A','B']);```<br/>
>>> 取得参数A可以参考以下代码,不一定用ref,ref只是vue在定义变量类型<br/>
>>> ```const defA = ref(props.A);```<br/>
>>> 以上都写在ts里，defA是template可使用的变量
>> ### 引用
>>> 当我们在其他vue文件里想要引用menu.vue，首先要import，后面的名字随便，注意避开vue关键字就行如下<br/>
>>> ```import MyMenu from './components/menu.vue'```<br/>
>>> 然后定义mymenu变量使得template可以使用，如下<br/>
>>> ```const mymenu = ref(MyMenu)```<br/>
>>> template使用例子如下<br/>
>>> ```<el-col :span="24">```<br/>
>>> ```<mymenu A="1" B="testkey"/>```<br/>
>>> ```</el-col>```<br/>

***

## 所有组件
> ### demo.vue
>> **description**
>>> guide.md的组件撰写demo。
>>>
>> **props**
>>> *props1* : 参数1的描述
>>>
>>> *props2* : 参数2的描述
>>>

> ### App/menu.vue
>> **description**
>>> 导航栏组件
>>>
>> **props**
>>> *defA* : 导航栏每个选项都有index，从左往右由1依次递增，defA指定默认激活项。如主页填1，则第一个选项底部出现一抹颜色，表示此项为激活项，用于指导用户清楚自己所在位置。
>>>
>>> *actColor(optional)* : 被选中项的背景主题颜色，使用#00ffff这种，默认值#409EFF。
>>>

> ### App/RecentNews.vue
>> **description**
>>> 最新动态组件，类型是card
>>>
>> **props**
>>> 

> ### App/Papers.vue
>> **description**
>>> 最新论文组件，类型是card
>>>
>> **props**
>>> 

> ### App/Papers.vue
>> **description**
>>> 研究方向组件，类型是card
>>>
>> **props**
>>> 