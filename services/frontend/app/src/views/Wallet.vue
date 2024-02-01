<template>
  <header>
    <div id=app>
      <top-header></top-header>
      <!-- <TopMD></TopMD> -->
    </div>
  </header>
  <div class="MuiBox-root css-18ljo6z  child">
        <div
          class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation0 MuiAlert-root MuiAlert-standardWarning MuiAlert-standard css-1wcb4vn"
          role="alert"
        >
          <div class="MuiAlert-icon css-1l54tgj">
            <svg
              class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cw4hi4"
              focusable="false"
              aria-hidden="true"
              viewBox="0 0 24 24"
              data-testid="ReportProblemOutlinedIcon"
            >
              <path
                d="M12 5.99L19.53 19H4.47L12 5.99M12 2L1 21h22L12 2zm1 14h-2v2h2v-2zm0-6h-2v4h2v-4z"
              ></path>
            </svg>
          </div>
          <div class="MuiAlert-message css-1xsto0d">
            There is a phishing website out there, to be safe
            <p></p>
            <ol>
              <li>make sure you are landing on bitfriendly.<b>me</b></li>
              <li>
                never try to enter any keys that were not generated on bitfriendly
              </li>
              <li>
                when connecting via metamask make sure domain in the message
                matches domain you are on
              </li>
            </ol>
          </div>
        </div>
        <div class="MuiBox-root css-1rwzrlh">
          <div class="MuiBox-root css-uewl2b">
            <h2 class=" css-1cqd3n0">
              Connect with Wallet
            </h2>
          </div>
        <div class="css-z2fqyo">
          <button
          v-if="!isTouch"
            @click="handleConnect()"
            class="css-4563"
            tabindex="0"
            type="button"
            style="border: none;"
          >
            <span >Connect</span>
          </button>
          <div v-if="isTouch" style="color: black;">
          <input v-model="Enter_password" type="password" placeholder="Enter Password">
          <button @click="loginWallet()">Login</button>
          <p v-if="loginError" style="color: red;">{{ loginErrorMessage }}</p>
          <p v-if="loggedIn">Logged in!</p>
        </div>

      </div>

      <div class="MuiBox-root css-1rwzrlh">
          <div class="MuiBox-root css-uewl2b">
            <h2 class="MuiTypography-root MuiTypography-h2 css-1cqd3n0">
              Or Import your key
            </h2>
          </div>
        <div class="css-z2fqyo">
          <button
          v-if="!ishandleRecoverWallet"
            @click="handleRecoverWallet()"
            class="css-4563"
            tabindex="0"
            type="button"
            style="border: none;"
          >
          <span >BITFRIENDLY Key</span>
          </button>
          <div v-if="ishandleRecoverWallet" style="color: black;">
            <label for="mnemonicWords">Mnemonic Words:</label>
            <input v-model="mnemonicWords" type="text" id="mnemonicWords" placeholder="mnemonic seed" />
            <input  v-model="createPassword" type="password" placeholder="create Password">
            <input v-model="confirm_password" type="password" placeholder="confim_password">
          <button class="but" @click="recoverWallet()">Recover Wallet</button>
          <!-- <p v-if="loginError" style="color: red;">{{ loginErrorMessage }}</p> -->

        </div>
        </div>
      </div>
      
          <div class="MuiBox-root  css-1xaekgw">
            <p class="MuiTypography-root MuiTypography-body1 css-9l3uo3">
              If you don't have <span style="color: #fcd535;">BIT</span>FRIENDLY key, you can create new one
            </p>
            </div>
            <div class="css-z2fqyo">
            <button
          v-if="!touchCreate"
            @click="handleCreate()"
            class="css-4563"
            tabindex="0"
            type="button"
            style="border: none;"
          >
            <span >Create new wallet</span>
          </button>
          
          <div v-if="touchCreate" style="color: black;">
            <input  v-model="create_Password" type="password" placeholder="create Password">
            <input v-model="password_confirm" type="password" placeholder="confim_password">
          <button @click="createWallet()">Create</button>
         
 
        </div>
        </div>
        </div>
        <div class="my-rows">
      <div v-if="walletCreated || privateExtendedKey" class="send-crypto-form">
        
        <h2 style="padding: 10px; color: #fcd535">Generated private_key: </h2>
        <p id="private-key">{{ privateExtendedKey }}</p>
      </div>
      <div v-if="walletCreated || Taproot_Address" class="send-crypto-form">
      
        <h2 style="color: #fcd535">Generated Address: </h2>
        <p id="address">{{ Taproot_Address }}</p>
      </div>
      <div v-if="walletCreated || phrase" class="send-crypto-form">
      
        <h2 style="color: #fcd535">Generated Mnemonic: </h2>
        <p id="mnemonic">{{ phrase }}</p>
      </div>
      </div>
        <div class="MuiBox-root css-1rwzrlh">
          <h2 class="MuiTypography-root MuiTypography-h2 css-1cqd3n0">
            Sign in with xpub(Beta)
          </h2>
          <a
            class="MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-fullWidth MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-fullWidth css-112fg7o"
            tabindex="0"
            href="/psbt/import"
            >Sign in<span class="MuiTouchRipple-root css-w0pj6f"></span
          ></a>
        </div>
      
        <div style="align-items:center">
      <Footer></Footer>
    </div>
  </div>

  </template>

