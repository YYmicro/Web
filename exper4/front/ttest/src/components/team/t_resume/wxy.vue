<script lang="ts" setup>
import { ref, reactive, onMounted } from "vue";
import type { TabsPaneContext } from 'element-plus'

var t_messages = {
        "name" : "王晓英",
        "imageurl" : "team/teacher/wxy.png",
        "qhu_title" : "教授",
        "edu_title" : "清华大学(博士)",
        "email" : "Wxy_cta@qhu.edu.cn",
        "academic_title" : "CCF 会员，ACM 会员，青海省计算机学会常务理事等",
        "main_studying_direction" : "高性能计算，绿色计算等",
        "individual_resume" : ["吉林双辽人，博士，教授，青海大学副校长，曾任计算机技术与应用系常务副主任（2013.6-2019.3）。1999年考入 清华大学计算机科学与技术系计算机科学与技术专业，于 2003 年获得学士学位。2003年9月以免试资格进入清华 大学计算机系攻读博士学位。2008年7月获博士学位，并被评为“清华大学优秀博士毕业生”。2008年8月到青海大 学计算机技术与应用系工作至今。2008年12月进入清华大学博士后流动站从事在职博士后研究工作，2010年12月 完成博士后工作出站。2013年任青海大学计算机系常务副主任。2014.8-2015.2被国家留学基金委选派赴Rutgers , The State University of New Jersey，USA计算机科学系做访问学者。任CCF（中国计算机学会）高级会员、 CCF西宁分部副主席、青海省计算机学会常务理事、中国高等教育学会地方大学教育研究分会监事等社会兼职。",
                                "目前担任《计算机系统平台》《计算机体系结构》课程的主讲工作，作为项目负责人完成国家级项目3项，省科技 厅应用基础研究计划项目2项，校级科研项目2项，横向课题4项，省级教改项目1项，校级一类课程建设项目1项 等；目前作为项目负责人正在承担国家级项目1项，横向课题1项。完成科技成果评价鉴定及成果登记5项，其中 国际领先1项，国际先进3项。主要在数据中心资源管理、数据中心能耗管理与可再生能源利用等方面开展了研究 工作并取得相应成果。2011年获批青海省高校“135高层次人才培养工程”创新教学科研骨干人才，并获“青海省普 通高等学校青年教师小岛奖励金”及“青海省教育系统优秀共产党员”等荣誉称号。2015年被评为“青海省优秀专业 技术人才”及青海省第十批自然科学与工程技术学科带头人。2016年入选青海省“高端创新人才千人计划”拔尖人才 （培养）。2017年获宝钢教育基金“优秀教师奖”。2021年入选青海省“昆仑英才·高端创新人才千人计划”领军人才 （培养），获得首届青海省科学成果奖“青年科技奖状”及省级教学成果奖二等奖。发表研究论文80余篇，获批授权 发明专利9项，软件著作权6项。",
                            ],
        "related_research_situation" : [
            {"name" : "国家自然科学基金项目“融合人工智能技术和数值模式的三江源区中短期降水预测方法研究”（No. 62162053，36万元）；2022.01-2025.12；", "position" : "项目负责人"},
            {"name" : "国家自然科学基金项目“智能电网影响感知的数据中心需求响应策略与机制研究”（No.61762074，39万元）；2018.01-2021.12；", "position" : "项目负责人"},
            {"name" : "国家自然科学基金项目“应用间歇性可再生能源的数据中心资源与能耗管理模型与算法研究”（No.61363019，45万元）；2014.01-2017.12；", "position" : "项目负责人"},
            {"name" : "国家自然科学基金项目“基于虚拟化技术的资源自主管理模型与机制”（60963005，20万元）；2010.1-2012.12,;", "position" : "项目负责人"},
            {"name" : "青海省科技计划项目-应用基础研究计划“GRAPES数值天气预报模式动力框架大规模并行算法与优化技术研究”（No.2019-ZJ-7034，35万元），2019.01-2021.12;", "position" : "项目负责人"},
            {"name" : "清华大学-宁夏银川水联网数字治水联合研究院横向课题（项目编号：SKL-IOW-2020TC2004-01）“基于深度学习和数值模式的短临降水预测系统”，2021.1-2023.1，20万元;", "position" : "项目负责人"},
            {"name" : "清华大学国家重点实验室开放基金 “基于多源卫星的天河工程数据集成平台”（No. sklhse-2017-A-05）, 2017.1-2018.12, 15万元;", "position" : "项目负责人"},
            {"name" : "赛尔网络下一代互联网技术创新项目“基于IPv6的光伏电站监控数据共享平台”(No.NGII20160505)，2017.1-2018.12，5万元;", "position" : "项目负责人"},
            {"name" : "青海省科技计划项目-应用基础研究计划“高压设备热图像在线监测故障诊断策略研究及应用”（No. 2014-ZJ-718），2014.07-2017.07;", "position" : "项目负责人"}
        ],
        "papers" : [
            {"year" : "2022",
             "journal" : ["Chenyu Ma, Jinfang Jia, Zhen Liu, Kun Zhang, Jianqiang Huang, <b>Xiaoying Wang</b>. Simulation of three-dimensional phase field model with LBM method using OpenCL, The Journal of Supercomputing, 2022:78(8), 11092–11110. (SCI源刊，影响因子2.557)",
                        "张琨,贾金芳,严文昕,黄建强,<b>王晓英</b>.GRAPES动力框架中大规模稀疏线性系统并行求解及优化[J/OL].计算机工程: 2022,48(01):149-154+162.（北大核心）",
                        "Zizhen Zhang; Tengfei Cao; <b>Xiaoying Wang</b>; Han Xiao; Jianfeng Guan. VC-PPQ: Privacy-preserving Q-learning Based Video Caching Optimization in Mobile Edge Networks. IEEE Transactions on Network Science and Engineering, 2022年8月3日. (已录用) （SCI源刊，影响因子5.033）",
                        "J. Huang, H. Wang, X. Fei, <b>X. Wang</b> and W. Chen, \" TC-Stream: Large-Scale Graph Triangle Counting on a Single Machine Using GPUs,\" in IEEE Transactions on Parallel and Distributed Systems, vol. 33, no. 11, pp. 3067-3078, 1 Nov. 2022, doi: 10.1109/TPDS.2021.3135329. （SCI源刊，CCF A, 影响因子3.757）",    
                        "曹腾飞，刘延亮，<b>王晓英</b>. 基于改进深度强化学习的边缘计算服务卸载算法, 计算机应用, 2022年7月1日（CSCD源刊，网络首发）",
                        "Yu Zhu, Haixing Zhao *, Jianqiang Huang, <b>Xiaoying Wang</b>. \"Hypernetwork Representation Learning with Common Constraints of the Set and Translation\". Symmetry, 2022（已录用）（SCI源刊，影响因子2.940）",
                        "Yanping Li, Lu Wang, Lei Zhang, Haiwen Chen, Shiying Wang, <b>Xiaoying Wang</b>. HrreNet: semantic segmentation network for moderate and high-resolution satellite images. International Journal of Remote Sensing, 2022: 43(11), pp.4065-4086. （SCI源刊，影响因子3.531）",
                    ],
             "conference" : ["Yu Zhu, Haixing Zhao, Jianqiang Huang, <b>Xiaoying Wang</b>. Hypernetwork Representation Learning with the Transformation Strategy. 2022 6th International Conference on High Performance Compilation, Computing and Communications, 2022, June 23-25.",
                        "Jian Wang, Tengfei Cao, <b>Xiaoying Wang</b>, Man Zhang, Jianfeng Guan. Resource Scheduling in Vehicular Networks with Age of Information and Channel Awareness. IEEE/CIC International Conference on Communications in China. 2022，11–13 August 2022.",
                    ],
            },
            {"year" : "2021",
             "journal" : ["Mengmeng Zhao, <b>Xiaoying Wang*</b>. A Synthetic Approach for Datacenter Power Consumption Regulation towards Specific Targets in Smart Grid Environment. Energies, 2021, 14(9), 2602. (SCI期刊，影响因子3.004, WOS：000650150300001, EI：20212210421500)",
                        "Haodong Bian, Jianqiang Huang*, Lingbin Liu, Dongqiang Huang, <b>Xiaoying Wang</b>. ALBUS: A Method for Efﬁciently Processing SpMV Using SIMD and Load Balancing. Future Generation Computer Systems.Volume 116, March 2021, Pages 371-392. (SCI期刊，影响因子6.125)",
                        "Haodong Bian, Jianqiang Huang, Jiahao Tang, Runting Dong, Li Wu, <b>Xiaoying Wang</b>. PAS: A new powerful and simple quantum computing simulator. Software: Practice and Experience, 2021: 1- 18. (SCI期刊，影响因子2.028)",
                        "Jianqiang Huang, Wentao Han, <b>Xiaoying Wang</b>, Wenguang Chen. Heterogeneous Parallel Algorithm Design and Performance Optimization for WENO on the Sunway TaihuLight Supercomputer. Tsinghua Science and Technology. 2020.25(1): 56-67(SCI源刊，影响因子1.697)",
                        "J. Huang, W. Xue, H. Bian, W. Yan, <b>X. Wang</b> and W. Chen. Helmholtz solving and performance optimization in global/regional assimilation and prediction system. Tsinghua Science and Technology, 2021, 26(3):335-346. (SCI期刊，影响因子1.328)",
                        "张琨,贾金芳,黄建强,<b>王晓英</b>,严文昕. 预处理共轭梯度算法异构并行求解及优化[J/OL].小型微型计算机系统:1-6. 2021-08网络首发（北大核心）",
                        "郭渝洛,边浩东,董润婷,唐嘉豪,<b>王晓英</b>,黄建强.基于SIMD高效并行傅里叶空间图像相似度计算研究[J/OL].计算机工程, 2021,47(11),247-253（北大核心）",
                        "江翠丽,曹腾飞,李长哲,<b>王晓英</b>.基于SVM的视频用户需求预测算法[J].计算机技术与发展,2021,31(05): 38-42.",
                    ],
             "conference" : ["Zhao Mengmeng, <b>Wang Xiaoying*</b>. Datacenter Power Consumption Regulation towards Specific Targets in Smart Grid Environment, 2021 Asia-Pacific Conference on Communications Technology and Computer Science (ACCTCS 2021), 2021, pp.33-36. (EI检索号：20211910328307)",
                            "Dingchang Huang, Runting Dong, <b>Xiaoying Wang*</b>. Modeling and Analysis of Demand Response Strategies for Datacenters in Smart Grid Environment. CONF-CDS 2021: The 2nd International Conference on Computing and Data Science, 2021, No.41, pp.1-6. (EI检索号：20212110387493)",
                            "Wenxin Yan, Jinfang Jia, Kun Zhang, Jianqiang Huang, and Xiaoying Wang. Solving algorithm and parallel optimization of Helmholtz equation in GRAPES model. In The 2nd International Conference on Computing and Data Science (CONF-CDS 2021). Association for Computing Machinery, New York, NY, USA, 2021, Article 171, 1–6. （EI检索号：20212110387319）",
                    ],
            },
            {"year" : "2020",
             "journal" : [" Peicong Luo, <b>Xiaoying Wang*</b> and Yuling Li. The Impact of Datacenter Load Regulation on the Stability of Integrated Power Systems. Sustainable Energy Technologies and Assessments, Volume 42, 2020, 100875. (SCI期刊，影响因子3.427)",
                    ],
             "conference" : []
            }
        ],
        "technological_achievements" : [
            "成果名称： 智能电网影响感知的数据中心需求响应策略与机制研究<br/><br/>批准登记号： 9632022J0263 推荐单位： 青海大学<br/>完成单位 青海大学<br/>完成人： 王晓英、黄建强、曹腾飞、贾金芳、张国晶、解辉、张玉安、张小丹、杨培、任洋甫、薛万东<br/>成果公报内容： 本项目以接入可再生能源的智能电网环境中部署和运行的数据中心为研究对象，面向可再生能源随季节和天气而随时变化的特性及电网自身负载的变化特性，考虑电网运行效率和安全性问题的约束，对能够感知电网运行状态的数据中心需求响应的策略和关键机制进行研究，旨在设计全面、完整的研究体系结构，并提供解决其中一些关键问题的思路。研究成果能够为绿色数据中心中可再生能源的利用和研究提供重要的参考，有助于进一步提高数据中心服务提供者的总体收益，也可促进可再生能源应用的快速发展和更大规模并网，对节能减排及环境保护具有重要的意义。成果达到国际领先水平。<br/>",

        ],
        "achievements_list" : [
            "专利授权：授权日期：2022年8月9日，名称：智能电网环境中数据中心功耗调节方法、系统、介质及设备，赵梦梦;王晓英。（公开(公告)号:CN112994037A 公开(公告)日:2021.06.18，申请号:CN202110141041.2，申请日:2021.02.02。 证书编号5373438。",

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
                        <el-tab-pane class="el_main_studying" label="主要研究方向" name="first">{{t_messages.main_studying_direction}}</el-tab-pane>
                    </el-tabs>
                    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
                        <el-tab-pane class="el_email" label="联系方式" name="first">{{t_messages.email}}</el-tab-pane>
                    </el-tabs>
                </el-col>
                <el-col :span="2"></el-col>
                <!-- 右边为个人简历 -->
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
                        <el-tabs tab-position="left" type="border-card" class="demo-tabs">
                            <el-tab-pane v-for="rrs in t_messages.papers" :label="rrs.year" :key="rrs">
                                <el-tabs type="card">
                                    <el-tab-pane label="期刊论文">
                                        <span v-for="(j,index) in rrs.journal" :key="j">[{{index+1}}]<p style="display: inline;" v-html="j"></p><br/><br/></span>
                                    </el-tab-pane>
                                </el-tabs>
                                <el-tabs type="card">
                                    <el-tab-pane label="会议论文">
                                        <span v-for="(c,index) in rrs.conference" :key="c">[{{index+1}}]<p style="display: inline;" v-html="c"></p><br/><br/></span>
                                    </el-tab-pane>
                                </el-tabs>
                            </el-tab-pane>
                        </el-tabs>
                        </el-tab-pane>
                    </el-tabs>
                    <br/>
                    <!-- 科技成果登记 -->
                    <el-tabs type="border-card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>科技成果登记</span>
                            </span>
                        </template>
                        <span v-for="(ta,index) in t_messages.technological_achievements" :key="ta">
                            [{{index+1}}]<p style="display: inline;" v-html="ta"></p><br/><br/>
                        </span>
                        </el-tab-pane>
                    </el-tabs>
                    <!-- 业绩列表 -->
                    <el-tabs type="border-card" class="demo-tabs">
                        <el-tab-pane>
                        <template #label>
                            <span class="custom-tabs-label">
                            <el-icon><calendar /></el-icon>
                            <span>业绩列表（近5年）</span>
                            </span>
                        </template>
                        <span v-for="(al,index) in t_messages.achievements_list" :key="al">
                            [{{index+1}}]<p style="display: inline;" v-html="al"></p><br/><br/>
                        </span>
                        </el-tab-pane>
                    </el-tabs>
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

