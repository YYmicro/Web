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
    <div class="card w-100 p-2" style="border: none;">
        <img src="../../assets/Index/1.jpg" class="card-img-top w-100">
        <div class="card-body mybg">
            <h5 class="card-title"><b>最新动态</b></h5>
            <el-card class="news_card" shadow="hover" v-for="news_title in news_titles" :key="news_title">{{news_title}}</el-card>
        </div>
    </div>
</template>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";

.mybg{
    background-color: rgba(0, 0, 0, 0.15);
}

.news_card{
    font-weight: bold;
    color: rgb(0, 156, 189);
    margin: 2px;
}

</style>