<script >

import TopHeader from "@/components/top-header.vue";
import TopMD from "@/components/top-md.vue";
import Footer from "@/components/Footer.vue";
import Web3 from 'web3';
import axios from 'axios';




export default {
  name: 'wallet',
  components: {
    TopHeader,
    TopMD,
    Footer,
  },
  
  data() {
    return {
      isTouch: '',
      touchCreate: '',
      contractResult: '',
      ishandleRecoverWallet: '',
      mnemonic_words: '', // Set this to your mnemonic words
      movedUp: false,
      walletCreated: false,
      walletId: false,
      Taproot_Address: '',
      privateExtendedKey: '',
      phrase: '',
      createPassword: '',
      create_Password: '',
      Enter_password: '',
      confirm_password: '',
      password_confirm: '',
      mnemonicWords: '', // Holds the user input for mnemonic words imported from
      enteredPassword: '',
      loginError: false,
      loggedIn: false,
    };
  },

  methods: {
    handleConnect() {
      // Logic to handle the 'Connect' button click
      this.isTouch = true; // Set isTouch to true when the 'Connect' button is clicked
    },
    handleCreate() {
      // Logic to handle the 'Connect' button click
      this.touchCreate = true; // Set isTouch to true when the 'Connect' button is clicked
    },
    handleRecoverWallet() {
      // Logic to handle the 'Connect' button click
      this.ishandleRecoverWallet = true; // Set isTouch to true when the 'Connect' button is clicked
    },



    async loginWallet() {
      if (!this.Enter_password ) {
        console.error('Password or confirm_password is missing');
        return;
      }
      try {
        const response = await axios.post('http://127.0.0.1:5000/token/', 
        {
          password: this.Enter_password,
        },
        {
         headers: {
              'Content-Type': 'application/json',
            },
          });

          console.log(response.data);
        // Access the access token from the response
        const accessToken = response.data.access_token;
        const taproot_address = response.data.taproot_address;
        const private_key = response.data.private_key;
        console.log(accessToken);
        // Store the access token in Vuex
        //this.$store.dispatch('index/loginSuccess', accessToken);
        this.$store.commit('updateWalletInfo', {
        taproot_address: response.data.taproot_address,
        private_key: response.data.private_key
        });

        // Update component state
        this.loggedIn = true;
        this.loginError = false;

        // Redirect or perform other actions on successful login
        this.$router.push('/sendCryptoForm'); // Example redirect

        console.log('Login successful');
      } catch (error) {
        // Handle login failure
        this.loginError = true;
        // Reset error state
        this.loginErrorMessage = '';

        if (error.response && error.response.data && error.response.data.detail) {
          // Capture and display the error message
          this.loginErrorMessage = error.response.data.detail;
        } else {
          // Display a generic error message
          this.loginErrorMessage = 'An error occurred during login.';
        }

        console.error('Login failed', error);
      }
    },

 
   
    generateAddress() {
      const keyPair = bitcoin.ECPair.makeRandom({ rng: secp256k1.rng });
      const publicKey = keyPair.publicKey;
      const { address } = bitcoin.payments.p2tr({
        pubkey: bitcoin.payments.segwit({ pubkey: publicKey }).publicKey,
        network: bitcoin.networks.bitcoin,
      });
      this.TaprootAddress = address;
    },
    async createWallet() {
      if (!this.create_Password || !this.password_confirm) {
        console.error('Password or confirm_password is missing');
        return;
      }

      try {
        const response = await axios.post(
          'http://127.0.0.1:5000/users/',
          {
            
            password: this.create_Password,
            confirm_password: this.password_confirm,
        
          },
          {
          headers: {
                'Content-Type': 'application/json',
            },
      
          },
          
        );

        // Assuming the response structure is something like this
        const responseData = response.data;

        // Handle success
        this.Taproot_Address = responseData.addresses;
        this.privateExtendedKey = responseData.private_key;
        this.phrase = responseData.mnemonic;
        //this.walletCreated = true;
      } catch (error) {
        // Handle error
        console.error('Wallet creation failed', error);

        // Reset any relevant state
        //this.walletCreated = false;

        // Display an error message
        if (error.response && error.response.data && error.response.data.detail) {
          // Capture and display the error message
          console.error('Error message:', error.response.data.detail);
        } else {
          // Display a generic error message
          console.error('An error occurred during wallet creation.');
        }
      }
    }
    ,
  isValidBitcoinAddress(address) {
      try {
        bitcoin.address.toOutputScript(address, bitcoin.networks.bitcoin);
        return true;
      } catch (error) {
        return false;
      }
    },


    // Check if Web3 provider is available (e.g., Metamask)
    isWeb3ProviderInstalled() {
      return window.ethereum || window.web3;
    },

    // Check if Bitcoinjs library is available
    isBitcoinjsInstalled() {
      return typeof bitcoin !== 'undefined';
    },

    // Check if any wallet (Web3 provider or Bitcoinjs) is installed
    isAnyWalletInstalled() {
      return this.isWeb3ProviderInstalled() || this.isBitcoinjsInstalled();
    },

    // Connect function
    Connect() {
      // Check if any wallet is installed
      if (this.isAnyWalletInstalled()) {
        // Request accounts for Bitcoin (not Ethereum)
        ethereum
          .request({ method: 'eth_requestAccounts' })
          .then((accounts) => {
            if (accounts.length > 0) {
              this.connected = true;
              alert('Connected to the Bitcoin wallet!');
              console.log('Wallet ID: ' + accounts[0]);
              // You can use accounts[0] as the Bitcoin wallet address
            } else {
              // User canceled connection request
              alert('Connection request canceled by the user.');
              console.error('Connection request canceled.');
            }
          })
          .catch((err) => {
            // Handle errors during connection
            alert('Error connecting to the Bitcoin wallet.');
            console.error('Error connecting to the Bitcoin wallet:', err);
          });
      } else {
        // No wallet is installed
        alert('No Bitcoin wallet is installed!');
        console.error('No Bitcoin wallet is installed.');
      }
    },
    async recoverWallet() {
      if (!this.createPassword || !this.confirm_password || !this.mnemonicWords ) {
        console.error('mnemonicWords, Password or confirm_password is missing');
        return;
      }

      try {
        const response = await axios.post(
          'http://127.0.0.1:5000/users/',
          {
            mnemonicWords: this.mnemonicWords,
            password: this.createPassword,
            confirm_password: this.confirm_password,
        
          },
          {
          headers: {
                'Content-Type': 'application/json',
            },
      
          },
          
        );
          // Assuming the response structure is something like this
          const responseData = response.data;

        // Handle success
        this.Taproot_Address = responseData.addresses;
        this.privateExtendedKey = responseData.private_key;
        this.phrase = responseData.mnemonic;
        //this.walletCreated = true;

         // Redirect or perform other actions on successful login
        this.$router.push('/sendCryptoForm'); // Example redirect
        } catch (error) {
        // Handle error
        console.error('Wallet recovering failed', error);

        // Reset any relevant state
        //this.walletCreated = false;

        // Display an error message
        if (error.response && error.response.data && error.response.data.detail) {
          // Capture and display the error message
          console.error('Error message:', error.response.data.detail);
        } else {
          // Display a generic error message
          console.error('An error occurred during recovering wallet.');
        }
        }
        },
 
    async fetchTokenList() {
      const url = 'https://www.okx.com/api/v5/explorer/brc20/token-list';
      const headers = {
        'OK-ACCESS-KEY': '08430EAE9C1D094D49EFF0AA78D164D0',
        'OK-ACCESS-SIGN': 'f3642522-9474-43fd-8aad-48a6b9ca4154',
        'OK-ACCESS-TIMESTAMP': '1691412867904',
      };
      try {
        const response = await axios.get(url, { headers });
        console.log(response.data); // Handle the response data as needed
      } catch (error) {
        console.error('Error fetching token list:', error);
        // Handle errors as needed
      }
    },
  }
 };
