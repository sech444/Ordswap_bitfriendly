
<template>
    <div class="container">
      <div class="texthd-90">Restore Your Bitfriendly Wallet </div>
      <!-- <div class="thecss">You will use this Password to unlock your wallet.</div> -->
      <input type="mnemonic_words" class="input-phrase" placeholder="secret phrase">
      <input type="password" class="input-fields" v-model="password" placeholder="Password">
      <input type="password" class="input-field-css" v-model="confirmPassword" placeholder="Confirm Password">
      <button class="button" @click="restoreWallet()">Restore secret phrase</button>
      <p v-if="error" class="css-error" style="color: red;">{{ error }}</p>
      <!-- <div class="subtitle">Secret phrases will be shown on the next screen.</div> -->
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        password: '',
        confirmPassword: '',
        taprootAddress: '',
        privateExtendedKey: '',
        error: '',
        taproot_address: '',
        mnemonic_words: '',
        mnemonic: '',
      };
    },
    methods: {
      async restoreWallet() {
      if (!this.createPassword || !this.confirm_password || !this.mnemonicWords ) {
        this.error('mnemonicWords, Password or confirm_password is missing');
        return;
      }

     // Ensure mnemonic_words is populated from the input field
    this.mnemonic_words = document.querySelector('.input-phrase').value;
    console.log('Mnemonic words:', this.mnemonic_words);
    try {
    const response = await axios.post(
      'http://127.0.0.1:5000/users/',
      {
        mnemonic: this.mnemonic_words,
        password: this.password,
        confirm_password: this.confirmPassword,
      },
      
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      console.log('response.data:', response.data);
      //const {addresses, private_key, mnemonic } = response.data;
  
          // Assuming the response structure is something like this
      const responseData = response.data;
  
          // Handle success
      
      this.taprootAddress = responseData.addresses;
      this.privateExtendedKey = responseData.private_key;
      this.phrase = responseData.mnemonic;
  
      this.$store.commit('updateWalletInfo', {
            taproot_address: this.taprootAddress,
            private_key: this.privateExtendedKey,
            phrase: this.phrase,
          });
  
      // console.log('Wallet information stored in Vuex:', this.$store.state.updateWalletInfo);
      // Redirect to the new component
      this.$router.push({
        name: 'SecretPhraseDisplay',
      });
    } catch (error) {
      this.error = error.response?.data?.detail || 'An error occurred during wallet restore.';
     
    }
  },
    }
  };
  </script>
  
  
  
  
  
  <style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');
  
  .texthd-90 {
            max-width: 600px;
            font-size: 4rem;
            //align-items: center;
            letter-spacing: 0.00938em;
            color: rgb(255, 255, 255);
            position: absolute;
            top: 15%;
            min-width: 80%;
            text-align: center;
            font-weight: 400;
            margin: auto;
            padding-right: 10px;
            left: 50%;
            transform: translate(-50%, -50%);
          }
  
  
  
  h1 {
  font-weight: 400;
  font-size: 61px;
  }
  
  h2 {
  font-size: 25px;
  }
  
  .center-div {
      position: absolute;
      max-width: 600px;
      //background-color: #ffffff !important;
      padding: 20px;
      border-radius: 100%;
      min-width: 80%;
      color: #0D0D0E;
      align-items: center;
      text-align: center;
      top: 68%;
      
      }
  
  .thecss{
    max-width: 60rem;
    position: absolute;
    top: 35%;
    font-size: 2.8rem;
    min-width: 80%;
    text-align: center;
    color: rgb(255, 255, 255);
    letter-spacing: 0.00938em;
    padding-right: 10px;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .css-45{
  font-size: 150%;
  color: #123456;
  // background-color: #ffffff;
  }
  
  .content-container {
    margin-left: auto;
    margin-right: auto;
    padding: 20px ;
    padding-top: 5px;
    height: auto;
    max-width: 100%;
    font-weight: 63px;
    align-items: center;
    text-align: center;
  }
  
  .css-error{
            position: absolute;
            max-width: 100%;
            font-size: 14px;
            color: rgb(219, 35, 35);
            text-align: center;
            top: 85%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 20px;
            font-weight: 700;
  }
  
  
  body {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        .title {
            font-size: 24px;
            font-weight: bold;
        }
        .subtitle {
            position: absolute;
            max-width: 100%;
            font-size: 14px;
            color: rgb(190, 205, 50);
            text-align: center;
            top: 72%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 20px;
            font-weight: 700;
        }
  
  .input-phrase {
            position: absolute;
            max-width: 100%;
            padding: 10px;
            width: 500px;
            margin: 10px 0;
            border: 1px solid #ffffff;
            border-radius: 5px;
            background-color: #0b1c26 !important;
            color: #ffffff;
            top: 37%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;

  }
  
  .input-fields {
            position: absolute;
            max-width: 100%;
            padding: 10px;
            width: 500px;
            margin: 10px 0;
            border: 1px solid #ffffff;
            border-radius: 5px;
            background-color: #0b1c26 !important;
            color: #ffffff;
            top: 47%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
        }
  
  .input-field-css {
            position: absolute;
            max-width: 100%;
            padding: 10px;
            margin: 10px 0;
            width: 500px;
            border: 1px solid #ffffff;
            border-radius: 5px;
            background-color: #0b1c26 !important;
            color: #ffffff;
            top: 55%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 16px;
            cursor: pointer;
           
        }
        .button {
            position: absolute;
            max-width: 100%;
            min-height: 50px;
            background-color: #ffffff;
            color: #1a1a1a;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            text-align: center;
            top: 67%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 500px;
            cursor: pointer;
            font-weight: 700;
            font-size: 20px;
        }
   
  
  @media (min-width:320px) { /* smartphones, iPhone, portrait 480x320 phones */
  
    .subtitle {
              position: absolute;
              max-width: 100%;
              font-size: 20px;
              color: rgb(190, 205, 50);
              text-align: center;
              top: 80%;
              left: 50%;
              transform: translate(-50%, -50%);
              font-weight: 700;
          }
  
      .texthd-90 {
          max-width: 600px;
          font-size: 4rem;
          //align-items: center;
          letter-spacing: 0.00938em;
          color: rgb(255, 255, 255);
          position: absolute;
          top: 26%;
          min-width: 80%;
          text-align: center;
          font-weight: 400;
          margin: auto;
          padding-right: 10px;
        }
        
    .thecss{
      max-width: 60rem;
      position: absolute;
      top: 38%;
      font-size: 2.8rem;
      min-width: 80%;
      text-align: center;
      color: rgb(255, 255, 255);
      letter-spacing: 0.00938em;
      padding-right: 10px;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  
    .input-fields {
            position: absolute;
            max-width: 70%;
            padding: 10px;
            width: 500px;
            margin: 10px 0;
            border: 1px solid #ffffff;
            border-radius: 5px;
            background-color: #0b1c26 !important;
            color: #ffffff;
            top: 47%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
        }
  
  .input-field-css {
            position: absolute;
            max-width: 70%;
            padding: 10px;
            margin: 10px 0;
            width: 500px;
            border: 1px solid #ffffff;
            border-radius: 5px;
            background-color: #0b1c26 !important;
            color: #ffffff;
            top: 55%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 16px;
            cursor: pointer;
           
        }
  
        .button {
            position: absolute;
            max-width: 60%;
            min-height: 50px;
            background-color: #ffffff;
            color: #1a1a1a;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            text-align: center;
            top: 67%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 500px;
            cursor: pointer;
            font-weight: 700;
            font-size: 20px;
        }
        .input-phrase {
          position: absolute;
            max-width: 70%;
            padding: 10px;
            width: 500px;
            margin: 10px 0;
            border: 1px solid #ffffff;
            border-radius: 5px;
            background-color: #0b1c26 !important;
            color: #ffffff;
            top: 37%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
        }
  
  
  }
  </style>
  
  
  