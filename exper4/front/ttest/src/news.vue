<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

import Message from './components/news/message.vue'
const message = ref(Message)
import Paper from './components/news/paper.vue'
const paper = ref(Paper)


const activeName = ref('first')

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event)
}
// console.log(props.defA)

const handleSelect = () => {

}
onMounted(() => {

})
</script>

<template>
<br/><br/>
<el-row>
    <el-col :span="3"></el-col>
    <el-col :span="18">
        <el-tabs
            v-model="activeName"
            type="card"
            class="demo-tabs"
            @tab-click="handleClick"
        >
            <el-tab-pane name="first">
                <template #label>
                    <span class="custom-tabs-label">
                        <el-icon :size="20"><ChatDotSquare /></el-icon>
                        <span class="tab-pane-news">&nbsp;动态</span>
                    </span>
                </template>
                <message />
            </el-tab-pane>
            <el-tab-pane name="second">
                <template #label>
                    <span class="custom-tabs-label">
                        <el-icon :size="20"><Tickets /></el-icon>
                        <span class="tab-pane-news">&nbsp;论文</span>
                    </span>
                </template>
                <paper />
            </el-tab-pane>
        </el-tabs>
    </el-col>
    <el-col :span="3"></el-col>
</el-row>
</template>


<style>
.tab-pane-news{
    /* margin: 10px; */
    font-size: 22px;
}
</style>