</script>


<style lang="scss">
@import '../components/index-import.css';
@import '../components/index-inscribe.css';

* {
  box-sizing: border-box;
}

.navbar {
  display: flex;
  position: relative;
  justify-content: space-between;
  align-items: center;
  background-color: #2b3139;
  color: white;
}


.css-1s9msd {
  width: 100%;
  margin-left: auto;
  box-sizing: border-box;
  margin-right: auto;
  display: block;
  padding-top: 34px;
  padding-bottom: 48px;
}
.css-4563{
  font-size: 180%;
  color: #fcd535;
  background-color: #2b3139;
}

.brand-title {
  font-size: 1.1rem;
  margin: 0.5rem;
}
.css-white{
  color: white;
  font-size: 1rem;
  background-color: white;
}

.navbar-links {
  height: 100%;
}

.navbar-links ul {
  display: flex;
  margin: 0;
  padding: 0;
}

.navbar-links li {
  list-style: none;
}
.send-crypto-form {
  border: 2px solid #fcd535;
  background-color: #2b3139;
  // display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 10px;
  text-decoration: none;
  font-size: 20px;
  color: #ffffff;
  margin-bottom: 8px;
  text-align: center;
  width: 100%;
  margin-top: 10px;
  font-weight: bold;
  white-space: nowrap;
  overflow-wrap:break-word;
  max-width: 80vw;
  display: block !important;
  flex-wrap: flex-end;
  overflow: auto;
}

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

