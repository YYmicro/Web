<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

var t_messages = {
        "name" : "边浩东",
        "imageurl" : "team/teacher/bhd.jpg",
        "qhu_title" : "助教",
        "edu_title" : "青海大学（硕士）",
        "email" : "hpc_bhd@163.com",
        "main_studying_direction" : "体系结构与高性能计算（并行计算、异构计算）、系统软件（图计算系统、性能分析及自动调优工具）。并行计算和异构计算的研究内容有基础研究（数值算法（矩阵运算（目前主攻）、多项式与线性代数方程组、快速傅里叶变换等）、非数值算法（以图算法为主））、应用程序优化（目前主要以服务器端为主（数值天气预报系统Grapes、量子计算模拟器等）、移动端（主要面向商业场景，例如计算机视觉模型、小型深度学习模型等基于移动端平台的性能优化））、高性能算子库与求解器研发（包括但不仅限于以上内容）。",
        "individual_resume" : ["曾就职于北京旷视科技有限公司（MEGVII），担任资深研发工程师，主要从事高性能计算优化等相关工作。目前以第一作者在SPE、FGCS、CCGRID、ICA3PP等国际重要期刊会议上发表文章",
                           ],
        "awards" : "本人对各种编程类学科竞赛具有狂热的兴趣，包括高性能计算领域（ASC、PAC、CPC、IPCC、PRA）、算法竞赛（ICPC、CCPC、CSP、蓝桥杯等）、数学建模竞赛（全国研究生数学建模竞赛）等。欢迎感兴趣的同学与我联系。",
        "papers" : ["<b>H. Bian</b>, J. Huang, J. Tang, R. Dong, L. Wu, X. Wang, \"PAS: A new powerful and simple quantum computing simulator\", Softw Pract Exper. 2021; 1-18. (CCF B / THU B)  (中科院SCI三区 / JCR二区 / IF=3.200)",
                    "<b>H. Bian</b>, J. Huang, L. Liu, D. Huang, X. Wang, “ALBUS: A method for efficiently processing SpMV using SIMD and Load balancing”, Future Generation Computer Systems, Volume 116, 2021, pp. 371-392. (CCF C / THU B)  (中科院SCI一区 / Top期刊 / IF=7.307)",
                    "<b>H. Bian</b>, J. Huang, R. Dong, Y. Guo, L. Liu, D. Huang and X. Wang, \"A simple and efficient storage format for SIMD-accelerated SpMV\", Cluster Comput 24, 3431-3448 (2021). (THU B)  (中科院SCI三区 / JCR二区 / IF=2.303)",
                    "<b>H. Bian</b>, J. Huang, R. Dong, L. Liu and X. Wang, \"CSR2: A New Format for SIMD-accelerated SpMV\", 2020 20th IEEE/ACM International Symposium on Cluster, Cloud and Internet Computing (CCGRID), Melbourne, Australia, 2020, pp. 350-359. (CCF C / THU B)",
                    "<b>H. Bian</b>, J. Huang, R. Dong, Y. Guo, X. Wang, \"HpQC: A New Efficient Quantum Computing Simulator\", In: Qiu M. (eds) Algorithms and Architectures for Parallel Processing. ICA3PP 2020. Lecture Notes in Computer Science, vol 12453. Springer, Cham. (CCF C)",
                    "郭渝洛,<b>边浩东</b>,董润婷,唐嘉豪,王晓英,黄建强. 基于SIMD高效并行傅里叶空间图像相似度计算研究[J/OL].计算机工程:1-7[2020-11-23].(CCF C类中文期刊、CSCD)",
                    ],
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
                    </el-tabs>
                    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
                        <el-tab-pane class="el_edu_title" label="学历" name="first">{{t_messages.edu_title}}</el-tab-pane>
                    </el-tabs>
                    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
                        <el-tab-pane class="el_email" label="联系方式" name="first">{{t_messages.email}}</el-tab-pane>
                    </el-tabs>
                    <br/>
                </el-col>
                <el-col :span="2"></el-col>
                <!-- 右边为个人简历等 -->
                <el-col :span="12">
                    <el-tabs type="card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>个人简介</span>
                            </span>
                        </template>
                        <p v-for="i_resume in t_messages.individual_resume" :key="i_resume" style="text-indent: 2em;">{{i_resume}}</p>
                        </el-tab-pane>
                    </el-tabs>
                    <br/>
                    <el-tabs type="card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>主要研究方向</span>
                            </span>
                        </template>
                        <p style="text-indent: 2em;">{{t_messages.main_studying_direction}}</p>
                        </el-tab-pane>
                    </el-tabs>
                    <br/>
                    <el-tabs type="card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>获奖情况</span>
                            </span>
                        </template>
                        <p style="text-indent: 2em;">{{t_messages.awards}}</p>
                        </el-tab-pane>
                    </el-tabs>
                </el-col>
                <el-col :span="2"></el-col>
            </el-row>
            <!-- 下半部分 -->
            <br/>
            <el-row>
                <el-col :span="2"></el-col>
                <el-col :span="20">
                    <!-- 主持、参与科研情况 -->
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

