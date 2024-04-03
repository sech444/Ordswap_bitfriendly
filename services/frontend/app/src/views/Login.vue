<template>
    <div class="content-container" style="align-items: center;">
<h1 class="texthdcss">Welcome to Bitfriendly Wallet</h1>
<!-- <p></p> -->
<h2 class="thecss-2">Bitfriendly Wallet is non-custodial taproot BTC wallet that allow users to store and view BTC and Ordinals digital artifacts</h2>
<div class="">
  <button
          v-if="!isTouch"
            @click="passworddir()"
            class="input-fields24"
            tabindex="0"
            type="button"
            style="border: none;"
          >
            <span >Input Password to Access Bitfriendly Wallet</span>
          </button>
        
        
</div>

<div class="">
          <button
          v-if="!isTouch"
            @click="homedir()"
            class="button"
            tabindex="0"
            type="button"
            style="border: none;"
          >
            <span >Create new wallet</span>
          </button>
        
</div>
<div>
  <button
          v-if="!isTouch"
            @click="walletdir()"
            class="restoreButton"
            tabindex="0"
            type="button"
            style="border: none;"
          >
            <span >Restore Wallet</span>
          </button></div>
</div>
</template>



<script>
// import Restorewallet from '../components/Restorewallet.vue';

export default {
  // components: {
  //   Restorewallet
  // },
  methods: {
    async homedir() {
      this.$router.push('/Createpassword');
    },

    async walletdir() {
      this.$router.push('/Restorewallet');
    },
    // Add other methods if needed
    async passworddir() {
      this.$router.push('/Passworldpass');
  },

  },
  // Add other component options if needed
};
</script>





<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

@media (min-width:1281px) { /* hi-res laptops and desktops */

  .thecss-2{
      max-width: 20vw;
      position: absolute;
      top: 48%;
      min-width: 25%;
      text-align: center;
      color: rgb(255, 255, 255);
      letter-spacing: 0.00938em;
      padding: 20px;
      padding-bottom: 30px;
      font-size: 35px;
      left: 50%;
      // padding: 20px;
      transform: translate(-50%, -50%);
  }

  .content-container {
      margin-left: auto;
      margin-right: auto;
      padding: 20px ;
      max-height: auto;
      max-width: auto;
      min-width: 30%;
      font-weight: 63px;
      align-items: center;
      text-align: center;

  .button {
    position: absolute;
    max-width: 600px;
    background-color: #ffffff !important;
    padding: 20px;
    border-radius: 35px;
    min-width: 40%;
    color: #0D0D0E;
    align-items: center;
    text-align: center;
    top: 60%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    font-weight: 600;
  }
  .restoreButton {
    position: absolute;
    max-width: 600px;
    padding: 20px;
    border-radius: 45px;
    min-width: 50%;
    color: #ffffff;
    align-items: center;
    text-align: center;
    top: 78%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    font-weight: 600;
    background-color: transparent; /* or background-color: none; */
    border: 2px solid #ffffff; /* Add a border to make the button visible */
    cursor: pointer; /* Add cursor style to indicate interactivity */
  }
  .input-fields24{
    position: absolute;
    max-width: 600px;
    padding: 20px;
    border-radius: 45px;
    min-width: 50%;
    color: #ffffff;
    align-items: center;
    text-align: center;
    top: 55%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    font-weight: 600;
    background-color: transparent; /* or background-color: none; */
    border: 2px solid #ffffff; /* Add a border to make the button visible */
    cursor: pointer; /* Add cursor style to indicate interactivity */

  }
  .input-fields24 :hover{
    background-color: white;
    color: #000;
    font-size: 22px;
    font-weight: 600;
  }
      
  }

  .texthdcss{
        max-width: 500px;
        font-size: 4rem;
        padding-bottom: 30px;
        // align-items: center;
        letter-spacing: 0.00938em;
        color: rgb(255, 255, 255);
        position: absolute;
        top: 30%;
        min-width: 80%;
        text-align: center;
        font-weight: 400;
        margin: auto;
        left: 50%;
      transform: translate(-50%, -50%);

      }

    h1 {
        font-size: 6rem;
        padding-bottom: 0;
        margin-bottom: 0;
    }

    h2 {
        font-size: 4rem;
    }

    h3 {
        font-size: 3rem;
        padding: 0 0 10px 0;
    }

    h4 {
        font-style: italic;
        font-size: 1.1rem;
    }

    h5, h6 {
        font-size: 1rem;
    }

    h6 {
        font-style: italic;
    }

  .center-div {
      position: absolute;
      max-width: 600px;
      background-color: #ffffff !important;
      padding: 20px;
      border-radius: 100%;
      min-width: 80%;
      color: #0D0D0E;
      align-items: center;
      text-align: center;
      top: 68%;

  }

  .css-45{
    font-size: 150%;
    color: #123456;
    background-color: #ffffff;
  }


}

@media (min-width:320px) { /* smartphones, iPhone, portrait 480x320 phones */


  .content-container {
        margin-left: auto;
        margin-right: auto;
        padding: 20px ;
        max-height: auto;
        max-width: auto;
        min-width: 30%;
        font-weight: 63px;
        align-items: center;
        text-align: center;

  .button {
    position: absolute;
    max-width: 70%;
    background-color: #ffffff !important;
    padding: 20px;
    border-radius: 35px;
    min-width: 30vw;
    color: #0D0D0E;
    align-items: center;
    text-align: center;
    top: 65%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    font-weight: 600;
}
.restoreButton {
    position: absolute;
    max-width: 600px;
    padding: 20px;
    border-radius: 45px;
    min-width: 50%;
    color: #ffffff;
    align-items: center;
    text-align: center;
    top: 76%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    font-weight: 600;
    background-color: transparent; /* or background-color: none; */
    border: 2px solid #ffffff; /* Add a border to make the button visible */
    cursor: pointer; /* Add cursor style to indicate interactivity */
}

      
}

  
  .texthdcss {
        max-width: 800px;
        font-size: 4rem;
        padding-bottom: 30px;
        // align-items: center;0
        letter-spacing: 0.00938em;
        color: rgb(255, 255, 255);
        position: absolute;
        top: 35%;
        min-width: 80%;
        text-align: center;
        font-weight: 400;
        margin: auto;
        left: 50%;
      transform: translate(-50%, -50%);

}
    h1 {
        font-size: 3rem;
        padding-bottom: 0;
        margin-bottom: 0;
    }

    h2 {
        font-size: 2rem;
    }

    h3 {
        font-size: 1.5rem;
        padding: 0 0 10px 0;
    }

    h4 {
        font-style: italic;
        font-size: 1.1rem;
    }

    h5, h6 {
        font-size: 1rem;
    }

    h6 {
        font-style: italic;
    }

    .thecss-2{
        max-width: 30vw;
        position: absolute;
        top: 50%;
        min-width: 80%;
        text-align: center;
        color: rgb(255, 255, 255);
        letter-spacing: 0.00938em;
        padding: 20px;
        padding-bottom: 30px;
        left: 50%;
        font-size: 20px;
        // padding: 20px;
        transform: translate(-50%, -50%);
    }
}


</style>

 
