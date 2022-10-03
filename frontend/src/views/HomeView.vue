<template>
  <div>
    <h1>Home</h1>
    <button @click="getJson">Get Json</button>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "Home",
    data(){
      return {
        json: []
      }
    },
    methods: {
      getJson() {
        axios.get('http://localhost:8000/api/saglik/  ')
          .then(response => {
            console.log(response.data);
          })
      }
    }
  }

</script>