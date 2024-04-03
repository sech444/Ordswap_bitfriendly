<template>
  <div>
    <div class="content-block">
      <div class="circle"> change pfp</div>
      <div class="subt-Click">
        <span class="material-symbols-outlined">person</span>
      </div>
      <h1 class="bold">
        <span class="css-toper">Portfolio Value :</span
        ><span class="css-toperBTC-info">{{ formattedBtcAvailable }}</span>
        <span class="css-toperBTC"> BTC </span>
      </h1>
      <h3 class="css-left">
        <span class="green-text">Liquidity Value : </span
        ><span class="bold-css">{{ formattedBtcAvailable }}</span
        ><span class="bold-css-3"> BTC </span>
      </h3>
      <h3 class="css-right">
        <span class="green-text">Inscription Value : </span
        ><span class="bold-css-btc">{{ formattedBtcAvailable }}</span
        ><span class="bold-css-4"> BTC </span>
      </h3>
    </div>
    <div>
      <div>
      <div class="transaction-hold">
        <button v-if="!walletCreated" class="button-utc" @click="showPopupwallet()" style="margin-right: 10px;">Receive</button>

        <button type="button" class="button-utc-1" @click="showModal = true" style="margin-right: 10px;">Send</button>
        <button type="button" class="button-utc-2" @click="navigateToSendCryptoForm()">Shop</button>
      </div>
    
    </div>
      
    </div>
    <div class="bold-css-234">
      <h1>My Collection</h1>
    </div>
    <div class="bold-css-23456">
      <h1>BRC-20</h1>
    </div>
    <div class="bold-css-23478">
      <h1>Portfolio Activities</h1>
    </div>
    <div>

  </div>

      <walletqrcode v-model="popupVisible" />
  </div>
<div>
 
      <DashboardSendBTC v-if="showModal"> 
        <!-- Modal content goes here -->
        <!-- <p>This is the modal content</p> -->
        <button @click="showModal = false">Close Modal</button>
      </DashboardSendBTC>
   
    </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { ref } from 'vue';
import walletqrcode from './walletqrcode.vue';
import DashboardSendBTC from './DashboardSendBTC.vue';

export default {
  name: "Headerbtc",
  components: {
    walletqrcode,
    DashboardSendBTC
  },
  setup() {
    const store = useStore();
    let balas = 0;

  const showModal = ref(false);

    // Define computed properties with formatted values
    const formattedBtcAvailable = computed(() => {
      // Format btcAvailable to display "0.000"
      return store.state.btcAvailable.toFixed(4);
    });

    const isWalletModalOpen = ref(false);
    const walletCreated = ref(false);
    const popupVisible = ref(false); // Initialize popupVisible

    const showWalletModal = () => {
      isWalletModalOpen.value = true;
    };

    const showPopupwallet = () => {
      popupVisible.value = true; // Set popupVisible to true to show the pop-up
    };

    const closePopup = () => {
      popupVisible.value = false; // Set popupVisible to false to close the pop-up
    };

    const closePopupOutside = (event) => {
      // Check if the clicked element is outside the popup
      const popupElement = document.querySelector('.popup'); // Adjust selector if necessary

      if (popupElement && !popupElement.contains(event.target)) {
        closePopup();
      }
    };

    return {
      balas,
      formattedBtcAvailable,
      isWalletModalOpen,
      showWalletModal,
      walletCreated,
      popupVisible, // Return popupVisible
      showPopupwallet,
      closePopup,
      closePopupOutside,
      showModal,
    };
  },
};
</script>





<style lang="scss">

.button-utc, .button-utc-1, .button-utc-2 {
  max-width: 20vw;
  min-width: 30vw;
  background-color: #2b3139;
  font-weight: 300;
  font-size: 1vw;
  padding: 13px;
  color: #EDEAE0;
  text-align: center;
  position: absolute;
  top: 28%;
  transform: translate(-50%);
}

.button-utc {
  left: 19%;
}

.button-utc-1 {
  left: 50%;
}

