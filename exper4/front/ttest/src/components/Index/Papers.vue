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
      <div class="card-body mybg">
          <h5 class="card-title"><b>学术氛围</b></h5>
          <p class="card-text">我们的实验室拥有十分浓厚的学术氛围，大家可以对研究过程中出现的任何问题做自由讨论。 并且我们会按时进行一周一次的组会讨论，对你遇到的各种学术问题予以解决，以帮助你更快的成长。 我们还会定期参加大型的学术交流会，例如全国高性能计算学术年会、CNCC中国计算机大会等， 让你能够充分的接触到相关研究方向的国内外学术大咖。与此同时，我们还会全力支持对于成功发表论文的同学外出做学术交流。</p>
          <a href="#" class="btn btn-primary">看看团队日常记录</a>
      </div>
  </div>
  <div class="card w-100 p-2" style="border: none;">
    <img src="../../assets/Index/2.jpg" class="card-img-top w-100">
    <div class="card-body  mybg">
        <h5 class="card-title"><b>最新论文</b></h5>
        <el-card class="news_card" shadow="hover" v-for="papers_title in papers_titles" :key="papers_title">{{papers_title}}</el-card>
    </div>
    </div>
</template>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
.mybg{
    background-color: rgba(0, 0, 0, 0.15);
}
</style>

