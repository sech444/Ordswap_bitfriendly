


<template>
  <div>
    <top-header></top-header>
    <div class="">
    <div style="margin-top: 1.03rem;" class="transaction-value-spacing ">
    <button v-if="!walletCreated" type="button" class="button" @click="createWallet()">Create  Wallet</button>
    <button v-if="!walletCreated && !walletId" type="button" class="button" @click="getWalletIdAndCheckBalances()">Get Balances</button>
    <!-- <button v-if="!walletCreated" :disabled="!walletCreated"  type="button" class="button" @click="navigateToSendCryptoForm()">Send Btc</button> -->
    <button v-if="!walletCreated"  type="button" class="button" @click="navigateToSendCryptoForm()">Send Btc</button>
  </div>
</div>
    <div class="my-rows">
      <div v-if="walletCreated || privateExtendedKey" class="send-crypto-form">
        <button class="copy-button" @click="copyText('private-key')">Copy Text</button>
        <h2 style="padding: 10px; color: red">Generated private_key: </h2>
        <p id="private-key">{{ privateExtendedKey }}</p>
      </div>
      <div v-if="walletCreated || Taproot_Address" class="send-crypto-form">
        <button class="copy-button" @click="copyText('address')">Copy Text</button>
        <h2 style="color: red">Generated Address: </h2>
        <p id="address">{{ Taproot_Address }}</p>
      </div>
      <div v-if="walletCreated || phrase" class="send-crypto-form">
        <button class="copy-button" @click="copyText('mnemonic')">Copy Text</button>
        <h2 style="color: red">Generated Mnemonic: </h2>
        <p id="mnemonic">{{ phrase }}</p>
      </div>
      <div v-if="!walletId && btcBalances" class="send-crypto-form wallet">
       
        <h2 style="color: red">BTC Balances: </h2>
        <p id="btcBalances" style="padding: 6px">{{ btcBalances["final_balance"] }}</p>
        <div v-if="errorMessage">{{ errorMessage }}</div>
      
      <div> <h1>Address</h1>
    <p id="btcBalances">{{btcBalances["address"] }}</p>
    </div>
    <h1>Total received</h1>
   
    <p id="btcBalances">{{ btcBalances["total_received"] }} btc</p>
    <h1>Total sent</h1>
    <p id="btcBalances">{{ btcBalances["totalSent"] }} btc</p>
    <h1>Balance</h1>
    <p>{{ balance }} btc</p>
    <div class="transactions">
      <h1>Transactions</h1>
      <div v-for="transaction in transactions" :key="transaction.id">
        <p>{{ transaction.date }}</p>
        <p>{{ transaction.amount }} btc</p>
      </div>

      </div>
      
      <div v-if="walletCreated">
        <h3 style="padding: 10px; color: red" class="send-crypto-form">

        Warning: Please backup your wallet before close || BITFRIENDLY has no access to your private or mnemonic.
        </h3>
        <!-- <button class="button" @click="closeForm()">Close</button> -->
      </div>

      
    </div>

  
  </div>

  </div>
  <div class="my-rows">
  <h3 style="padding: 10px; color: red; margin-top: 3rem;" class="send-crypto-form">

Warning: Never disclose this key. Anyone with your private keys can steal any assets held in your wallet.
</h3>
</div>
  <Footer></Footer>
</template>

<script>
import TopHeader from "@/components/top-header.vue";
import TopMD from "@/components/top-md.vue";
import Footer from "@/components/Footer.vue";
import SendCryptoFrom from "@/views/SendCryptoForm.vue";
import axios from 'axios';
import router from '@/router/index.js'; 




