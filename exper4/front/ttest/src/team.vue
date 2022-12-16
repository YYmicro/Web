<script lang="ts" setup>

import { onErrorCaptured, ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

import Teacher from './components/team/teacher.vue'
import Master from './components/team/master.vue'
const teacher = ref(Teacher)
const master = ref(Master)

const activeName = ref('first')

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event)
}
// console.log(props.defA)

const handleSelect = () => {

}

onErrorCaptured(err => {
  console.log('Caught error', err.message)
  window.location.reload();
  return false
})
onMounted(() => {
})
</script>

<template>
<br/><br/>
<el-row>
    <el-col :span="3"></el-col>
    <el-col :span="18">
        <el-tabs type="border-card" class="demo-tabs">
            <el-tab-pane>
            <template #label>
                <span class="custom-tabs-label">
                <el-icon :size="20"><calendar /></el-icon>
                <span class="tab-pane-team">&nbsp;师资队伍</span>
                </span>
            </template>
            <teacher />
            <!-- <KeepAlive> -->
                <!-- <teacher :is="activeComponent"/> -->
            <!-- </KeepAlive> -->
            </el-tab-pane>
            <el-tab-pane>
            <template #label>
                <span class="custom-tabs-label">
                <el-icon :size="20"><calendar /></el-icon>
                <span class="tab-pane-team">&nbsp;硕士研究生</span>
                </span>
            </template>
            <master />
            </el-tab-pane>
            <el-tab-pane>
            <template #label>
                <span class="custom-tabs-label">
                <el-icon :size="20"><calendar /></el-icon>
                <span class="tab-pane-team">&nbsp;毕业学生</span>
                </span>
            </template>
            Route
            </el-tab-pane>
        </el-tabs>
    </el-col>
    <el-col :span="3"></el-col>
</el-row>
</template>


<style>
.tab-pane-team{
    /* margin: 10px; */
    font-size: 22px;
}
</style>

