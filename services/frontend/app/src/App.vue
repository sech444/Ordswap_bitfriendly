<template>
  <div id="app">
   
    </div>

    <router-view />
    
</template>

<script>
import TopHeader from "@/components/top-header.vue";
import { mapGetters } from "vuex";
import TopMD from "@/components/top-md.vue";


export default {
  components: {
    "top-header": TopHeader,
    "top-md": TopMD,
 
  },
  data() {
    const { getSpinner } = mapGetters(["getSpinner"]);
    

    return {
      getSpinner,
    };
  },

};

</script>


<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 16px;
  // text-align: center;
  background-color: rgba(21, 30, 61, 0.5) !important;
}
// #app {
//   color: #3498db;
//   background-color: #2ecc71;
// }

#nav {
  padding: 0px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.page {
  position: absolute;
  background-color: rgba(21, 30, 61, 0.5); 
  z-index: 25;
  width: 100%;
  height: 100%;
}

.spinner {
  z-index: 26;
  position: relative;
  top: 50%;
}
</style>

