<script lang="ts" setup>
import { ref, reactive } from "vue";
import axios from 'axios';
axios.defaults.withCredentials = true;

const message = ref("")

function sendData() {
  axios({
    data: {},
    method: "post",
    url: "http://127.0.0.1:5000",
  }).then((rsp) => {
    message.value = rsp.data;
    console.log(message);
  });
}

</script>

<template>
<el-container>
    <el-row>
        <el-col :span="8"></el-col>
        <el-col :span="8">
            <el-button @click="sendData">click</el-button>
        </el-col>
        <el-col :span="8"></el-col>
    </el-row>
</el-container>
</template>
  
<style scoped>

</style>