.nav-menu.active {
  left: 0;
}
@keyframes moveLabel {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0);
  }
}

.animate {
  animation-name: moveLabel;
  animation-duration: 0.5s;
}
.alert{
  background-color: white !important;
}

.navbar-links li a {
  display: block;
  text-decoration: none;
  color: white;
  padding: 1.8rem;
}

.navbar-links li:hover {
  background-color: #fcd535;
}

.toggle-button {
  position: absolute;
  top: 1.85rem;
  right: 3rem;
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 20px;
  height: 15px;
}
.css-1wcb4vn .MuiAlert-icon {
  color: rgb(255, 167, 38);
}
.css-1l54tgj {
  margin-right: 12px;
  padding: 7px 0px;
  display: flex;
  font-size: 152px;
  opacity: 0.9;
}
*,
::before,
::after {
  box-sizing: inherit;
}
.css-1wcb4vn {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400px;
  font-size: 0.875rem;
  line-height: .43rem;
  letter-spacing: 0.01071em;
  color: rgb(255, 226, 183);
}


.toggle-button .bar {
  height: 3px;
  width: 100%;
  background-color: white;
  border-radius: 15px;
}
.css-1cw4hi4 {
  user-select: none;
  width: 1em;
  height: 1em;
  display: inline-block;
  fill: currentcolor;
  flex-shrink: 0;
  transition: fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  font-size: inherit;
}
*,
::before,
::after {
  box-sizing: inherit;
}


.css-1xsto0d {
  padding: 8px 0px;
  min-width: 20px;
  overflow: auto;
  max-height: 700px;
  font-size: 17px;
}
*,
::before,
::after {
  box-sizing: inherit;
}

@media (max-width: 800px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
  }

  .toggle-button {
    display: flex;
  }

  .navbar-links {
    display: none;
    width: 100%;
  }

  .navbar-links ul {
    width: 100%;
    flex-direction: column;
  }

  .navbar-links ul li {
    text-align: center;
  }

  .navbar-links ul li a {
    padding: 0.5rem 1rem;
  }

  .navbar-links.active {
    display: flex;
  }
}

.css-1xaekgw {
  margin-top: 20px;
}

.material-symbols-outlined {
  font-size: 2.8rem;
  margin-right: 12px;
  font-variation-settings: "FILL" 0, "wght" 700, "GRAD" 0, "opsz" 24;
}

.child {
    display: block;
  margin-left: auto;
  margin-right: auto;
}

.css-9l3uo3 {
  margin: 0px;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 2.23rem;
  line-height: 1.5;
  letter-spacing: 0.00938em;
  color: white;
  padding-bottom: 1.5rem;
}

