<script lang="ts" setup>
import { ref, reactive } from "vue";
import axios from 'axios';
import { tr } from "element-plus/es/locale";

const props = defineProps(['id']);
const id = ref(props.id);
const fixvisble = ref("display:none");
console.log("id = ")
console.log(id.value)
const text = ref("if display this explains that rsp from tail has some problem")
if(id.value=="0"){
    text.value = "# 欢迎使用帮助文档"
    fixvisble.value = "display:none";
}else{
    axios({
        data: {'id' : id.value},
        method: "post",
        url: "http://127.0.0.1:5000/select_one",
    }).then((rsp) => {
        text.value = rsp.data;
        // console.log(rsp);
        // console.log(message.value);
    });
    fixvisble.value = "";
};

const fixmdvisble = ref("display:none");
function fix(){
    if(fixmdvisble.value == ""){
        fixmdvisble.value = "display:none";
    }else{
        fixmdvisble.value = "";
    }
    
}

function fixover(){
    axios({
        data: {'id' : id.value, 'text' : text.value},
        method: "post",
        url: "http://127.0.0.1:5000/fixone",
    }).then((rsp) => {
        text.value = rsp.data;
        // console.log(rsp);
        // console.log(message.value);
    });
    window.location.reload();
}

</script>

<template>
<br/><br/>
<el-row>
    <!-- <el-col :span="3"></el-col> -->
    <el-col :span="24">
        <el-card type="border-card">
            <v-md-preview :text="text"></v-md-preview>
        </el-card>
    </el-col>
    <el-button type="danger" @click="fix" :style="fixvisble">在线修改</el-button><br/>
    <!-- <el-col :span="3"></el-col> -->
</el-row>
<el-row :style="fixmdvisble">
    <v-md-editor v-model="text" height="400px"></v-md-editor>
    <el-button type="primary" @click="fixover" :style="fixvisble">提交</el-button><br/>
</el-row>
</template>
  
<style scoped>

</style>