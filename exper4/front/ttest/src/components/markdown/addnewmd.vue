<script lang="ts" setup>
import { ref, reactive } from "vue";
import axios from 'axios';
import { Minus } from "@element-plus/icons-vue";

const title = ref("")
const text = ref("")
const visible = ref(false)
const tips = ref("提交成功")

function sendData() {
    axios({
        data: {'title' : title.value, 'text' : text.value},
        method: "post",
        url: "http://127.0.0.1:5000/addnew",
    }).then((rsp) => {
        const r = rsp.data;
        console.log(r);
        if(r=='1'){
            visible.value = true;
        }else{
            visible.value = true;
            tips.value = "提交失败，请联系管理员"
        }
        // window.setTimeout(window.location.href="#/markdown", 3000)
        // console.log(message.value);
    });
}

</script>

<template>
<br/><br/>
<el-row>
    <el-col :span="3"></el-col>
    <el-col :span="18">
        <el-card type="border-card">
            标题 : <el-input v-model="title" placeholder="Please input" /><br/>
            内容 :
            <v-md-editor v-model="text" height="400px"></v-md-editor>
            <br/><br/>
            <el-button @click="sendData()" type="primary">提交</el-button>
        </el-card>
    </el-col>
    <el-col :span="3"></el-col>
</el-row>
<el-dialog v-model="visible" :show-close="false">
    <template #header="{ close, titleId, titleClass }">
    <div class="my-header">
        <h4 :id="titleId" :class="titleClass">{{ tips }}</h4>
        <a href="#/markdown">
            <el-button type="danger" @click="close">    
                <el-icon class="el-icon--left"><CircleCloseFilled /></el-icon>
                Close
            </el-button>
        </a>
    </div>
    </template>
    This is dialog content.
</el-dialog>
</template>
  
<style scoped>

</style>