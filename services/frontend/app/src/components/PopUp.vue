<template>
      <!-- Example in PopUp.vue template -->

  <div class="popup"  v-if="modelValue">
    
    <!-- Your pop-up content goes here -->
    <div class="popup-content">
      <button class=" material-symbols-outlined  button-45">arrow_back</button>
      <img src="/bitcoin-lock.png" alt="Bitcoin Lock" style="width:25%"> 
      <h1 style=" padding: 15px">This Secret Phrase is the Master key to your Wallet</h1>
      <ol >
        <li>Your 12-Words Secret Phrase is the Master Key to Your Wallet. Anyone that has Your Secret Phrase can access and Take Your Asset.</li>
        <li>Bitfriendly Wallet does not keep a copy of Your Secret Phrase</li>
        <li>Saving this Digitally in Plain Text is NOT Recommended. Examples include Screenshorts, text files, or Emailing Yourself</li>
        <li>Write Down Your Secret Phrase and Store it in a Secure Offline Location!</li>
      </ol>
      <h4 style="color: rgb(190, 205, 50); background-color: #123456;">Click continue to confirm you understand importance of your secret phrase</h4>
      <p style=" padding: 15px; "></p>
      <button @click="Dashboard">Continue</button>
    </div>
  </div>
</template>



  <script>
  export default {
    props: {
      modelValue: Boolean,
    },
    methods: {
      closePopup() {
        this.$emit('update:modelValue', false);
      },
      Dashboard() {
      this.$router.push('/SendCryptoFrom');
    },
    },
  };
  </script>
  
  <style scoped>

  
@media (min-width:320px) { /* smartphones, iPhone, portrait 480x320 phones */
  .popup {
        position: absolute;
        text-align: center;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 20px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        background-color: #123456 !important;
      }
  
  .popup-content {
        background-color: #123456 !important;
        position: absolute;
        width: 50vw; /* Set the width to 50% of the viewport width */
        min-width: 40rem;
        max-height: 800px;
        font-size: 22px;
        padding: 10px;
        color: #EDEAE0;
        align-items: center;
        text-align: center;
        top: 80%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-weight: 500;
    }


  img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  li{
    padding: 12px;
    letter-spacing:2px;
    font-size:3.2vw;
    
  }

  button {
    position: absolute;
    border-radius: 25px;
    background-color: #125634;
    color: #EDEAE0;
    max-width: 300px;
    min-width: 350Px;
    text-align: center;
    border: none;
    height: 40px;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

.material-symbols-outlined {
      position: fixed;
      top: 5%;
      left: 8%;
      transform: translate(-50%, -50%);
      color: #fff;
      font-variation-settings:
      'FILL' 0,
      'wght' 400,
      'GRAD' 0,
      'opsz' 24
    }

.button-45{
  background-color: transparent !important;
  border: none;
}


@media (min-width:1281px) { /* hi-res laptops and desktops */

  .material-symbols-outlined {
      position: fixed;
      top: 5%;
      left: 8%;
      transform: translate(-50%, -50%);
      color: #fff;
      font-variation-settings:
      'FILL' 0,
      'wght' 400,
      'GRAD' 0,
      'opsz' 24
    }

.button-45{
  background-color: transparent !important;
  border: none;
}


h1 {
      font-size: 4rem;
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
      font-size: 2.5rem;
      padding: 0 0 10px 0;
  }
.popup {
      position: absolute;
      text-align: center;
      top: 45%;
      left: 50%;
      transform: translate(-50%, -50%);
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);

    }

.popup-content {
        background-color: #123456 !important;
        position: absolute;
        max-width: 1000px; /* Increase the max-width */
        min-width: 300px; /* Increase the min-width */
        height: 800px;
        font-size: 24px; /* Increase the font-size */
        padding: 40px; /* Increase the padding */
        color: #EDEAE0;
        align-items: center;
        text-align: center;
        border-radius: 15px;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-weight: 500;
}

img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

li{
  padding: 6px;
  letter-spacing:0.6px;
  font-size:1.5vw;
  /* background-color: #123456; */
}

button {
  position: absolute;
  border-radius: 15px;
  background-color: #125634;
  color: #EDEAE0;
  max-width: 600px;
  min-width: 600Px;
  text-align: center;
  border: none;
  height: 40px;
  left: 45%;
  transform: translate(-50%, -50%);

  
}
}



</style>
  