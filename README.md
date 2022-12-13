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
3. 初始化环境 : ```vue create hello-world``` : 选manual手动 : 选Typescript不是Javascript : 其他默认
4. 自动安装环境 : ```cnpm install```
5. 运行 : ```cnpm run serve```
6. 如果vuecli脚手架存在极其严格的语法检查，建议google然后手动关闭

## 引用element-plus
1. 安装 : ```cnpm install element-plus --save```
2. 在src文件夹下main.ts里添加 : 
    ```
    import ElementPlus from "element-plus";
    import "element-plus/dist/index.css";
    ```
    并修改CreateApp为 : 
    ```createApp(App).use(ElementPlus).mount("#app");```

## 引用bootstrap5其他前端框架
1. 引用css:在```<style></style>```里添加一行，引号的链接可以换成其他
   
   ```@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";```
2. 引用js:在```<script lang='ts' setup></script>```里添加如下，script.src可以换成其他
   ```
   onMounted(() => {
    let script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js';
    document.body.appendChild(script);
    })
   ```
## 打包挂github
1. 在vue.config.js引入publicpath，不然网页最后会成空白。
   ```
   module.exports = defineConfig({
        publicPath: './'
    });
   ```
2. 运行命令cnpm run build，得到dist文件夹
3. 将dist文件夹里所有东西上传到github，dist这个文件夹不需要，index.html需要在最外面。
4. 后续参考github web pages搭建教程