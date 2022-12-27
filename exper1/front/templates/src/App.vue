<script>
  import axios from "axios"
  export default{
    data(){
      return{
        message : '',
        userid : ''
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
          data : this.userid,
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
  
  <input v-model = "userid" placeholder="Your userid"/>
  <button @click="getData_post">登录</button>
  <h1>用户:{{message}}</h1>
  
</template>
