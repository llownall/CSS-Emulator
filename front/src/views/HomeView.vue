<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <p>{{ isLoaderVisible }}</p>
    <button @click="getFromApi">123</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import {mapActions, mapGetters} from "vuex";
import {TEST_ACTION} from "@/store";

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  computed: {
    ...mapGetters([
      "isLoaderVisible"
    ])
  },
  methods: {
    ...mapActions({
      getFromApi: TEST_ACTION,
    })
  },
  created() {
    var source = new EventSource("http://localhost:8000/api/sse/");
    source.onmessage = function (event) {
      console.log(event)
    };
  }
}
</script>
