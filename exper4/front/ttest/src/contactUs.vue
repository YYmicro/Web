<script lang='ts' setup>
import { onMounted } from "vue";
onMounted(() => {
    let script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js';
    document.body.appendChild(script);
})
</script>
<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css";
</style>
<template>
    <el-row>
        <el-col :span="3"></el-col>
        <el-col :span="18">
            <br/>
            <br/>
            <h4>我们组正在寻找积极进取的学生从事前沿研究项目。</h4>
            <p>非常欢迎各大本科生和研究生与我们联系，可以在<b>科研团队</b>中查找<font color="red">各位老师主页</font>进一步了解信息，下面为我们组各位优秀教师的联系方式，
欢迎各大学子根据兴趣联系相应老师，HDACP欢迎你们！
</p>
            <table class="table table-striped table-hover">
                <thead>
                    <tr class="table-dark">
                        <th>教师姓名</th>
                        <th>联系方式</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>王晓英</td>
                        <td>wxy_cta@qhu.edu.cn</td>
                    </tr>
                    <tr>
                        <td>黄建强</td>
                        <td>hjqxaly@163.com</td>
                    </tr>
                    <tr>
                        <td>贾金芳</td>
                        <td>qhu_jf@163.com</td>
                    </tr>
                    <tr>
                        <td>朱宇</td>
                        <td>sdcxzhuyu@163.com</td>
                    </tr>
                    <tr>
                        <td>张国晶</td>
                        <td>15297197253</td>
                    </tr>
                    <tr>
                        <td>吴利</td>
                        <td>wuli_qhu@163.com</td>
                    </tr>
                    <tr>
                        <td>边浩东</td>
                        <td>hpc_bhd@163.com</td>
                    </tr>
                </tbody>
            </table>
        </el-col>
        <el-col :span="3"></el-col>
    </el-row>
</template>