.css-h4os0j {
  font: inherit;
  letter-spacing: inherit;
  color: currentcolor;
  border: 0px none;
  box-sizing: content-box;
  background: rgba(0, 0, 0, 0) none repeat scroll 0% 0%;
  height: 1.4375em;
  margin: 0px;
  display: block;
  min-width: 0px;
  width: 100%;
  animation-name: mui-auto-fill-cancel;
  animation-duration: 10ms;
  padding: 16.5px 14px;
  
}

.css-1mlxe5f {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  cursor: text;
}


.css-z2fqyo {
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  position: relative;
  box-sizing: border-box;
  background-color: transparent;
  outline: currentcolor none 0px;
  margin: 0px;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 1.875rem;
  line-height: 1.75;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  min-width: 64px;
  padding: 5px 15px;
  border-radius: 4px;
  transition: background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  border: 1px solid #fcd535;
  color: #fcd535;
}

.css-112fg7o {
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  position: relative;
  box-sizing: border-box;
  background-color: transparent;
  outline: currentcolor none 0px;
  margin: 0px;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 1.875rem;
  line-height: 1.75;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  min-width: 64px;
  padding: 5px 15px;
  border-radius: 4px;
  transition: background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  border: 1px solid #fcd535;;
  color: #fcd535;
  width: 100%;
}


.css-feqhe6 {
  display: inline-flex;
  flex-direction: column;
  position: relative;
  min-width: 0px;
  padding: 0px;
  margin: 0px;
  border: 0px none;
  vertical-align: top;
  width: 100%;
}
.css-2bf9hj {
  color: rgba(255, 255, 255, 0.7);
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  padding: 0px;
  display: block;
  transform-origin: left top 0px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: calc(100% - 24px);
  position: absolute;
  text-decoration:none;
  left: 0px;
  top: 0px;
  transform: translate(14px, 16px) scale(1);
  transition: color 200ms cubic-bezier(0, 0, 0.2, 1) 0ms, transform 200ms cubic-bezier(0, 0, 0.2, 1) 0ms, max-width 200ms cubic-bezier(0, 0, 0.2, 1) 0ms;
  z-index: 1;
  pointer-events: none;
  
}
.css-1f8gpsx {
  margin-bottom: 12px;
  display: flex;
  flex-flow: row wrap;
  -moz-box-pack: justify;
  justify-content: space-between;
  gap: 6px;
  background-color: rgb(32, 32, 32);
}

.cut-edge {
  position: sticky;
  top: -5px;
  text-overflow: ellipsis;
  white-space: nowrap;
  height: 40px;
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  position: relative;
  box-sizing: border-box;
  outline: currentcolor none 0px;
  border: 0px none;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1.03rem;
  line-height: 1.27rem;
  letter-spacing: 0.01857em;
  text-transform: uppercase;
  min-width: 5rem;
  padding: 8px 8px;
  border-radius: 5px;
  transition: background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,
    box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,
    border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,
    color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  color: rgb(255, 255, 255);
  background-color: #fcd535;
  box-shadow: rgba(0, 0, 0, 0.2) 0px 3px 1px -2px,
    rgba(0, 0, 0, 0.14) 0px 2px 2px 0px, rgba(0, 0, 0, 0.12) 0px 1px 5px 0px;
  margin-left: -20px;
  margin-right: -15px;
}

.css-1kdt6ud {
  width: 35px;
  height: 35px;
  border-radius: 18px;
  text-align: center;
  -moz-box-align: center;
  align-items: center;
  display: flex;
  -moz-box-pack: center;
  justify-content: center;
  background: #fcd535;
  overflow: hidden;
  margin-right: 108px;
}

.css-2ceacx {
  background-color: rgb(32, 32, 32);
  padding: 32px 0px;
  margin-top: 24px;
}
*, ::before, ::after {
  box-sizing: inherit;
}

.css-18ljo6z {
  max-width: 900px;
  padding: 20px;
  background-color: #2b3139;
  border-radius: 45px;
}

*,
::before,
::after {
  box-sizing: inherit;
}

body {
  color: rgb(255, 255, 255);
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 5rem;
  line-height: 1.5;
  letter-spacing: 0.00938em;
}

.css-1ctifg4 {
  margin: 0px;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  line-height: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 900;
  letter-spacing: 0.2rem;
  font-size: 20px;
  cursor: pointer;
  color: white;
  margin-left: 40px;
  margin-top: -25px;
}

.small-button.MuiButton-root {
  padding: 2px 8px;
  font-size: 12px;
  min-width: 30px;
}

