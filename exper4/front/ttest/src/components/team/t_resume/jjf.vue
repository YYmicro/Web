<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

var t_messages = {
        "name" : "贾金芳",
        "imageurl" : "team/teacher/jjf.jpg",
        "qhu_title" : "讲师",
        "edu_title" : "华东理工大学博士（在读)",
        "email" : "qhu_jf@163.com",
        "academic_title" : "中国计算机学会（CCF）会员",
        "academic_part_time_job" : "Journal of supercomputing审稿人（国际知名SCI期刊）",
        "main_studying_direction" : "高性能计算、并行算法优化、机器学习",
        "related_research_situation" : [
            {"name" : "教育部春晖计划科研基金项目“基于OpenCL异构并行算法的材料微观组织模拟研究”,", "position" : "主持"},
            {"name" : "青海大学中青年科研基金项目“MPI/CUDA并行技术在材料模拟计算中的应用”，", "position" : "主持"},
            {"name" : "“青海电网数值天气预报子系统部署与运维保障”，", "position" : "主持"},
            {"name" : "青海省科技计划项目“GRAPES数值天气预报模式动力框架大规模并行算法与优化技术研究”，", "position" : "第一参与"},
            {"name" : "国家自然科学基金项目“智能电网影响感知的数据中心需求响应策略与机制研究”，", "position" : "参与"},
            {"name" : "“基于多源卫星的天河工程数据集成平台”，", "position" : "参与"},
           ],
        "papers" : ["Ma, Chenyu, <b>Jia, Jinfang*</b>, Liu, Zhen, Huang, Jianqiang, Wang, Xiaoying. Simulation of three-dimensional phase field model with LBM method using OpenCL. The Journal of Supercomputing, 2022:1-19. https://doi.org/10.1007/s11227- 022-04321-w （CCF C, SCI期刊）",
                    "张琨,<b>贾金芳*</b>,黄建强,王晓英,严文昕. 预处理共轭梯度算法异构并行求解及优化.小型微型计算机系统,2021.https://kns.cnki.net/kcms/detail/ 21.1106.tp. 20210818.0900.006.html （CCF B, CSCD核心期刊）",
                    "张琨, <b>贾金芳*</b> ,严文昕,黄建强,王晓英. GRAPES动力框架中大规模稀疏线性系统并行求解及优化[J].计算机工程,2022,48(01):149-154+162.（CCF C, CSCD核心期刊）",
                    "Yan Wenxin; <b>Jinfang Jia*</b>; Huang Jianqiang; Xiaoying Wang; Research of GRAPES Numerical weather Prediction Model, In Proceedings of the 2020 4th High Performance Computing and Cluster Technologies Conference & 2020 3rd International Conference on Big Data and Artificial Intelligence (HPCCT & BDAI 2020),Qingdao China, 2020.",
                    "Yan Wenxin; <b>Jinfang Jia*</b>; Kun Zhang; Huang Jianqiang; Xiaoying Wang; Solving algorithm and parallel optimization of Helmholtz equation in GRAPES model, CONFCDS 2021.（EI、ISTP）",
                    "Xiaodong Hu; Huanli Xu; <b>Jinfang Jia*</b>; Xiaoying Wang; Research on distributed storage and query optimization of multi-source heterogeneous meteorological data, the 2018 International Conference on Cloud Computing and Internet of Things (CCIOT 2018),Singapore, 2018.",

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
                            <span>学术兼职</span>
                            </span>
                        </template>
                        <p v-html="t_messages.academic_part_time_job"></p>
                        </el-tab-pane>
                    </el-tabs>
                    <br/>
                    <el-tabs type="card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>学术职称</span>
                            </span>
                        </template>
                        {{t_messages.academic_title}}
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

