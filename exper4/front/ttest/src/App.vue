<script setup>
import { ref, reactive, onMounted, computed } from "vue";
import Index from './Index.vue'
import researchIntro from './researchIntro.vue'
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
  '/researchintro': researchIntro
}
// 在上面添加新的页面
const currentPath = ref(window.location.hash)
window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>

<template>
  <el-menu :default-active="defA" :active-text-color="active_color" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1" class="home"><a href="#/"><p class="home_font all_font">HDACP</p></a></el-menu-item>
    <el-menu-item index="2"><a href="#/researchintro"><p class="all_font">研究介绍</p></a></el-menu-item>
    <el-menu-item index="3"><p class="all_font">科研团队</p></el-menu-item>
    <el-menu-item index="4"><p class="all_font">新闻动态</p></el-menu-item>
    <el-menu-item index="5"><p class="all_font">科研项目</p></el-menu-item>
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