.css-1r11lh4 {
  display: flex;
  place-items: center;
  cursor: pointer;
  padding: 16px;
}

.css-1i17ufj {
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  box-sizing: border-box;
  background-color: transparent;
  outline: currentcolor none 0px;
  border: 0px none;
  margin: 0px;
  border-radius: 0px;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 0.875rem;
  line-height: 1.15;
  letter-spacing: 0.01857em;
  text-transform: uppercase;
  max-width: 360px;
  min-width: 90px;
  position: relative;
  min-height: 48px;
  flex-shrink: 0;
  padding: 11px 16px;
  overflow: hidden;
  white-space: normal;
  text-align: center;
  flex-direction: column;
  color: rgba(155, 155, 155, 0.7);
}

.css-uewl2b {
  margin-bottom: 20px;
}

.css-1cqd3n0 {
  margin: 0px;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-size: 36px;
  letter-spacing: 0.15rem;
  font-weight: 900;
  line-height: 56px;
  text-transform: uppercase;
  color: white;
}

.css-1rwzrlh {
  margin-bottom: 60px;
  display: flex;
  justify-content: space-around;
  flex-direction: column;
}

.css-krltcp {
  max-width: 100%;
  display: flex;
  flex-wrap: wrap;
  -moz-box-align: center;
  align-items: center;
  gap: 10px;
  padding: 6px 11px 0px;
}

.css-1f8gpsx {
  margin-bottom: 12px;
  padding: 8px;
  display: flex;
  flex-flow: row wrap;
  -moz-box-pack: justify;
  justify-content: space-between;
  gap: 6px;
  background-color: black;
}

.css-13o7eu2 {
  display: block;
}

.css-1xlhn9g {
  overflow: hidden;
  min-height: 48px;
  display: flex;
  padding-top: 8px;
}

element {
  overflow: hidden;
  margin-bottom: 0px;
}

.css-1anid1y {
  position: relative;
  display: inline-block;
  flex: 1 1 auto;
  white-space: nowrap;
  overflow-x: hidden;
  width: 100%;
}

*,
::before,
::after {
  box-sizing: inherit;
}

.css-k008qs {
  display: flex;
}

.css-1i27ufj.Mui-selected {
  color: rgb(250, 4, 211);
  font-size: 1.2rem;
}

.css-1wcb4vn {
  transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  border-radius: 4px;
  box-shadow: none;
  background-image: linear-gradient(
    rgba(255, 255, 255, 0),
    rgba(255, 255, 255, 0)
  );
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1.075rem;
  line-height: 1.43;
  letter-spacing: 0.01071em;
  background-color: rgb(25, 18, 7);
  display: flex;
  padding: 8px 16px;
  color: rgb(255, 226, 183);
}

.css-gmuwbf {
  display: flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
}
.css-1i27ufj {
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  box-sizing: border-box;
  background-color: transparent;
  outline: currentcolor none 0px;
  border: 0px none;
  margin: 0px;
  border-radius: 0px;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 0.875rem;
  line-height: 1.25;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  max-width: 360px;
  min-width: 90px;
  position: relative;
  min-height: 48px;
  flex-shrink: 0;
  padding: 12px 16px;
  overflow: hidden;
  white-space: normal;
  text-align: center;
  flex-direction: column;
  color: rgba(255, 255, 255, 0.7);
}

*,
::before,
::after {
  box-sizing: inherit;
}

.css-wt6402 {
  margin: 0px;
  color: rgb(250, 4, 211);
  text-decoration: underline rgba(250, 4, 211, 0.4);
}

.css-1i27ufj.Mui-selected {
  color: rgb(250, 4, 211);
  font-size: 1.2rem;
}


.css-1mlxe5f {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  box-sizing: border-box;
  cursor: text;
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  width: 100%;
  position: relative;
  border-radius: 4px;
}

.css-1i27ufj {
  cursor: pointer;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 0.875rem;
  line-height: 1.25;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  white-space: normal;
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
}

.css-1i27ufj {
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  box-sizing: border-box;
  background-color: transparent;
  outline: currentcolor none 0px;
  border: 0px none;
  margin: 0px;
  border-radius: 0px;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 0.875rem;
  line-height: 1.25;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  max-width: 360px;
  min-width: 90px;
  position: relative;
  min-height: 48px;
  flex-shrink: 0;
  padding: 12px 16px;
  overflow: hidden;
  white-space: normal;
  text-align: center;
  flex-direction: column;
  color: rgba(255, 255, 255, 0.7);
}

