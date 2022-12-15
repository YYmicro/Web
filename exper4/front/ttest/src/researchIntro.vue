<script setup>
import { onMounted, ref, computed } from "vue"
import HPC from './components/researchIntro/HPC.vue'
import GCS from './components/researchIntro/GraphicsComputingSystem.vue'
import NotFound from './NotFound.vue'

const hpc = ref(HPC);
const gcs = ref(GCS);
const notfound = ref(NotFound);
const now = ref(HPC);

function getItem(item) {
  if(item == 'hpc'){
    console.log('hpc');
    now.value = hpc.value;
  }else if(item == 'gcs'){
    console.log('gcs');
    now.value = gcs.value;
  }else{
    now = notfound;
  }
}

onMounted(() => {
  let script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js';
  document.body.appendChild(script);
})
// // 导航栏组合式
// const researches = {
//   '/researchintro': HPC,
//   '/researchintro/gcs': GCS
//   // '/researchintro': researchIntro,
// }
// // 在上面添加新的页面
// const researchPath = ref(window.location.hash)
// window.addEventListener('hashchange', () => {
//   researchPath.value = window.location.hash
// })
// const researchView = computed(() => {
//   console.log("researchintro\n")
//   // console.log(researchPath.value)
//   // console.log(researchPath.value.slice(1))
//   // console.log(researchPath.value.slice(1) || '/')
//   console.log(researches[researchPath.value.slice(1) || '/'])
//   return researches[researchPath.value.slice(1) || '/'] || NotFound
// })
</script>
<template>
    <div class="common-layout">
      <el-container>
        <el-container style="height:100%;">
        <el-aside class="sidebar" width="200px" style="background-color:azure;height:100%">
            <el-menu default-active="1">
                  <!-- <el-menu-item index="1"><a href="#/researchintro">高性能计算</a></el-menu-item>
                  <el-menu-item index="2"><a href="#/researchintro/gcs">图计算系统</a></el-menu-item> -->
                  <el-menu-item index="1" @click="getItem('hpc')">高性能计算</el-menu-item>
                  <el-menu-item index="2" @click="getItem('gcs')">图计算系统</el-menu-item>
                  <el-menu-item index="3">深度学习</el-menu-item>
                  <el-menu-item index="4">计算机视觉</el-menu-item>
                  <el-menu-item index="5">绿色计算</el-menu-item>
            </el-menu>
        </el-aside>
        <el-main>
          <now />
          <!-- <component :is="researchView" /> -->
        </el-main>
      </el-container>
      </el-container>
    </div>
</template>