.button-utc-2 {
  left: 81%;
}
      .green-text {
        color: #EDEAE0;
        font-size: 3vw
      }
      .header-wallet-text {
        color: #EDEAE0;
        font-weight: 300;
        margin-top: -90px;
        position: absolute;
        right: 6.23rem;
        padding-block-end: 10%;
        font-size: 18px;
      }
      .header-wallet {
        color: #fff;
        font-weight: 300;
        position: absolute;
        right: 9.23rem;
        //padding-bottom: 45px;
      }
      .circle {
          background: lightblue;
          border-radius: 50%;
          max-width: 9vw;
          min-width:  9vw;
          max-height: 9vw;
          min-height:  9vw;
          display: flex;
          justify-content: center;
          align-items: center;
      }

      a {
        text-decoration: none;
        color: inherit;
      }
      .content-block {
        padding-bottom: 12px;
        max-width: 30vw;
      }

      
      // .bold-css {
      //   position: absolute;
      //   left: 78%;
      //   font-weight: 400;
      //   font-size: 4vw;
      //   color: #afafaf;
      //   transform: translate(-50%, -50%);
        
      // }
      .bold-css-234 {
        font-weight: 400;
        font-size: 4vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
        position: absolute;
        left: 9%;
        top: 40%;
        text-align: center;
    }
    .bold-css-23456 {
        font-weight: 400;
        font-size: 4vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
        position: absolute;
        left: 7%;
        top: 65%;
        text-align: center;
    }
    .bold-css-23478 {
        font-weight: 400;
        font-size: 4vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
        position: absolute;
        left: 11%;
        top: 88%;
        
    }
      .subt-Click {
        position: absolute;
        max-width: calc(1.5rem + 1.3vw);
        //min-width: 30px;
        //font-size: 14px;
        //color: rgb(190, 205, 50);
        text-align: center;
        border-radius: 15px;
        top: 6%;
        left: 15%;
        transform: translate(-50%, -50%);
        font-weight: 700;
      }

      .bold-css-3 {
        position: absolute;
        top: 44%;
        left: 112%;
        font-weight: 400;
        font-size: 2vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
      }

      .bold-css-4 {
        position: absolute;
        top: 44%;
        left: 112%;
        font-weight: 400;
        font-size: 2vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
      }
      .bold-css-btc {
      position: absolute;
      font-size: calc(1.7rem + 1.5vw);
      top: 44%;
      left: 96%;
      transform: translate(-50%, -50%);
      word-spacing: 15px;

        
      }
    

.material-symbols-outlined {
            max-width: 200%;
            min-width: 13px;
            color: #fff;
            font-size: 200% !important; /* Add !important */
            font-variation-settings:
                'FILL' 0,
                'wght' 800,
                'GRAD' 0,
                'opsz' 24;
        }



      .app-header { 
          min-height: 64px;
          width: 100%;
          padding: 10px;
          // padding-bottom: 60px;
          border-radius: 35px;
          z-index: 2; // Set a higher z-index value
        }

      .logo-text {
        color: #ffffff;
        word-spacing: 12px;
        position: relative;
        // top: -20px;
         }

     
      .transaction-hold{
        // padding: 5px;
        margin: 1px;
      }
  .css-right {
      max-width: 20vw;
      min-width: 35vw;
      right: -2%;
      position: absolute;
      color: #afafaf;
      top: 25%;
      transform: translate(-50%, -50%);
}

.css-left {
  max-width: 20vw;
  min-width: 35vw;
  left: 30%;
  position: absolute;
  color: #afafaf;
  top: 25%;
  transform: translate(-50%, -50%);
  display: block;
}

.css-toper {
  font-size: 4.3vw;
  position: absolute;
  top: 16%;
  left: 35%;
  max-width: 50%;
  min-width: 35%;
  min-height: 2rem;
  transform: translate(-50%, -50%);
  word-wrap: break-word; /* Ensure long words wrap onto the next line */
  color: #EDEAE0;
}

.css-toperBTC {
  font-size: 3vw;
  position: absolute;
  top: 16.4%;
  left: 70%;
  max-width: 50%;
  min-width: 15%;
  min-height: 2rem;
  transform: translate(-50%, -50%);
  color: #afafaf;
}

.css-toperBTC-info {
  font-size: 3.8vw;
  position: absolute;
  top: 16.4%;
  left: 59%;
  max-width: 50%;
  min-width: 30%;
  min-height: 3rem;
  transform: translate(-50%, -50%);
  color: #afafaf;
}

.bold-css {
      position: absolute;
      font-size: calc(1.7rem + 1.5vw);
      top: 45%;
      left: 94.7%;
      transform: translate(-50%, -50%);

        
      }  