.css-w0pj6f {
  overflow: hidden;
  pointer-events: none;
  position: absolute;
  z-index: 0;
  inset: 0px;
  border-radius: inherit;
}

*,
::before,
::after {
  box-sizing: inherit;
}

.css-1i27ufj {
  cursor: pointer;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 0.875rem;
  line-height: 1.25;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  white-space: normal;
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
}

*,
::before,
::after {
  box-sizing: inherit;
}

*,
::before,
::after {
  box-sizing: inherit;
}

.css-18iu0mu {
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  position: relative;
  box-sizing: border-box;
  outline: currentcolor none 0px;
  border: 0px none;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 0.575rem;
  line-height: 0.75;
  letter-spacing: 0.2857em;
  text-transform: uppercase;
  min-width: 4px;
  padding: 6px 16px;
  border-radius: 4px;
  transition: background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,
    box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,
    border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,
    color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  color: rgb(255, 255, 255);
  background-color: rgb(250, 4, 211);
  box-shadow: rgba(0, 0, 0, 0.2) 0px 3px 1px -2px,
    rgba(0, 0, 0, 0.14) 0px 2px 2px 0px, rgba(0, 0, 0, 0.12) 0px 1px 5px 0px;
  margin: 8px 12px;
}

.css-1i27ufj {
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  box-sizing: border-box;
  background-color: transparent;
  outline: currentcolor none 0px;
  border: 0px none;
  margin: 0px;
  border-radius: 0px;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 1.2rem;
  line-height: 1.25;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  max-width: 360px;
  min-width: 90px;
  position: relative;
  min-height: 48px;
  flex-shrink: 0;
  padding: 12px 16px;
  overflow: hidden;
  white-space: normal;
  text-align: center;
  flex-direction: column;
  color: rgba(255, 255, 255, 0.7);
}

*,
::before,
::after {
  box-sizing: inherit;
}

.css-1anid1y {
  white-space: nowrap;
}

element {
  left: 0px;
  width: 90px;
}

.css-19tgd8k {
  position: absolute;
  height: 2px;
  bottom: 0px;
  width: 100%;
  transition: all 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  background-color: rgb(250, 4, 211);
}

.css-1i27ufj {
  cursor: pointer;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  font-size: 0.875rem;
  line-height: 1.25;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  white-space: normal;
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
}

.css-krltcp {
  max-width: 100%;
  display: flex;
  flex-wrap: wrap;
  -moz-box-align: center;
  align-items: center;
  gap: 10px;
  padding: 6px 12px 0px;
}

.css-bcctbf {
  display: flex;
  gap: 10px;
  overflow-x: auto;
  white-space: nowrap;
  max-width: 100%;
  padding-top: 6px;
  background-color: black;
}

.css-13sljp9 {
  display: inline-flex;
  flex-direction: column;
  position: relative;
  min-width: 0px;
  padding: 0px;
  margin: 0px;
  border: 0px none;
  vertical-align: top;
}

.css-bcctbf {
  white-space: nowrap;
}

.css-1xskxc1 {
  color: rgba(255, 255, 255, 0.7);
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 2rem;
  line-height: 2.4375em;
  letter-spacing: 0.00938em;
  padding: 0px;
  display: block;
  transform-origin: left top 0px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: calc(133% - 24px);
  position: absolute;
  left: 0px;
  top: 0px;
  transform: translate(14px, -9px) scale(0.75);
  transition: color 200ms cubic-bezier(0, 0, 0.2, 1) 0ms,
    transform 200ms cubic-bezier(0, 0, 0.2, 1) 0ms,
    max-width 200ms cubic-bezier(0, 0, 0.2, 1) 0ms;
  z-index: 1;
  pointer-events: auto;
  user-select: none;
}

.css-1oqfyky {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  box-sizing: border-box;
  cursor: text;
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  position: relative;
  border-radius: 4px;
}

.css-bcctbf {
  white-space: nowrap;
}

.css-13sljp9 {
  display: inline-flex;
  flex-direction: column;
  position: relative;
  min-width: 0px;
  padding: 0px;
  margin: 0px;
  border: 0px none;
  vertical-align: top;
}

.css-bcctbf {
  white-space: nowrap;
}

