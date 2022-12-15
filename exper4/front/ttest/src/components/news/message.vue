<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event)
}
// console.log(props.defA)

const allmessages = ref([
    {   'year' : 2022,
        'content' : [
            {'title' : '第二十四届IEEE International Conference on High Performance Computing and Communications (HPCC-2022)正在征文',
            'link' : ''},
            {'title' : '恭喜：我组黄建强老师论文 Large-Scale Graph Triangle-Counting on a single Machine using GPUs被TPDS(CCF A, 国际顶级期刊)收录',
            'link' : ''},
            {'title' : '第十四届中国计算机图形学大会在我校顺利召开',
            'link' : ''},
        ],
    },
    {   'year' : 2021,
        'content' : [
            {'title' : '恭喜：我校超算团队在ASC世界大学生超级计算机竞赛中获得一等奖',
            'link' : ''},
        ],
    },
])

const handleSelect = () => {

}
onMounted(() => {

})
</script>
<template>
<el-tabs type="border-card">
    <el-tab-pane v-for="messages in allmessages" :key="messages" v-bind="messages" :label="messages.year">
        <el-card class="box-card card-space" v-for="content in messages.content" :key="content" v-bind="content">
            <div class="text item">
                <el-icon :size="24" color=#0d6efd><Finished /></el-icon>&nbsp;
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

