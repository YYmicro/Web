<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event)
}
// console.log(props.defA)

const allmessages = require("../../json/news/2.json")

const handleSelect = () => {

}
onMounted(() => {

})
</script>
<template>
<el-tabs tab-position="left" type="border-card">
    <el-tab-pane v-for="messages in allmessages" :key="messages" v-bind="messages" :label="messages.year">
        <el-card class="box-card card-space card-hover" v-for="content in messages.content" :key="content" v-bind="content">
            <div class="text item">
                <el-icon :size="24" color=#ffc107><Trophy /></el-icon>&nbsp;
                <el-link v-if="content.link != ''" :href="content.link"><p class="card-font">{{content.title}}</p></el-link>
                <el-link v-else href="#/news"><p class="card-font">{{content.title}}</p></el-link>
            </div>
        </el-card>
    </el-tab-pane>
</el-tabs>
</template>


<style scoped>
.card-space{
    padding: 0px;
    margin: 6px;
}
.card-font{
    font-size: 16px;
    font-weight: bold;
    margin: 0px;
    padding: 0px;
}
@keyframes example {
  0%   {transform: scale(1,1);}
  25%  {transform: scale(1.008,1.008);box-shadow: 0 0 2px 1px #0d6efd33;}
  50%  {transform: scale(1.016,1.016);box-shadow: 0 0 4px 2px #0d6efd66;}
  100% {transform: scale(1.02,1.02);box-shadow: 0 0 6px 3px #0d6efd99;}
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

