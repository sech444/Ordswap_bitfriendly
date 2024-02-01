<template>
    <div class="content-container" >
      <Header />
      <div class="center-div child">
      <Content :price="btcPrice" />
      <div class="txList">
          <TransactionList />
        </div>
      <Footer></Footer>
      <Footerbtc />
    </div>
  </div>
</template>

<script>
import axios from "axios";

import Header from "../components/Header";
import Content from "../components/Content";
import Footerbtc from "../components/Footerbtc";
import Footer from "../components/Footer";
import TransactionList from "../components/TransactionList";

export default {
  name: "SendCryptoForm",
  components: {
    Header,
    Content,
    Footerbtc,
    Footer,
    TransactionList,
  },
  data: function() {
    return { btcPrice: 0 };
  },
  mounted() {
    axios({
      url: "https://blockchain.info/ticker",
      method: "get",
    }).then((response) => {
      if (response && response.data && response.data.USD) {
        this.$store.dispatch("setPrice", {
          btcPrice: response.data.USD.last,
        });
      }
    });
  },
};
</script>




<style lang="scss">

@import url("https://fonts.googleapis.com/css?family=Roboto");

html {
  font-size: 62.5%;
}

body {
  margin: 0;
  padding: 0;
  font-family: "Roboto", sans-serif;
  font-size: 12px;
  //background-color: #f5f5f5;
  overflow: auto;
}

// #sechApp {
//   padding: 2px;
//   margin: 2px;
  

.content-container {
  margin-left: auto;
  margin-right: auto;
  padding: 20px ;
  padding-top: 5px;
  height: auto;
  max-width: 100%;
  font-weight: 63px;
}
.center-div {
  max-width: 600px;
  background-color: #2b3139 !important;
  padding: 20px;
  border-radius: 45px;
  min-width: 80%;
  color: #0D0D0E;

}
.child {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.box {
  width: 100px;
  height: 100px;
  background-color: red;
  position: relative;
  animation-name: example;
  animation-duration: 4s;
  animation-iteration-count: infinite;
}

/* Rest of your styles remain unchanged */

    @keyframes example {
      0%   {background-color: red; left: 0px; top: 0px;}
      25%  {background-color: yellow; left: 200px; top: 0px;}
      50%  {background-color: blue; left: 200px; top: 200px;}
      75%  {background-color: green; left: 0px; top: 200px;}
      100% {background-color: red; left: 0px; top: 0px;}
    }




.row {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  width: 100%;
}

.content-block {
  padding: 10px;
  align-items: center;
}

.block-size-1-2 {
  width: 48%;
}

.block-size-1-3 {
  width: 32%;
}

.block-size-2-3 {
  width: 65%;
}

.newtransaction-mobile-button {
  display: none;
}

.vertical-divider {
  border-right: 1px solid #e9eaf4;
}

h1 {
  font-weight: 400;
  font-size: 61px;
}

h2 {
  font-size: 25px;
}

.section-title {
  font-size: 3.4rem;
  //font-family: 'Courier New', Courier, monospace;
  color: #e9eaf4
  
}
@media only screen and (max-width: 768px) {
  // .content-right {
  //   margin: 0;
  // }

  h1.title {
    text-align: center;
  }

  .block-size-1-2 {
    width: auto;
  }

  .block-size-1-3 {
    width: auto;
  }

  .block-size-2-3 {
    width: auto;
  }

  .row {
    display: block;
  }
}

</style>
