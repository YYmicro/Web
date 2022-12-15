<script setup>
import { ref, reactive, onMounted, computed } from "vue";
import Index from './Index.vue'
import researchIntro from './researchIntro.vue'
import news from './news.vue'

import researchProject from './researchProject.vue'
import team from './team.vue'
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
  '/researchintro': researchIntro,
  '/researchproject': researchProject
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
    <el-menu-item index="6"><p class="all_font">联系我们</p></el-menu-item>
  </el-menu>
  <component :is="currentView" />
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
</style>

