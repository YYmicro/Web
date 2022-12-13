<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
// import axios from "axios";
// import { keyBy } from "lodash-es";
// axios.defaults.withCredentials = true;
import MyMenu from './components/menu.vue'
const mymenu = ref(MyMenu)
const Carousel_img_fit = 'scale-down'

const handleSelect = () => {

}
onMounted(() => {
  // let script = document.createElement('script');
  // script.type = 'text/javascript';
  // script.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js';
  // document.body.appendChild(script);
})
</script>


<template>
<div class="common-layout">
  <el-container>
    <el-header  justigy="space-evenly">
      <el-col :span="24">
        <mymenu defA="1"/>
      </el-col>
    </el-header>
    <el-main>
      <!-- <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
        <ol class="carousel-indicators">
          <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"></li>
          <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"></li>
          <li data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="./assets/App/1.jpg" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>First slide label</h5>
              <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="./assets/App/1.jpg" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>Second slide label</h5>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="./assets/App/1.jpg" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>Third slide label</h5>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
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
      </div> -->
    </el-main>
    <el-footer>Footer</el-footer>
  </el-container>
</div>
</template>


<style>
/* @import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"; */
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
</style>
