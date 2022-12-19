<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
// import axios from "axios";
// import { keyBy } from "lodash-es";
// axios.defaults.withCredentials = true;
// import MyMenu from './components/Index/menu.vue'
// const mymenu = ref(MyMenu)
import MyNews from './components/Index/RecentNews.vue'
const mynews = ref(MyNews)
import MyPapers from './components/Index/Papers.vue'
const mypapers = ref(MyPapers)
import ResearchDirect from './components/Index/ResearchDirect.vue'
const researchdirect = ref(ResearchDirect)

const Carousel_img_fit = 'scale-down'

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
<div class="common-layout">
  <el-container>
    <!-- 幻灯片 -->
    <el-main>
      <!-- yymicro index -->
      <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
        <ol class="carousel-indicators">
          <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"></li>
          <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"></li>
          <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="card mb-3 w-100">
              <div class="row g-0">
                <div class="col-md-2 bg-light"></div>
                <div class="col-md-5">
                  <img src="./assets/Index/1.png" class="d-block w-100" alt="...">
                </div>
                <div class="col-md-3">
                  <div class="card-body">
                    <h5 class="card-title"><b>实验室介绍</b></h5>
                    <hr/>
                    <p class="card-text">&nbsp;&nbsp;&nbsp;&nbsp;青海大学高性能与云计算研究所HDACP实验室(High-performance computing and Distributed systems, Computer vision and Pattern recognition)成立于2020年， 是青海大学高性能与云计算研究所开展国内外广泛交流的高性能计算与分布式系统以及计算机视觉研究的科研小组。 HDACP实验室的目标是：依托研究所，建立起具有国内外知名水平的研究组。</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                  </div>
                </div>
                <div class="col-md-2 bg-light"></div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="card mb-3 w-100">
              <div class="row g-0">
                <div class="col-md-2 bg-light"></div>
                <div class="col-md-5">
                  <img src="./assets/Index/2.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="col-md-3">
                  <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                  </div>
                </div>
                <div class="col-md-2 bg-light"></div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="card mb-3 w-100">
              <div class="row g-0">
                <div class="col-md-2 bg-light"></div>
                <div class="col-md-5">
                  <img src="./assets/Index/3.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="col-md-3">
                  <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                  </div>
                </div>
                <div class="col-md-2 bg-light"></div>
              </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </a>
      </div>
      <br/><br/><br/><br/>
      <el-row>
        <el-col :span="1"></el-col>
        <el-col :span="6">
          <mynews />
        </el-col>
        <el-col :span="10">
          <mypapers />
        </el-col>
        <el-col :span="6">
          <researchdirect />
        </el-col>
        <el-col :span="1"></el-col>
      </el-row>
    </el-main>
    <!-- <br/><br/><br/><br/> -->
    <!-- <el-footer>
      <el-row style="background-color: rgba(0, 0, 0,0.22); color:black; padding-top: 50px;">
        <el-col :span="1"></el-col>
        <el-col :span="6">
          <el-row>
            <el-col :span="18">
              <el-image class="image-hover" :src='require("./assets/Index/fig0.png")' />
            </el-col>
            <el-col :span="6"></el-col>
          </el-row>
        </el-col>
        <el-col :span="1"></el-col>
        <el-col :span="8">
          <h5>扫描下方二维码关注青海大学计算机系公众号</h5>
          <el-row>
            <el-col :span="6">
              <el-image :src='require("./assets/Index/qrcode.jpg")' />
            </el-col>
            <el-col :span="18"></el-col>
          </el-row>
          
        </el-col>
        <el-col :span="1"></el-col>
        <el-col :span="6">
          <h5>地址</h5>
          <el-link>青海省西宁市宁大路251号</el-link><br/>
          <el-link>青海大学计算机技术与应用系111实验室</el-link><br/>
          <el-divider/>
          <h5>常用链接</h5>
          <el-link href="https://www.qhu.edu.cn/">青海大学</el-link><br/>
          <el-link href="https://cs.qhu.edu.cn/">青海大学计算机技术与应用系</el-link><br/>
          <el-link href="https://www.ccf.org.cn/">中国计算机学会</el-link><br/>
          
        </el-col>
        <el-col :span="1"></el-col>
      </el-row>
    </el-footer> -->
  </el-container>
</div>
</template>


<style scoped>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
.el_image{
  width: 400px;
  height: 350px;
}
.el-header{
  padding:0px !important;
}
.el-main{
  padding:0px !important;
}
@keyframes example {
  0%    {}
  10%   {transform: rotateX(120deg) scale(1.05,1.05);}
  20%   {transform: rotateX(120deg) scale(1.10,1.10);}
  30%   {transform: rotateX(120deg) rotateY(120deg)  scale(1.15,1.15);}
  40%   {transform: rotateY(120deg) scale(1.20,1.20);}
  50%   {transform: rotateY(120deg) rotateZ(120deg) scale(1.25,1.25);}
  60%   {transform: rotateZ(120deg) scale(1.30,1.30);}
  70%   {transform: rotateZ(120deg) scale(1.35,1.35);}
  80%   {transform: scale(1.40,1.40);}
  90%   {transform: scale(1.25,1.25);}
  100%  {transform: scale(1,1);}
}
.image-hover{
  
}
.image-hover:hover{
  /* transition: transform 0.6s; */
    /* transform: scale(0.95,0.95); */
    animation-name: example;
    animation-duration: 3s;
    /* animation-iteration-count: 1; */
    animation-fill-mode: both;
}
</style>
