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
            {'title' : '祝贺：本组硕士生张琨同学论文被计算机工程(中文核心)录用',
            'link' : ''},
            {'title' : '祝贺：本组硕士生黄东强同学论文被郑州大学学报工学版(中文核心)录用',
            'link' : ''},
            {'title' : '祝贺：本组硕士生张琨同学论文被小型微型计算机系统(中文核心)录用',
            'link' : ''},
        ],
    },
    {   'year' : 2021,
        'content' : [
            {'title' : '祝贺：本组硕士生赵梦梦同学论文被sci期刊Energies录用',
            'link' : ''},
            {'title' : '祝贺：本组硕士生边浩东同学论文被sci期刊Future Generation Computer Systems录用',
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

