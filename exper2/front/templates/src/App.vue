<script>
  import axios from "axios"
  export default{
    data(){
      return{
        message : '',
        number : ''
      }
    },
    methods:{
      getData_post(){
        //设置axios
        axios({
          data : this.number,
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
  
  <input v-model = "number" placeholder="Your userid"/>
  <button @click="getData_post">乘法表生成</button>
  <h1>乘法表:</h1><br/>
  <div>
    <p v-for="m in message">{{m}}</p><br/>
  </div>
  
</template>
