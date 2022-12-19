<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";

const props = defineProps([]);
// console.log(props.defA)

const news_titles = ['祝贺: 实验室王晓英教授遴选为青海大学博士生导师',
                    '祝贺: 实验室黄建强教授遴选为青海大学博士生导师',
                    '祝贺: 实验室朱宇博士遴选为青海大学硕士生导师',
                    '第二十四届IEEE International Conference on High Performance Computing and Communications (HPCC-2022)正在征文',
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
  <div class="card w-100 p-2 card-hover" style="border: none;">
      <div class="card-body mybg">
        <h5 class="card-title" style="display: inline; color: #0d6efd;"><span style="font-weight: lighter;">学术氛围</span></h5>&nbsp;<el-link href="#/team" type="info">更多></el-link>
        <el-divider />

        <p class="card-text">我们的实验室拥有十分浓厚的学术氛围，大家可以对研究过程中出现的任何问题做自由讨论。 并且我们会按时进行一周一次的组会讨论，对你遇到的各种学术问题予以解决，以帮助你更快的成长。 我们还会定期参加大型的学术交流会，例如全国高性能计算学术年会、CNCC中国计算机大会等， 让你能够充分的接触到相关研究方向的国内外学术大咖。与此同时，我们还会全力支持对于成功发表论文的同学外出做学术交流。<br/><el-divider>期待你的加入！！!</el-divider></p>
      </div>
  </div>
  <div class="card w-100 p-2" style="border: none;">
        <!-- <img src="../../assets/Index/1.jpg" class="card-img-top w-100"> -->
        <div class="card-body mybg">
            <h5 class="card-title" style="display: inline; color: #0d6efd;"><span style="font-weight: lighter;">最新动态</span></h5>&nbsp;<el-link href="#/news" type="info">更多></el-link>
            <el-divider />
            <el-card class="news_card card-hover" style="margin: 10px;" shadow="hover" v-for="news_title in news_titles" :key="news_title"><el-icon :size="20" color=#ffc107><Trophy /></el-icon>&nbsp;{{news_title}}</el-card>
        </div>
    </div>
</template>

<style scoped>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
.mybg{
    background-color: rgba(0, 0, 0, 0.07);
}
.card-hover{

}

@keyframes example {
  0%   {transform: scale(0.98,0.98);}
  25%  {transform: scale(0.96,0.96);box-shadow: 0 0 2px 1px #0d6efd33;}
  50%  {transform: scale(0.94,0.94);box-shadow: 0 0 4px 2px #0d6efd66;}
  100% {transform: scale(0.92,0.92);box-shadow: 0 0 6px 3px #0d6efd99;}
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