.css-1xskxc1 {
  color: rgba(255, 255, 255, 0.7);
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  padding: 0px;
  display: block;
  transform-origin: left top 0px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: calc(133% - 24px);
  position: absolute;
  left: 0px;
  top: 0px;
  transform: translate(14px, -9px) scale(0.75);
  transition: color 200ms cubic-bezier(0, 0, 0.2, 1) 0ms,
    transform 200ms cubic-bezier(0, 0, 0.2, 1) 0ms,
    max-width 200ms cubic-bezier(0, 0, 0.2, 1) 0ms;
  z-index: 1;
  pointer-events: auto;
  user-select: none;
}

.css-1oqfyky {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  box-sizing: border-box;
  cursor: text;
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  position: relative;
  border-radius: 4px;
}

.css-1y7k1sw.css-1y7k1sw.css-1y7k1sw {
  padding-right: 32px;
}

.css-1y7k1sw {
  appearance: none;
  user-select: none;
  border-radius: 4px;
  cursor: pointer;
  font: inherit;
  letter-spacing: inherit;
  color: currentcolor;
  border: 0px none;
  box-sizing: content-box;
  background: rgba(0, 0, 0, 0) none repeat scroll 0% 0%;
  height: 1.4375em;
  margin: 0px;
  display: block;
  min-width: 0px;
  width: 100%;
  animation-name: mui-auto-fill-cancel;
  animation-duration: 10ms;
  padding: 8.5px 14px;
  padding-right: 14px;
}

.css-1k3x8v3 {
  bottom: 0px;
  left: 0px;
  position: absolute;
  opacity: 0;
  pointer-events: none;
  width: 100%;
  box-sizing: border-box;
}

.css-1oqfyky {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  cursor: text;
}

.css-yop3gh {
  user-select: none;
  width: 1em;
  height: 1em;
  display: inline-block;
  fill: currentcolor;
  flex-shrink: 0;
  transition: fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  font-size: 1.5rem;
  position: absolute;
  right: 7px;
  top: calc(50% - 0.5em);
  pointer-events: none;
  color: rgb(255, 255, 255);
}

.css-1oqfyky {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  cursor: text;
}

.css-1oqfyky {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  cursor: text;
}

.css-nqlg3w {
  text-align: left;
  position: absolute;
  inset: -5px 0px 0px;
  margin: 0px;
  padding: 0px 8px;
  pointer-events: none;
  border-radius: inherit;
  border-style: solid;
  border-width: 1px;
  overflow: hidden;
  min-width: 0%;
  border-color: rgba(255, 255, 255, 0.23);
}

.css-1oqfyky {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  cursor: text;
}

.css-14lo706 {
  float: unset;
  width: auto;
  overflow: hidden;
  display: block;
  padding: 0px;
  height: 11px;
  font-size: 0.75em;
  visibility: hidden;
  max-width: 100%;
  transition: max-width 100ms cubic-bezier(0, 0, 0.2, 1) 50ms;
  white-space: nowrap;
}

.css-1oqfyky {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  cursor: text;
}

.css-14lo706 {
  float: unset;
  width: auto;
  overflow: hidden;
  display: block;
  padding: 0px;
  height: 11px;
  font-size: 0.75em;
  visibility: hidden;
  max-width: 100%;
  transition: max-width 100ms cubic-bezier(0, 0, 0.2, 1) 50ms;
  white-space: nowrap;
}

*,
::before,
::after {
  box-sizing: inherit;
}

.css-14lo706 > span {
  padding-left: 5px;
  padding-right: 5px;
  display: inline-block;
  opacity: 0;
  visibility: visible;
}

*,
::before,
::after {
  box-sizing: inherit;
}

.css-14lo706 {
  font-size: 0.75em;
  visibility: hidden;
  white-space: nowrap;
}

.css-nqlg3w {
  text-align: left;
  pointer-events: none;
}

.css-1oqfyky {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.4375em;
  letter-spacing: 0.00938em;
  color: rgb(255, 255, 255);
  cursor: text;
}

body {
  color: rgb(255, 255, 255);
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.5;
  letter-spacing: 0.00938em;
}

.hr1 {
  border: 0;
  height: 0.1057rem;
  background: #3d3f3f;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 100px;
}

button {
  margin-bottom: 20px;
}

.world {
  width: 100px;
  height: 100px;
  background-color: #3498db;
  transition: transform 0.5s ease;
}

.world-up {
  transform: translateY(-100px);
}

input {
  margin-top: 20px;
  width: 200px;
  padding: 10px;
  font-size: 16px;
}
</style>