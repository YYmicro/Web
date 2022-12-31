<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";

const props = defineProps([]);
// console.log(props.defA)

const searchs = [{title:'高性能计算',img:require('../../assets/Index/s1.jpg')},
                {title:'图计算系统',img:require('../../assets/Index/s2.jpg')},
                {title:'深度学习',img:require('../../assets/Index/s3.jpg')},
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
        <img src="../../assets/Index/t2.jpg" class="card-img-top w-100">
        <div class="card-body  mybg">
            <h5 class="card-title" style="display: inline; color: #0d6efd;"><span style="font-weight: lighter;">研究方向</span></h5>&nbsp;<el-link href="#/researchintro" type="info">更多></el-link>
            <el-divider />
            <el-card class="news_card card-hover" style="margin: 10px;" shadow="hover" v-for="search in searchs" :key="search">
                <el-row>
                    <el-col :span="4">
                        <el-image fit="cover" :src="search.img"/>
                    </el-col>
                    <el-col :span="6"></el-col>
                    <el-col :span="14" class="ver_mid">{{search.title}}</el-col>
                </el-row>
            </el-card>
        </div>
    </div>
</template>

<style scoped>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
.mybg{
    background-color: rgba(0, 0, 0, 0.07);
}
.ver_mid{
    display:flex;
    justify-content:center;/*主轴上居中*/
    align-items:center;/*侧轴上居中*/
}
@keyframes example {
  0%   {transform: scale(1,1);}
  25%  {transform: scale(1.02,1.02);box-shadow: 0 0 2px 1px #0d6efd33;}
  50%  {transform: scale(1.04,1.04);box-shadow: 0 0 4px 2px #0d6efd66;}
  100% {transform: scale(1.06,1.06);box-shadow: 0 0 6px 3px #0d6efd99;}
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

