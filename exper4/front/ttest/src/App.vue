<script setup>
import { ref, reactive, onMounted, computed } from "vue";

import Index from './Index.vue'
import researchIntro from './researchIntro.vue'
import news from './news.vue'
import researchProject from './researchProject.vue'
import team from './team.vue'
  import t_wxy from "./components/team/t_resume/wxy.vue"
  import t_hjq from "./components/team/t_resume/hjq.vue"
  import t_jjf from "./components/team/t_resume/jjf.vue"
  import t_zy from "./components/team/t_resume/zy.vue"
  import t_zgj from "./components/team/t_resume/zgj.vue"
  import t_wl from "./components/team/t_resume/wl.vue"
  import t_bhd from "./components/team/t_resume/bhd.vue"
import contactUs from './contactUs.vue'
import NotFound from './NotFound.vue'

const props = defineProps(['defA','actColor']);
const defA = ref(props.defA);
const active_color = ref("#409EFF");
active_color.value = props.actColor;
// console.log(props.defA)

const handleSelect = () => {

}
onMounted(() => {

})
// 导航栏组合式
const routes = {
  '/': Index,
  '/news': news,
  '/team' : team,
  '/team/teacher/wxy' : t_wxy,
  '/team/teacher/hjq' : t_hjq,
  '/team/teacher/jjf' : t_jjf,
  '/team/teacher/zy' : t_zy,
  '/team/teacher/zgj' : t_zgj,
  '/team/teacher/wl' : t_wl,
  '/team/teacher/bhd' : t_bhd,
  '/researchintro': researchIntro,
  '/researchproject': researchProject,
  '/contactus': contactUs
}
// 在上面添加新的页面
const currentPath = ref(window.location.hash)
window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  console.log("index\n")
  console.log(routes[currentPath.value.slice(1) || '/'])
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>

<template>
  <el-menu :default-active="defA" :active-text-color="active_color" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1" class="home">
      <a href="#/">
        <p class="home_font all_font">HDACP</p>
      </a>
    </el-menu-item>
    <el-menu-item index="2"><a href="#/researchintro"><p class="all_font">研究介绍</p></a></el-menu-item>
    <!-- <el-sub-menu index="2">
      <template #title><a href="#/researchintro"><p class="all_font">研究介绍</p></a></template>
      <el-menu-item index="2-1">高性能计算</el-menu-item>
      <el-menu-item index="2-2">图计算系统</el-menu-item>
      <el-menu-item index="2-3">深度学习</el-menu-item>
      <el-menu-item index="2-3">计算机视觉</el-menu-item>
      <el-menu-item index="2-3">绿色计算</el-menu-item>
    </el-sub-menu> -->
    <el-menu-item index="3"><a href="#/team"><p class="all_font">科研团队</p></a></el-menu-item>
    <el-menu-item index="4"><a href="#/news"><p class="all_font">新闻动态</p></a></el-menu-item>
    <el-menu-item index="5"><a href="#/researchproject"><p class="all_font">科研项目</p></a></el-menu-item>
    <el-menu-item index="6"><a href="#/contactus"><p class="all_font">联系我们</p></a></el-menu-item>
  </el-menu>
  <component :is="currentView" />
  <br/><br/><br/><br/>
  <el-row style="background-color: rgba(0, 0, 0,0.22); color:black; padding-top: 50px;">
    <el-col :span="1"></el-col>
    <el-col :span="6">
      <el-row>
        <el-col :span="18">
          <el-image class="image-hover" :src='require("./assets/Index/fig0.png")' />
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
    </el-col>
    <el-col :span="1"></el-col>
    <el-col :span="8">
      <h5>扫描下方二维码关注青海大学计算机系公众号</h5>
      <el-row>
        <el-col :span="6">
          <el-image :src='require("./assets/Index/qrcode.jpg")' />
        </el-col>
        <el-col :span="18"></el-col>
      </el-row>
      
    </el-col>
    <el-col :span="1"></el-col>
    <el-col :span="6">
      <h5>地址</h5>
      <!-- <el-divider /> -->
      <el-link>青海省西宁市宁大路251号</el-link><br/>
      <el-link>青海大学计算机技术与应用系111实验室</el-link><br/>
      <el-divider/>
      <h5>常用链接</h5>
      <!-- <el-divider /> -->
      <el-link href="https://www.qhu.edu.cn/">青海大学</el-link><br/>
      <el-link href="https://cs.qhu.edu.cn/">青海大学计算机技术与应用系</el-link><br/>
      <el-link href="https://www.ccf.org.cn/">中国计算机学会</el-link><br/>
      <br/><br/>
    </el-col>
    <el-col :span="1"></el-col>
  </el-row>
</template>


<style>
.all_font{
  font-weight:bold;
  margin: 2px;
  font-size: 16px;
}
.home{
  background-color: rgb(0, 183, 195);
  /* background-color: #00ffff; */
}
.home_font{
  color: white;
  font-size:18px;
}
a{text-decoration: none;}

@keyframes example {
  0%    {}
  10%   {transform: rotateX(120deg) scale(1.05,1.05);}
  20%   {transform: rotateX(120deg) scale(1.10,1.10);}
  30%   {transform: rotateX(120deg) rotateY(120deg)  scale(1.15,1.15);}
  40%   {transform: rotateY(120deg) scale(1.20,1.20);}
  50%   {transform: rotateY(120deg) rotateZ(120deg) scale(1.25,1.25);}
  60%   {transform: rotateZ(120deg) scale(1.30,1.30);}
  70%   {transform: rotateZ(120deg) scale(1.35,1.35);}
  80%   {transform: scale(1.40,1.40);}
  90%   {transform: scale(1.25,1.25);}
  100%  {transform: scale(1,1);}
}
.image-hover{
  
}
.image-hover:hover{
  /* transition: transform 0.6s; */
    /* transform: scale(0.95,0.95); */
    animation-name: example;
    animation-duration: 3s;
    /* animation-iteration-count: 1; */
    animation-fill-mode: both;
}
</style>

