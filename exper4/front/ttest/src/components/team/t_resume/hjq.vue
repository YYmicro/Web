<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

var t_messages = {
        "name" : "黄建强",
        "imageurl" : "team/teacher/hjq.png",
        "qhu_title" : "教授",
        "edu_title" : "清华大学(博士)",
        "email" : "hjqxaly@163.com",
        "academic_title" : "中国计算机学会高性能计算专业委员会委员，中国计算机学学会高级会员，ACM会员，IEEE会员",
        "academic_part_time_job" : "IET image processing 审稿人（国际高水平SCI 期刊）<br/>Journal of supercomputing 审稿人（国际知名SCI 期刊）<br/>IEEE trans on big data审稿人（国际顶级大数据期刊）",
        "main_studying_direction" : "高性能计算、大规模图计算。重点面向高性能计算系统、智能计算系统，提高系统的数据通信性能瓶颈，提高系统整体性能和能效比。具体研究内容涵盖大规模系统性能评估、MPI应用性能优化等、智能计算系统（包括但不限于大规模深度学习框架优化）",
        "individual_resume" : ["黄建强，清华大学博士，中国计算机学会高性能计算专业委员会委员，现为青海大学教授，博士生导师，信息化技术中心副主任，超算团队教练，目前以第一作者/通信作者在IEEE TPDS、SPE、FGCS、J SUPERCOMPUT、CLUSTER COMPUTING、 清华大学学报、ACM CCGRID、ICA3PP、ICPADS等国内外知名期刊、会议上发表论文40余篇，入选2021年青海省“昆仑英才·高端创新创业人才”。",
                           ],
        "awards" : "本科毕设优秀指导教师、世界大学生超算竞赛全球一等奖、青海省教学竞赛优秀、青海大学教学成果二等奖、青海省小岛奖励金、青海大学突出贡献等",
        "related_research_situation" : [
            {"name" : "主持青海大学2013年校级中青年项目“步态识别在视频监控中的研究与应用”， 2万元", "position" : ""},
            {"name" : "国家自然科学基金项目“应用间歇性可再生能源的数据中心资源与能耗管理模型与算法研究”，45万元，", "position" : "参与"},
            {"name" : "青海省科技厅项目“高压设备热图像在线监测故障诊断策略研究及应用”，15万元", "position" : ""},
            {"name" : "《青海省气象科学研究所“数值模式高性能计算平台建设》16万", "position" : ""},
            {"name" : "智能电网影响感知的数据中心需求响应策略与机制研究（国家自然基金）", "position" : ""},
            {"name" : "中国气象局系统模式移植 ", "position" : "主持"},
            {"name" : "国家重点实验室开放基金：基于三江源数据分析平台的全球数值天气预报系统的性能优化技术研究，10万", "position" : "主持"},
            {"name" : "国家自然科学基金项目：基于GPU异构体系结构的大规模图数据挖掘关键技术研究，37万元，2021， ", "position" : "主持"},
            {"name" : "青海省科技厅项目：三江源区数值天气预报模式移植优化及应用研究 ，25万元，2022， ", "position" : "主持"},
           ],
        "papers" : [
            {"domain" : "大规模图计算系统",
             "content" : ["<b>Huang Jianqiang</b>; Haojie Wang; Xiang Fei; Xiaoying Wang ;Wenguang Chen.  Large-Scale Graph Triangle-Counting on a single Machine using GPUs.TPDS. 2022.<b>(CCF A, 国际顶级期刊)</b>",
                        "<b>Jianqiang Huang</b>; Wei Qin; Xiaoying Wang; Wenguang Chen. Pimiento: A Vertex-Centric Graph-Processing Framework on a Single Machine. ICA3PP-2019.<b>(CCF C，国际知名会议)</b>",
                        "<b>Huang, Jianqiang</b>; Qin, Wei; Wang, Xiaoying; Chen, Wenguang. Survey of external memory large-scale graph processing on a multi-core system.",
                        "Haodong Bian; <b>Jianqiang Huang*</b>; Runting Dong; Linbing Liu; Xiaoying Wang. CSR2: A New Format for SIMD-accelerated SpMV. CCGRID-2020.<b>(CCF C, 国际旗舰会议)</b>",
                        "Jiping Yu, Wei Qin, Xiaowei Zhu, Zhenbo Sun, <b>Jianqiang Huang</b>, Xiaohan Li, Wenguang Chen*. DFOGraph: An I/O- and Communication-Efficient System for Distributed Fully-out-of-Core Graph Processing. PPoPP2021.<b>(CCF A, 国际顶级会)</b>",
                        "Haodong Bian, <b>Huang Jianqiang*</b>，Lingbin Liu，Dongqiang Huang，and Xiaoying Wang. ALBUS: A Method for Efﬁciently Processing SpMV Using SIMD and Load Balancing. Future Generation Computer Systems. 2020.<b>(SCI期刊：中科院一区)</b>",
                    ]
            },
            {"domain" : "高性能计算",
             "content" : [" <b>Jianqiang Huang</b>; Kai Li; Xiaoying Wang. Single Image Super-resolution Reconstruction of Enhanced Loss Function with Multi-GPU Training, ISPA-2019.<b>(CCF C, 国际知名会议)</b>",
                        "A Retrieval Strategy of Load Balancing Optimization Scheme for CESM Based on Matrix Nesting. HPCChina 2019,<b>(CCF高性能计算年会)</b>",
                        "<b>Jianqiang Huang</b>; Wentao Han; Xiaoying Wang; Wenguang Chen. Heterogeneous Parallel Algorithm Design and Performance Optimization for WENO on the Sunway TaihuLight Supercomputer. Tsinghua Science and Technology, 2019. <b>(SCI期刊：JCR 2区)</b>",
                        "<b>Huang, Jianqiang</b>; Liang, Ye; Bian, Haodong; Wang, Xiaoying.Using Cluster Analysis and Least Square Support Vector Machine to Predicting Power Demand for the Next-Day. IEEE Access 2019.<b>(SCI期刊，JCR 1区)</b>",
                    ]
            },
            {"domain" : "计算机视觉",
             "content" : [" Kai Li; <b>Jianqiang Huang*</b>. Single Image Super Resolution Based on Generative Adversarial Networks. ICDIP2019.(EI、ISTP)",
                        "Kai Li; Shenghao Yang; Runting Dong; <b>Jianqiang Huang*</b>; Xiaoying Wang. A Survey of Single Image Super Resolution Reconstruction，April 2020，IET Image Processing.<b>(SCI期刊，CCF C)</b>",
                        "Huan Wu,<b>Jianqiang Huang*</b>,Xiaoying Wang,Jianbang Jia. Image Registration of Infrared and Visible Based on SIFT and SURF. The 10th International Conference on Digital Image Processing（ICDIP'2018）.(EI、ISTP)",
                        "<b>Jianqiang Huang*</b>, Zhengming Yi, Xiaoying Wang, Huan Wu.Gait Recognition System Based on (2D)2PCA and HMM[100].Eighth International Conference on Digital Image Processing (ICDIP 2016),10033. (EI、ISTP)",
                        " <b>Huang Jianqiang*</b>,Wu Huan, Wang Xiaoying and Yi Zhengming. Research and application of online monitoring fault diagnosis for infrared image and visible image registration[100]. 2016 6th International Workshop on Computer Science and Engineering(WCSE 2016), 765-772. (EI、ISTP)",
                        "<b>Huang Jianqiang*</b>, Wang Xiaoying, Cao Tengfei and Wang Rui.Speaking Video Summary Based on Face Detection in Moving Region[J].The Open Cybernetics & Systemics Journal,2014,8(1):784-789. （EI 期刊）",
                    ]

            }
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

const previewPDF = () => {
   let url = `http://mozilla.github.io/pdf.js/web/compressed.tracemonkey-pldi-09.pdf`;
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
                    </el-tabs>
                    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
                        <el-tab-pane class="el_edu_title" label="学历" name="first">{{t_messages.edu_title}}</el-tab-pane>
                    </el-tabs>
                    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
                        <el-tab-pane class="el_title" label="学术职称" name="first">{{t_messages.academic_title}}</el-tab-pane>
                    </el-tabs>
                    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
                        <el-tab-pane class="el_email" label="联系方式" name="first">{{t_messages.email}}</el-tab-pane>
                    </el-tabs>
                    <br/>
                    <el-button @click="previewPDF" style="font-weight: bold;" type="primary" plain>致报考我的硕士研究生们</el-button>
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
                            <span>学术论文发表</span>
                            </span>
                        </template>
                        <el-tabs type="border-card" class="demo-tabs">
                            <el-tab-pane v-for="rrs in t_messages.papers" :label="rrs.domain" :key="rrs">
                                <span v-for="(c,index) in rrs.content" :key="c">[{{index+1}}]<p style="display: inline;" v-html="c"></p><br/><br/></span>
                            </el-tab-pane>
                        </el-tabs>
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

