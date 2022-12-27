<script lang="ts" setup>
import { ref, reactive } from "vue";
import axios from "axios";
axios.defaults.withCredentials = true;
import { useCookies } from "vue3-cookies";
const { cookies } = useCookies();
import { MyStore } from "./store/store";

const c = ref("");
let store = new MyStore();
function sendData() {
  store.addCount();
  console.log(store.getCount());
  c.value = store.getCount();
  // axios({
  //   data: {},
  //   method: "post",
  //   url: "http://127.0.0.1:5000",
  // }).then((rsp) => {
  //   rrr.user = rsp.data;
  //   // console.log(rrr.user);
  // });
}
</script>

<template>
  <el-container>
    <el-header></el-header>
    <el-main>
      <el-row>
        <el-col :span="8"></el-col>
        <el-col :span="8">
          <h2>你是第{{ c }}个访客</h2>
          <el-button @click="sendData"></el-button>
          <!-- <el-select v-model="sex" placeholder="your sex">
            <el-option value="男" label="男" />
            <el-option value="女" label="女" />
          </el-select> -->
        </el-col>
        <el-col :span="8"></el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<style></style>
