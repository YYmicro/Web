<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";

const props = defineProps([]);
// console.log(props.defA)


const papers_titles = ['祝贺：本组硕士生张琨同学论文被计算机工程(中文核心)录用',
                      '祝贺：本组硕士生黄东强同学论文被郑州大学学报工学版(中文核心)录用',
                      '祝贺：本组硕士生张琨同学论文被小型微型计算机系统(中文核心)录用',
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
    <el-image :src='require("../../assets/Index/t1.jpg")' class="card-img-top w-100"/>
    <div class="card-body mybg">
        <h5 class="card-title" style="display: inline; color: #0d6efd;"><span style="font-weight: lighter;">最新论文</span></h5>&nbsp;<el-link href="#/news" type="info">更多></el-link>
        <el-divider />
        <el-card class="news_card card-hover" style="margin: 10px;" shadow="hover" v-for="papers_title in papers_titles" :key="papers_title"><el-icon :size="20" color=#ffe69c><Opportunity /></el-icon>&nbsp;{{papers_title}}</el-card>
    </div>
    </div>
    
</template>

<style scoped>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";

.mybg{
    background-color: rgba(0, 0, 0, 0.07);
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

