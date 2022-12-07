<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import axios from "axios";
axios.defaults.withCredentials = true;

import HelloWorld from './components/HelloWorld.vue'
const helloworld = ref(HelloWorld)
onMounted(() => {

})
</script>

<template>
  <el-container>
    <el-main>
      <el-row>
        <el-col :span="8"></el-col>
        <el-col :span="8">
          <HelloWorld ref="helloworld"/>
        </el-col>
        <el-col :span="8"></el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<style></style>
