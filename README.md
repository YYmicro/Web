# Web
Vue+flask+mysql

* Web-origin : 初次成功的文件夹,作保留备份
* exper1 : 简单的登录审核
* exper2 : 99乘法表
* exper3 : 组合式+ts
* exper4 : HDACP实验室管理系统


# 指导
1. 用npm安装cnpm : ```npm install -g cnpm -registry=https://registry.npm.taobao.org```
2. 安装vue脚手架 : ```cnpm install -g @vue/cli```
3. 初始化环境 : ```vue create hello-world``` : 选vue3或者默认 : 选Typescript不是Javascript
4. 运行 : ```cnpm run serve```
5. 打包 : ```cnpm run build``` : 得到dist文件夹

## 引用element-plus
1. 安装 : ```cnpm install element-plus --save```
2. 在src文件夹下main.ts里添加 : 
        ```
        import ElementPlus from "element-plus";
        import "element-plus/dist/index.css";
        ```
    并修改CreateApp为 : 
        ```createApp(App).use(ElementPlus).mount("#app");```