@media (max-width: 900px) { 
  .button-utc, .button-utc-1, .button-utc-2 {
    max-width: 30%;
    position: absolute;
    //min-width: auto;
    font-size: 12px;
    font-weight: 800;
    left: 50%;
    top: 40%; /* Reset the top value */
    transform: translate(-50%, -50%);
  }

  .button-utc {
    left: 19%; /* Adjust these values as needed */
  }

  .button-utc-1 {
    left: 50%; /* Adjust these values as needed */
  }

  .button-utc-2 {
    left: 81%; /* Adjust these values as needed */
  }
  .css-left {
      font-size: 1vw;
      position: absolute;
      top: 28%;
      left: 28%;
      max-width: 58%;
      min-width: 35%;
      transform: translate(-50%, -50%);
      word-wrap: break-word; /* Ensure long words wrap onto the next line */
      color: #EDEAE0;
  }
  .css-right {
      font-size: 0.81vw;
      position: absolute;
      top: 33.5%;
      left: 30%;
      max-width: 80%;
      min-width: 20%;
      transform: translate(-50%, -50%);
      word-wrap: break-word; /* Ensure long words wrap onto the next line */
      color: #EDEAE0;
  }
  .green-text {
      color: #EDEAE0;
      font-size: 6.5vw;
      font-weight: 400;
    }


    .green-text {
      color: #EDEAE0;
      font-size: 6.5vw;
      font-weight: 400;
    }
    .header-wallet-text {
      color: #EDEAE0;
      font-weight: 300;
      margin-top: -90px;
      position: absolute;
      right: 6.23rem;
      padding-block-end: 10%;
      font-size: 18px;
    }
    .header-wallet {
      color: #fff;
      font-weight: 300;
      position: absolute;
      right: 9.23rem;
      //padding-bottom: 45px;
    }
    .circle {
        max-width: 12rem;
        min-width: 12rem;
        max-height: 12rem;
        min-height: 12rem;
        //top: 60%; /* Reset the top value */
        
      }

    a {
      text-decoration: none;
      color: inherit;
    }
    .content-block {
      padding-bottom: 12px;
      max-width: 30vw;
    }

    .bold {
      font-weight: 600;


    }
    .css-toperBTC-info {
          position: absolute;
          top: 22%;
          left: 67%;
          font-size: calc(2.3rem + 1.8vw);
          transform: translate(-50%, -50%);
        }
   
    .subt-Click {
      position: absolute;
      max-width: calc(1.5rem + 1.3vw);
      text-align: center;
      border-radius: 15px;
      top: 7%;
      left: 35%;
      transform: translate(-50%, -50%);
      font-weight: 700;
            }

    .bold-css-234 {
        font-weight: 400;
        font-size: 4vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
        position: absolute;
        left: 18%;
        top: 48%;
        text-align: center;
    }
    .bold-css-23456 {
        font-weight: 400;
        font-size: 4vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
        position: absolute;
        left: 15%;
        top: 65%;
        text-align: center;
    }
    .bold-css-23478 {
        font-weight: 400;
        font-size: 4vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
        position: absolute;
        left: 23%;
        top: 88%;
        
    }
     


    .css-toper {          
      position: absolute;
      font-size: 6.9vw;
      top: 22%;
      left: 30%;
      transform: translate(-50%, -50%);
      word-wrap: break-word; /* Ensure long words wrap onto the next line */
      color: #EDEAE0;
              }

    .logo-text {
      color: #ffffff;
      word-spacing: 12px;
      position: relative;
      // top: -20px;
      
    }


    .transaction-hold{
      // padding: 5px;
      margin: 1px;
    }

    .css-toperBTC {
      position: absolute;
      font-size: calc(1.7rem + 1.5vw);
      top: 22%;
      left: 85%;
      transform: translate(-50%, -50%);

    }
  
    .bold-css {
      position: absolute;
      font-size: calc(1.7rem + 1.9vw);
      top: 40%;
      left: 130%;
      transform: translate(-50%, -50%);
      word-spacing: 15px;

        
      }
      .bold-css-btc {
      position: absolute;
      font-size: calc(1.7rem + 1.9vw);
      top: 40%;
      left: 103%;
      transform: translate(-50%, -50%);
      word-spacing: 15px;

        
      }
      .bold-css-3 {
        position: absolute;
        top: 38%;
        left: 165%;
        font-weight: 400;
        font-size: 4.3vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
        
}
.bold-css-4 {
        position: absolute;
        top: 38%;
        left: 125%;
        font-weight: 400;
        font-size: 4.5vw;
        color: #afafaf;
        transform: translate(-50%, -50%);
}
}
</style>