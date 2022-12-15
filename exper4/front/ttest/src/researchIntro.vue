<script setup>
import { onMounted, ref, computed } from "vue"
import HPC from './components/researchIntro/HPC.vue'
import GCS from './components/researchIntro/GraphicsComputingSystem.vue'
import dl from './components/researchIntro/DeepLearning.vue'
import CV from './components/researchIntro/ComputerVision.vue'
import GC from './components/researchIntro/GreenComputing.vue'
import NotFound from './NotFound.vue'

const hpc = ref(HPC);
const gcs = ref(GCS);
const DL = ref(dl);
const cv = ref(CV);
const gc = ref(GC);
const notfound = ref(NotFound);
const now = ref(HPC);

const articles = ref(["高性能计算","图计算系统","深度学习","计算机视觉","绿色计算"]);
onMounted(() => {
  let script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js';
  document.body.appendChild(script);
})

</script>

<template>
    <el-tabs tab-position="left" type="border-card">
    <el-tab-pane v-for="article in articles">
      <template #label>
        <span class="custom-tabs-label">
          <!-- <el-icon><calendar /></el-icon> -->
          <span style="margin:50px;">{{article}}</span>
        </span>
      </template>
      <div class="articles" v-if="article=='高性能计算'">
      <hpc/>
      </div>
      <div class="articles" v-else-if="article=='图计算系统'">
      <gcs/>
      </div>
      <div class="articles" v-else-if="article=='深度学习'">
      <DL/>
      </div>
      <div class="articles" v-else-if="article=='计算机视觉'">
      <cv/>
      </div>
      <div class="articles" v-else="article=='绿色计算'">
      <gc/>
      </div>
    </el-tab-pane>
  </el-tabs>
</template>
<style>
.articles{
  padding:30px;
}
</style>