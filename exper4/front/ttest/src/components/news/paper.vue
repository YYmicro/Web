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
        <el-card class="box-card card-space" v-for="content in messages.content" :key="content" v-bind="content">
            <div class="text item">
                <el-icon :size="24" color=#ffc107><Trophy /></el-icon>&nbsp;
                <el-link v-if="content.link != ''" :href="content.link"><p class="card-font">{{content.title}}</p></el-link>
                <el-link v-else href="#/news"><p class="card-font">{{content.title}}</p></el-link>
            </div>
        </el-card>
    </el-tab-pane>
</el-tabs>
</template>


<style>
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
</style>

