<script lang='ts' setup>
import { onMounted } from "vue";
onMounted(() => {
    let script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js';
    document.body.appendChild(script);
})
</script>
<template>
    <br/>
    <el-row>
    <el-col :span="3"></el-col>
    <el-col :span="18">
    <table class="table table-striped table-hover">
        <thead>
            <tr class="table-dark">
                <th scope="col">项目名称</th>
                <th scope="col">时间</th>
                <th scope="col">资助基金</th>
                <!-- <th scope="col">Handle</th> -->
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>融合人工智能技术和数值模式的三江源区中短期降水预测方法研究</td>
                <td>2022-2025</td>
                <td>国家自然科学基金</td>
            </tr>
            <tr>
                <td>清华大学-宁夏银川水联网数字治水联合研究院横向课题"基于深度学习和数值模式的短临降水预测系统"</td>
                <td>2021-2023</td>
                <td>横向课题</td>
            </tr>
            <tr>
                <td>三江源区数值天气预报模式移植优化与应用研究</td>
                <td>2022-2024</td>
                <td>青海省科技厅应用基础研究项目</td>
            </tr>
            <tr>
                <td>基于三江源数据分析平台的全球数值天气预报系统的性能优化技术研究</td>
                <td>2022-2024</td>
                <td>国家重点实验室开放基金</td>
            </tr>
            <tr>
                <td>智能电网影响感知的数据中心需求响应策略与机制研究</td>
                <td>2018-2021</td>
                <td>国家自然科学基金</td>
            </tr>
            <tr>
                <td>GRAPES数值天气预报模式动力框架并行并行算法与优化技术研究</td>
                <td>2019-2021</td>
                <td>青海省科技计划项目</td>
            </tr>
            <tr>
                <td>基于GPU异构体系结构的大规模图数据挖掘关键技术研究</td>
                <td>2020-2023</td>
                <td>国家自然科学基金</td>
            </tr>
            <tr>
                <td>基于超边建模的异质超网络表示学习研究</td>
                <td>2022-2025</td>
                <td>国家自然科学基金</td>
            </tr>
            <tr>
                <td>富超边的异质超网络表示学习关键技术研究</td>
                <td>2022-2024</td>
                <td>青海省自然科学基金</td>
            </tr>
            <!-- <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
            </tr>
            <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
            </tr>
            <tr>
                <th scope="row">3</th>
                <td colspan="2">Larry the Bird</td>
                <td>@twitter</td>
            </tr> -->
        </tbody>
    </table>
</el-col>
    <el-col :span="3"></el-col>
</el-row>
    <!-- <button type="button" class="btn btn-primary">Primary</button> -->
</template>
<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
</style>
