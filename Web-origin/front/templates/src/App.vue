<script>
  import axios from "axios"
  export default{
    data(){
      return{
        message : ''
      }
    },
    methods:{
      getData_get(){
        //设置axios
        axios({
          method : 'get',
          url : 'http://127.0.0.1:5000'
        }).then((rsp) => {
          this.message = rsp.data.message;
        })
      },
      getData_post(){
        //设置axios
        axios({
          method : 'post',
          url : 'http://127.0.0.1:5000'
        }).then((rsp) => {
          this.message = rsp.data.message;
        })
      }
    },
    mounted(){
    }
  }
</script>

<template>
  <button @click="getData_get">get</button>
  <button @click="getData_post">post</button>
  <h1>姓名 : {{message.name}}</h1><br>
  <h1>学号 : {{message.age}}</h1><br>
  <h1>学校 : {{message.score}}</h1><br>
  <h1>方法 : {{message.method}}</h1><br>
</template>
