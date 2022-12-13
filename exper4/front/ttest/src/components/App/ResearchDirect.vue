<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";

const props = defineProps([]);
// console.log(props.defA)

const searchs = [{title:'高性能计算',img:require('../../assets/App/s1.jpg')},
                {title:'图计算系统',img:require('../../assets/App/s2.jpg')},
                {title:'深度学习',img:require('../../assets/App/s3.jpg')},
]

const handleSelect = () => {

}
onMounted(() => {
  let script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js';
  document.body.appendChild(script);
})
</script>

<template>
    <div class="card w-100 p-2" style="border: none;">
        <img src="../../assets/App/3.jpg" class="card-img-top w-100">
        <div class="card-body  mybg">
            <h5 class="card-title"><b>最新论文</b></h5>
            <el-card class="news_card" shadow="hover" v-for="search in searchs" :key="search">
                <el-row>
                    <el-col :span="8">
                        <el-image fit="cover" :src="search.img"/>
                    </el-col>
                    <el-col :span="4"></el-col>
                    <el-col :span="12" class="ver_mid">{{search.title}}</el-col>
                </el-row>
            </el-card>
        </div>
    </div>
</template>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
.mybg{
    background-color: rgba(0, 0, 0, 0.15);
}
.ver_mid{
    display:flex;
    justify-content:center;/*主轴上居中*/
    align-items:center;/*侧轴上居中*/
}
</style>

