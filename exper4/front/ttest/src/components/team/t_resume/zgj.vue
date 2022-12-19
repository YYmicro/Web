<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

var t_messages = {
        "name" : " 张国晶",
        "imageurl" : "team/teacher/zgj.jpg",
        "qhu_title" : "讲师",
        "edu_title" : "青海大学(硕士)",
        "email" : "15297197253",
        "main_studying_direction" : "高性能计算",
        "individual_resume" : "2014年7月本科毕业于青海大学计算机技术与应用系计算机 科学与技术专业,获得工学学士。2017年7月硕士毕业于青海大学机械设计及理论专业， 年8月到青海大学计算机技术与应用系工作至今。目前担任《计算机应用基础》等课程的主讲工作。",
        "related_research_situation" : [
            {"name" : "应用间歇性可再生能源的数据中心资源与能耗管理模型与算法", "position" : "（参与科研）"},
            ],
        "papers" : ["<b>Guojing Zhang</b>, Xiaoying Wang*, Mengqin Yang. Managing and Scheduling Approximate Applications to Utilize Renewable Energy in Cloud Computing Datacenters. APPLIED ECOLOGY AND ENVIRONMENTAL RESEARCH, 2017, 15(3):307-321. (SCI)",
                    "<b>Guojing Zhang</b>, Xiaoying Wang*, Zhihui Du. Research on the Prediction of Solar Energy Generation based on Measured Environmental Data. International Journal of u- and e- Service, Science and Technology. 2015: 8(5): 385-402. （EI检索号：20152600975359）",
                    "<b>Guojing Zhang</b>, Xiaoying Wang*, Zhihui Du. Review of Heterogeneous Computing based on GPU. 2015 International Conference on Informatics, Control and Automation (ICA2015), July, 2015, Phuket, Thailand, pp.175-180. （ISTP检索号：000377614100032）",
                    "Xiaoying Wang, <b>Guojing Zhang</b>, Mengqin Yang. Chapter title: Green-aware Virtual Machine Migration Strategy in Sustainable Cloud Computing Environments. Cloud Computing (ISBN 978-953-51-4932-3) 已录用,待出版",
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

