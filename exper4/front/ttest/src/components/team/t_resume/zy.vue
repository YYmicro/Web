<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

var t_messages = {
        "name" : "朱宇",
        "imageurl" : "team/teacher/zhuyu.jpg",
        "qhu_title" : "讲师",
        "edu_title" : "青海师范大学(博士)",
        "email" : "sdcxzhuyu@163.com",
        "main_studying_direction" : "机器学习、数据挖掘、网络表示学习",
        "related_research_situation" : [
            {"name" : "国家自然科学基金“基于超边建模的异质超网络表示学习研究”(No. 62166032),2022.01 ~ 2025.12,", "position" : "项目负责人"},
            {"name" : "青海省自然科学基金“富超边的异质超网络表示学习关键技术研究”(No.2022-ZJ-961Q),2022.01~2024.12,", "position" : "项目负责人"},
           ],
        "papers" : ["<b>Yu Zhu</b>, et al. Hypernetwork representation learning with the set constraint. Applied Sciences, 2022, 12(5): 2650. (SCI)",
                    "<b>Yu Zhu</b>, et al. Text-enhanced network representation learning. Frontiers of Computer Science, 2020, 14(6): 146322(CCF C类期刊, SCI)",
                    "<b>Yu Zhu</b>, et al. Network representation learning based on community and text features. Lecture Notes in Computer Science, 2018, 11221: 348-360 (EI)",
                    "<b>Yu Zhu</b>, et al. Hypernetwork representation learning with the transformation strategy. The 6th International Conference on High Performance Compilation, Computing and Communications, 2022, 131-136. (EI，第一作者)",
                    "刘贞国，<b>朱宇</b>,等.基于转换策略的异质超网络表示学习.计算机 应用研究，2022，39(11).（中文核心，CSCD，通讯作者）",
                ]
        
    }

t_messages.imageurl = require("../../../assets/" + t_messages.imageurl)

const activeName = ref("first")
const handleSelect = () => {

}
onMounted(() => {

})
const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event)
}

const previewPDF = () => {
   let url = `https://github.com/Xiamu-ssr/Web/blob/main/exper4/front/ttest/src/components/team/t_resume/Letter.pdf`;
   window.open(url, "_blank");
};
</script>

<template>
<br/>
<el-row>
    <el-col :span="4"></el-col>
    <el-col :span="16">
        <el-card>
            <!-- 上半部分 -->
            <el-row>
                <el-col :span="2"></el-col>
                <!-- 左边为基础信息 -->
                <el-col :span="6">
                    <el-avatar :size="168" :src="t_messages.imageurl" fit="fill" class="el_image" />
                    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
                        <el-tab-pane class="el_name" label="姓名" name="first">{{t_messages.name}}({{t_messages.qhu_title}})</el-tab-pane>
                        <el-tab-pane class="el_edu_title" label="学历" name="sceond">{{t_messages.edu_title}}</el-tab-pane>
                        <el-tab-pane class="el_email" label="联系方式" name="third">{{t_messages.email}}</el-tab-pane>
                    </el-tabs>

                </el-col>
                <el-col :span="2"></el-col>
                <!-- 右边为个人简历等 -->
                <el-col :span="12">
                    <el-tabs type="card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>主要研究方向</span>
                            </span>
                        </template>
                        <p>{{t_messages.main_studying_direction}}</p>
                        </el-tab-pane>
                    </el-tabs>
                    <br/>
                </el-col>
                <el-col :span="2"></el-col>
            </el-row>
            <!-- 下半部分 -->
            <br/>
            <el-row>
                <el-col :span="2"></el-col>
                <el-col :span="20">
                    <!-- 主持、参与科研情况 -->
                    <el-tabs type="border-card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>主持/参与科研情况</span>
                            </span>
                        </template>
                        <p v-for="(rrs,index) in t_messages.related_research_situation" :key="rrs" style="margin: 5px;">
                            [{{index+1}}]{{rrs.name}}<b>{{rrs.position}}</b>
                        </p>
                        <!-- <el-card v-for="(rrs,index) in t_messages.related_research_situation" :key="rrs" style="margin: 5px;">
                            [{{index}}]{{rrs.name}}<b>{{rrs.position}}</b>
                        </el-card> -->
                        </el-tab-pane>
                    </el-tabs>
                    <br/>
                    <!-- 学术论文发表 -->
                    <el-tabs type="border-card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>学术论文发表(近五年)</span>
                            </span>
                        </template>
                        
                        <span v-for="(c,index) in t_messages.papers" :key="c">[{{index+1}}]<p style="display: inline;" v-html="c"></p><br/><br/></span>
                        
                        
                        </el-tab-pane>
                    </el-tabs>
                    <br/>
                </el-col>
                <el-col :span="2"></el-col>
            </el-row>
        </el-card>
    </el-col>
    <el-col :span="4"></el-col>
</el-row>
</template>

<style scoped>
.el_image{
    height: 210px;
    width: 170px;
}
.el_name{
    font-weight: bold;
    font-size: 18px;
}
.el_edu_title{
    font-weight:lighter;
    font-size: 16px;
}
.el_title{
    font-weight:lighter;
    font-size: 16px;
}
.el_main_studying{
    font-weight:lighter;
    font-size: 16px;
}
.el_email{
    font-style:italic;
    font-weight: bold;
    font-size: 14px;
}
</style>

