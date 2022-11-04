<template>
  <el-container>
    <el-header></el-header>
    <el-main>
      <el-row>
        <el-col :span="6"></el-col>
        <el-col :span="12">
          <el-input v-model="name" placeholder="Please input" />
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
      <el-row>
        <el-col :span="6"></el-col>
        <el-col :span="12">
          <el-radio-group v-model="sex">
            <el-radio label="1">male</el-radio>
            <el-radio label="0">female</el-radio>
          </el-radio-group>
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
      <el-row>
        <el-col :span="6"></el-col>
        <el-col :span="12">
          <el-button type="success" @click="sendData">submit</el-button>
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
      <el-row>
        <el-col :span="6"></el-col>
        <el-col :span="12">
          <el-card>
            <div class="card-header">
              <h3>Name : {{ rec_name }}</h3>
            </div>
            <div>
              <p>sex : {{ rec_sex }}</p>
            </div>
          </el-card>
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script lang="ts" setup>
import { ref } from "vue";
const name = ref("");
const sex = ref("");
const rec_name = ref("");
const rec_sex = ref("");
import axios from "axios";
function sendData() {
  axios({
    data: { name: name.value, sex: sex.value },
    method: "post",
    url: "http://127.0.0.1:5000",
  }).then((rsp) => {
    var message = rsp.data;
    // console.log(typeof message);
    // console.log(message);
    rec_name.value = message.name;
    rec_sex.value = message.sex;
  });
}
</script>
