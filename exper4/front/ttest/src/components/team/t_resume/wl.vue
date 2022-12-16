<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

var t_messages = {
        "name" : " 吴利",
        "imageurl" : "team/teacher/wl.jpg",
        "qhu_title" : "助教",
        "edu_title" : "清华大学(硕士)",
        "email" : "wuli_qhu@163.com",
        "main_studying_direction" : "高性能计算、深度学习、优化算法",
        "individual_resume" : "2019年7月在清华大学高性能所获得硕士学位，并在阿里巴巴担任一年算法工程师，从事高性能计算、深度学习，优化算法等相关研究。 2020年9月到青海大学计算机技术与应用系工作。",
        "related_research_situation" : [
            {"name" : "2017/04–2019/07 无缝隙气候模式集合预测方法", "position" : "研究项目参与人", "content" : "实验室承接的国家重大专项；主要负责研究气候集合预报中的机器学习方法，如利用回归算法构建气候模式的代理模式，用分类算法对暴雨等极端天气是否发生进行预测，用深度学习模型DBN来自动挖掘多个气候变量之间隐藏的内在的联合规律等。"},
            {"name" : "2017/07–2019/07 地球系统模式公共软件平台研发", "position" : "研究项目参与人", "content" : "实验室承接的国家重大专项：针对气候模式中由于高维物理参数不确定性导致模式性能不理想的问题，提出了高效率的有约束的优化算法，并设计了自动化调优的框架。"},
        ],
        "papers" : [" <b>Li Wu</b>, Tao Zhang, Yi Qin, Wei Xue. An effective parameter optimization with radiation balance constraint in CAM5 (version 5.3). Geoscientific Model Development.2020.",
                    "Xinliang Wang, Weifeng Liu, Wei Xue, and <b>Li Wu</b>. swSpTRSV: a fast sparse triangular solve with sparse level tile layout on sunway architectures[C]. Principles and Practice of Parallel Programming. ACM, 2018:338-353.",
                    "<b>Li Wu</b>,Tao Zhang, Yi Qin, et al. An effective parameter optimization with radiation balance constraint in CAM5. AGU Fall Meeting 2017(Poster).",
                    "<b>Li Wu</b>, Xiaoge Xin, Yanjie, Cheng, Wei Xue. Application of Breeding of Growing Mode ensemble method in seasonal prediction of climate system model. AGU Fall Meeting 2018(Poster).",
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
                            <span>个人简介</span>
                            </span>
                        </template>
                        <p>{{t_messages.individual_resume}}</p>
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
                            [{{index+1}}]<b>{{rrs.name}} {{rrs.position}}</b><br/>
                            <p>{{rrs.content}}</p>
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