export default {
  name: 'CreateWallet',
  components: {
    TopHeader,
    TopMD,
    Footer,
    SendCryptoFrom
  },
  data() {
    return {
      walletCreated: false,
      walletId: false,
      Taproot_Address: '',
      privateExtendedKey: '',
      phrase: '',
      btcBalances: null,
      errorMessage: null,
     
    };
  },
  methods: {
    navigateToSendCryptoForm() {
    // Use Vue Router to navigate to the SendCryptoForm.vue page
    router.push({ name: 'SendCryptoForm' }); // Replace 'SendCryptoForm' with the actual name or path of your route
  },
    createWallet() {
      // Set the base URL using axios.create() if you want to override it for this specific request
      const api = axios.create({
        baseURL: 'https://bitfriendly-api.onrender.com/',  // Update with your FastAPI backend address
      });

      api.get('/HDwallets')
        .then(response => {
          // handle success
          this.Taproot_Address = response.data.addresses['p2wsh']; 
          this.privateExtendedKey = response.data.private_key;
          this.phrase = response.data.mnemonic;
          this.walletCreated = true;
          this.btcBalances = null; 
        })
        .catch(error => {
          alert("BITFRIENDLY Wallet offline ");
          console.log(error);
        });
    },
    async getWalletIdAndCheckBalances() {
      const walletId = prompt('Enter your wallet ID:');

      if (walletId) {
        // Only proceed if the user provided a wallet ID
        this.userAddress = walletId;
        await this.getBTCBalances();
        //console.log(walletId)
      } else {
        // Handle case where the user canceled the prompt
        console.log('User canceled wallet ID input.');
      }
    },
    
   async getBTCBalances() {
    try {
      const response = await fetch(`https://api.blockcypher.com/v1/btc/main/addrs/${this.userAddress}`, {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json', // Updated Content-Type
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      this.btcBalances = data; // Assuming data directly contains the balances
      console.log(this.btcBalances);
      this.error = null;
    } catch (error) {
      console.error('Error fetching BTC balances:', error);
      this.error = 'Error fetching BTC balances';
    }
  },


  copyText(id) {
    const textToCopy = document.getElementById(id).innerText;
    navigator.clipboard.writeText(textToCopy).then(() => {
      console.log("Copied to clipboard: " + textToCopy);
      alert("Copied!");
    }, (error) => {
      console.error('Could not copy text: ', error);
    });
  },

    closeForm(formType) {
      // Reset all form-related data properties to close the form
      this.walletCreated = false;
      this.privateExtendedKey = null;
      this.Taproot_Address = null;
      this.phrase = null;
    }
  },
};
</script>



<style lang="scss" scoped>

.div-style{
  border-radius: 20px 2px 0 0;
  background: #838383;
  width: 45px;
}
.button {
  background-color: rgb(0, 162, 255);
  column-gap: 20px;
  font-weight: 300;
  font-size: 1.6rem;
  padding: 8px 23px;
  border-radius: 13px;
  outline: none;
  transition: all 0.5s;
  
}

.copy-button {
  background-color: #4CAF50;
  color: white;
  padding: 5px 32px;
  text-align: center;
  text-decoration: none;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
  position: absolute;
  right: 27.03rem;
  position: absolute;
  margin: auto;
  font-size: 18px;
  transform: translateY(-60px);
}


.button:hover {
  background: #afafaf;
  transition: all 0.5s;
  cursor: pointer;
  /* box-shadow: 1px 1px 1px 1px #88888854; */
}

.button:focus {
  background: #afafaf;
  transition: all 0.5s;
  /* box-shadow: 0.8px 0.8px 0.8px 0.8px #8888889e; */
}

.my-rows {
  padding-top: 3px;
  display: flex;
  //flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  max-width: 65rem;
  margin-left: auto;
  margin-right: auto;
}


.error-status {
  align-self: flex-start;
  color: #db2828;
  font-size: 1rem;
  font-style: italic;
  height: 8px;
}

.button-transaction-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.transaction-value-text {
  margin: 0;
  font-size: 1.2rem;
}

.transaction-value-spacing {
  //margin-right: 2px;
  margin-bottom: 0px;
  display: flex;
  column-gap: 2px;
  justify-content: space-around ;
}

.send-crypto-form {
  border: 2px solid #fa04d3;
  background-color: white;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 20px;
  text-decoration: none;
  font-size: 28px;
  color: black;
  margin-bottom: -8px;
  text-align: center;
  width: 100%;
  margin-top: 10px;
  font-weight: bold;

}

.input {
  border: none;
  color: #838383;
  font-weight: 300;
  line-height: 1rem;
  border-bottom: 1px solid #e7e7e7;
  padding: 5px 15px;
}

.input:focus {
  transition: all 0.2s;
  border-bottom: 1px solid #74cab3;
  /* box-shadow: 0.8px 0.8px 0.8px 0.8px #8888889e; */
}

.input::selection {
  background: #74cab3;
  color: #fff;
}

.input::placeholder {
  font-style: italic;
  color: #999999;
  font-size: 1.4rem;
}

.wallet-input {
  padding: 5px;
}

.input-spacing {
  margin-bottom: 20px;
  width: 100%;
}

.bold {
  font-weight: 700;
}

input:focus {
  outline: none;
}

@media only screen and (max-width: 768px) {
  .send-crypto-form {
    max-width: 80vw;
    display: block !important;
    flex-wrap: flex-end;
    overflow: auto;
  }
}

@media only screen and (max-width: 768px) {

  .copy-button {
    background-color: #4CAF50;
    color: white;
    //padding: 5px 32px;
    text-align: center;
    text-decoration: none;
    font-size: 13px;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
    position: absolute;
    margin-top: 35px;
    right: -0.3rem;
    padding-top: -50px;
    border-radius: 5px;

  }
}

@media only screen and (max-width: 1124px) {
  .button-transaction-container {
    flex-flow: column;
  }

  .transaction-value-spacing {
    margin-bottom: 10px;
  }

  .transaction-value-spacing {
    align-self: flex-start;
  }

  .button {
    align-self: flex-end;
  }
}
.wallet {
  background-color: #000;
  color: #fff;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.wallet h1 {
  color: #0f0;
  margin-bottom: 5px;
}

.wallet p {
  margin-bottom: 20px;
}

.transactions {
  border-top: 1px solid #0f0;
  margin-top: 20px;
  padding-top: 20px;
}

.transactions div {
  border-bottom: 1px solid #0f0;
  padding-bottom: 20px;
  margin-bottom: 20px;
}
</style>
