<template>
  <div class="common-layout">
  <!-- <div> -->
    <el-container>
      <el-header>Header</el-header>
      <el-main>
        <el-row>
          <el-col :span="3" style="background-color: aqua;">00<div class="grid-content ep-bg-purple" /></el-col>
          <el-col :span="18" style="background-color:brown">Main<div class="grid-content ep-bg-purple-light" /></el-col>
          <el-col :span="3" style="background-color: aquamarine;">22<div class="grid-content ep-bg-purple" /></el-col>
        </el-row>
      </el-main>
      <el-footer>Footer

      </el-footer>
    </el-container>
  </div>
</template>

<!-- <script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'App',
});
</script> -->

<style>
body{
  margin:0px;
  padding:0px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 0px; */
  /* padding: 0px !important; */
}
.common-layout{
  margin:0px;
  padding:0px !important;
}
.el-header{
background-color: #000000;
/* display: flex;
justify-content: space-between;
padding-left: 0;
align-items: center;
color: rgba(8, 245, 4, 0.38);
font-size: 20px; */

}
.el-main{
  --el-main-padding:0px !important;
}

</style>

