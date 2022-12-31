<script lang="ts" setup>
import { ref, reactive, nextTick } from "vue";
import axios from 'axios';
import { Minus, Refresh } from "@element-plus/icons-vue";

import Display from "./components/markdown/display.vue"
const display = ref(Display)
// axios.defaults.withCredentials = true;

const message = ref("")
const deletestatus = ref("display:none;")
const displayid = ref("0");
const refresh = ref(true);

axios({
        data: {},
        method: "post",
        url: "http://127.0.0.1:5000",
    }).then((rsp) => {
        message.value = rsp.data;
        // console.log(rsp);
        // console.log(message.value);
});

function deleteable() {
    if(deletestatus.value == ""){
        deletestatus.value = "display:none;"
    }else{
       deletestatus.value = "" 
    }
    
};

function deletemd(id) {
    console.log(id)
    axios({
        data: {"id" : id},
        method: "post",
        url: "http://127.0.0.1:5000/delete",
    }).then((rsp) => {
        // message.value = rsp.data;
        // console.log(rsp);
        // console.log(message.value);
    });
    window.location.reload();
};

function changemd(id) {
    refresh.value = false;
    nextTick(()=>{
        refresh.value = true;
    })
    console.log("change md for id %d",id)
    displayid.value = id;
}
</script>

<template>
<el-row>
    <el-col :span="3"></el-col>
    <el-col :span="18">
        <el-tabs type="border-card">
            <el-tab-pane label="帮助文档">
                <el-space wrap size="large">
                    <!-- <a href="#/markdown/display"> -->
                    <el-card v-for="m in message" @click="changemd(m.id)" class="card-hover">
                        <el-icon :size="60"><InfoFilled /></el-icon><br/>
                        {{ m.title }}
                        <br/>
                        <el-button :style="deletestatus" @click="deletemd(m.id)" type="danger">X</el-button>
                    </el-card>
                    <!-- </a> -->
                    <el-card class="card-hover">
                        <el-icon :size="60"><Plus /></el-icon><br/>
                        <a href="#/markdown/addnewmd"><el-button type="primary">添加新文档</el-button></a>
                    </el-card>
                    <el-card class="card-hover">
                        <el-icon :size="60"><Minus /></el-icon><br/>
                        <el-button @click="deleteable" type="warning">删除文档</el-button>
                    </el-card>
                </el-space>
            </el-tab-pane>
        </el-tabs>
        <br/><br/>
        <display :id="displayid" v-if="refresh" />
    </el-col>
    <el-col :span="3"></el-col>
</el-row>
</template>
  
<style scoped>
@keyframes example {
  0%   {transform: scale(1,1);}
  25%  {transform: scale(1.01,1.01);box-shadow: 0 0 2px 1px #0d6efd33;}
  50%  {transform: scale(1.02,1.02);box-shadow: 0 0 4px 2px #0d6efd66;}
  100% {transform: scale(1.03,1.03);box-shadow: 0 0 6px 3px #0d6efd99;}
}
.card-hover:hover{
    /* transition: transform 0.6s; */
    /* transform: scale(0.95,0.95); */
    animation-name: example;
    animation-duration: 0.3s;
    /* animation-iteration-count: 1; */
    animation-fill-mode: both;
}
</style>