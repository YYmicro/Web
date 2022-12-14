<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";

onMounted(() => {
  let script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js';
  document.body.appendChild(script);
})
</script>
<template>
    <div class="common-layout">
      <el-container>
        <el-main>
            main
        </el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </div>
</template>