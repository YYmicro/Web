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
                    <el-card v-for="m in message" @click="changemd(m.id)">
                        <el-icon :size="60"><InfoFilled /></el-icon><br/>
                        {{ m.title }}
                        <br/>
                        <el-button :style="deletestatus" @click="deletemd(m.id)" type="danger">X</el-button>
                    </el-card>
                    <!-- </a> -->
                    <el-card>
                        <el-icon :size="60"><Plus /></el-icon><br/>
                        <a href="#/markdown/addnewmd"><el-button type="primary">添加新文档</el-button></a>
                    </el-card>
                    <el-card >
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

</style>