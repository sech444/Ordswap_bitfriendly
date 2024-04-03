<template>
  <div style="padding: 10px;">
    <div>
      <h3 class="section-title">SEND BTC</h3>
      <img src="/Bitcoin-Logo-23.png" alt="Bitcoin logo">
    </div>
    <div>
      <input
        type="text"
        ref="walletInput"
        @input="handleAddressChange"
        @focus="focusInput('walletInput')"
        v-model="addressInput"
        class="input input-spacing wallet-input"
        placeholder="Address or Name (Bitfriendly Creator)"
      />

      <h1 class="send-text">
        <span class="css-Portfolio">Portfolio Value :</span
        ><span class="css-formatted1">{{ formattedBtcAvailable }}</span
        ><span class="css-Portfoliobtc"> BTC </span>
      </h1>
      <h1 class="send-text-2">
        <span class="css-liquidity">Unconfirmed BTC : </span
        ><span class="css-formatted2">{{ formattedBtcAvailable }}</span
        ><span class="css-liquiditybtc"> BTC </span>
      </h1>
      <h1 class="send-text-3">
        <span class="css-inscription">Liquidity Value : </span
        ><span class="css-formatted3">{{ formattedBtcAvailable }}</span
        ><span class="css-inscriptionbtc"> BTC </span>
        <span class="SafeToSend">Safe To Send</span>
        <button class="max-button">MAX</button>
      </h1>

      <input
        placeholder="Amount"
        ref="amountInput"
        @focus="focusInput('amountInput')"
        class="input input-spacing btc-input"
        type="text"
        @keydown.enter="handleSendClick"
        @input="handleAmountChange"
        v-model="amountInput"
      />
    </div>
    <div class="button-transaction-container">
      <div clas="button-container-left">
        <p class="error-status">{{ errorMsgText }}</p>
        <p class="transaction-value-text transaction-value-spacing">
          Transaction Value in USD:
          <span v-if="valueInUSD" class="bold">{{ valueInUSD }} $</span>
        </p>
      </div>
    </div>
   
    <div>
      <button v-if="!showContent" @click="handleSendClick" class="button">NEXT</button>
    </div>
    <div v-if="showContent" style="background-color: azure; min-width: 20vw; min-height: 10vw;">
      <!-- Your content to be shown -->
      <h3>Gas Fee: {{ selectedGasFee }} </h3>
      <h3>Service Fee: {{ serviceFee }} sat/vB</h3>
      <h3>Amount: {{ amountInput }} BTC</h3>
      <h1>Total Amount: {{ totalAmount }} BTC</h1>
      <button @click="handleSubmit()" class="sendbutt">Send</button>
      <button @click="cancelTransaction()" class="sendbutt">Cancel</button>
    </div>

    <!-- Include the PriceTrackerWidget component and pass selectedGasFee as a prop -->
    <PriceTrackerWidget v-if="!showContent" @feeSelected="handleFeeUpdate" />
  </div>
</template>

<script>
import axios from 'axios';
import { computed, inject } from 'vue';
import { useStore } from 'vuex';
import PriceTrackerWidget from './PriceTrackerWidget.vue';

export default {
  name: "SendCryptoForm",
  components: { PriceTrackerWidget },
  computed: {
    valueInUSD() {
      if (!this.amountInput) return "0";
      return (this.amountInput * this.$store.state.btcPrice).toFixed(2);
    },
   
    errorMsgText() {
      return this.$store.state.errorMessage;
    },
    btcAvailable() {
      return this.$store.state.btcAvailable;
    },
    formattedBtcAvailable() {
      return this.$store.state.btcAvailable.toFixed(6);
    },
    serviceFee() {
      return (this.amountInput * 0.17).toFixed(6); // Example service fee calculation (0.17 sat/vB of the amount)
    },
    totalAmount() {
      const amount = parseFloat(this.amountInput);
      const selectedGasFee = parseFloat(this.selectedGasFee) || 0; 
      const total = amount + parseFloat(this.selectedGasFee) + parseFloat(this.serviceFee);
      return total.toFixed(6);
    },
  },
  data() {
    return {
      amountInput: 0,
      addressInput: "",
      isFiveColumns: false, // New property for five-column 
      showContent: false, // Initially content is hidden
      gasFee: "", // Define a data property for the gas fee
      selectedGasFee: null, // Store the selected fee when NEXT is clicked
    };
  },
  methods: {
    focusInput(ref) {
      this.$refs[ref].select();
    },
    resetForm() {
      this.$store.dispatch("setErrorMessage", { errorMessage: "" });
      this.amountInput = 0;
      this.addressInput = "";
    },
    validateForm() {
      if (this.amountInput > this.$store.state.btcAvailable) {
        return "You don't have sufficient funds.";
      }
      if (!this.amountInput) {
        return "Please enter the correct amount.";
      }
      if (this.amountInput > this.$store.state.btcAvailable) {
        return "You don't have sufficient funds.";
      }
      return;
    },
    private_key() {
        return this.$store.state.private_key;
      },
    handleFeeUpdate(fee) {
      // Update selectedGasFee when a new fee is selected
      this.selectedGasFee = fee;
    },
    handleSendClick() {
      const validateResult = this.validateForm();
      if (!this.selectedGasFee) {
       this.$store.dispatch("setErrorMessage", { errorMessage: "Please select a gas fee." });
          return;
      }
      if (validateResult) {
        this.$store.dispatch("setErrorMessage", { errorMessage: validateResult });
        return;
      }
      this.showContent = true; // Show the transaction review section
    },
    cancelTransaction() {
      // Logic to cancel the transaction
      this.showContent = false; // Hide the review section
      this.resetForm(); // Reset the form
    },
    createTransaction() {
      this.$store.dispatch("addTransaction", {
        amount: parseFloat(this.amountInput),
        address: this.addressInput,
        id: this.generateId(),
      });
    },
    async handleSubmit() {
    // Important: You'll replace this with your actual blockchain interaction logic
    const api = axios.create({
        baseURL: 'http://127.0.0.1:5000',  // Update with your FastAPI backend address
    });

    const formData = {
        private_key: this.privateKey,
        addr_to: this.addressInput,
        amount: this.amountInput,
        gasfee: this.selectedGasFee
    };

    try {
        // Send data to your backend or directly interact with the blockchain
        const response = await api.post('/users/users/', formData);
        createTransaction();
        console.log("Transaction Result:", response.data);
    } catch (error) {
        console.error("Transaction Error:", error);
    }
  },
    generateId() {
      const transactionsNumber = this.$store.state.transactions.length;
      return transactionsNumber < 1 ? 0 : this.$store.state.transactions[transactionsNumber - 1].id + 1;
    },
    handleAmountChange(event) {
      this.amountInput = event.target.value;
      this.$store.dispatch("setAmount", { amount: this.amountInput });
    },
    handleAddressChange(event) {
      this.addressInput = event.target.value;
      this.$store.dispatch("setAddress", { address: this.addressInput });
    },
  },
};
</script>



<style lang="scss" scoped>


.sendbutt {
  font-size: 1.3vw;
  margin: 3rem 0.4rem;
  background-color: #F7931A !important;
  border: none;
  color: #fff;
  border-radius: 14px;
  min-width: 10vw;
  max-width: 10vw;
}
img {
  max-width:20%; 
  min-width: 20%;
  padding-bottom: 10px;
}

.button-send {
  background-color: #c5c0c0 !important;
  border: none;
  color: #fff;
  font-weight: 300;
  font-size: 2rem;
  padding: 8px 3px;
  border-radius: 3px;
  outline: none;
  top: 95%;
  transition: all 0.5s;
}


.button {
  background-color: #F7931A !important;
  border: none;
  color: #fff;
  font-weight: 300;
  font-size: 1.7rem;
  padding: 8px;
  border-radius: 13px;
  outline: none;
  top: 96%;
  transition: all 0.5s;
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

.error-status {
  align-self: flex-start;
  color: #db2828;
  font-size: 1.8rem;
  font-style: italic;
  height: 8px;
  font-weight: bold;
}
.send-text {
  position: flex-start;
  color: #c5c0c0;
  padding: 5px;
  max-width: 30vw;
  min-width: 35vw;
  margin-left: 6.8vw;
  left: 50%;
  transform: translateX(-50%);
}
.css-Portfolio{
  position: fixed;
  top: 50% !important;
  left: 44%;
  word-spacing: 5%;
  transform: translate(-50%, -50%);
}
.css-formatted1{
  position: fixed;
  top: 50%;
  right: -50%;
  transform: translate(-50%, -50%);
}
.css-Portfoliobtc{
  position: fixed;
  top: 51%;
  left: 150%;
  transform: translate(-50%, -50%);

}
.css-liquidity{
  position: fixed;
  top: 40%  !important;
  left: 45.8%;
  padding-top: 30px;
  transform: translate(-50%, -50%);
}
.css-formatted2{
  position: fixed;
  top: 50%;
  right: -66.4%;
  padding-top: 30px;
  transform: translate(-50%, -50%);
}
.css-formatted3{
  position: fixed;
  top: 28%;
  right: -66.4%;
  padding-top: 20px;
  transform: translate(-50%, -50%);
}
.max-button{
  position: fixed;
  top: 31%;
  right: -42.4%;
  padding-top: 20px;
  transform: translate(-50%, -50%);
  font-size: 0.9vw;
  background-color: transparent !important;
  border: none;
} 
.css-liquiditybtc{
  position: fixed;
  top: 38%;
  left: 166.5%;
  padding-top: 30px;
  transform: translate(-50%, -50%);
}
.css-inscriptionbtc{
  position: fixed;
  top: 22%;
  left: 166.5%;
  padding-top: 20px;
  transform: translate(-50%, -50%);
}

.css-inscription{
  position: fixed;
  top: 70% !important;
  left: 42.5%;
  padding-bottom: 35px;
  transform: translate(-50%, -50%);
}

.send-text-2{
  position:flex-start;
  color: #c5c0c0;
  padding: 25px;
  max-width: 30vw;
  min-width: 30vw;
  margin-left: 6.8vw;
  left: 50%;
  transform: translateX(-50%);
}
.send-text-3{
  position:flex-start;
  color: #c5c0c0;
  padding-bottom: 50px;
  max-width: 30vw;
  min-width: 30vw;
  margin-left: 7vw;
  left: 50%;
  transform: translateX(-50%);

}
.button-transaction-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 5.5rm;
}

.transaction-value-text {
  margin: 0;
  font-size: 2rem;
  color: #91918e;
}

.transaction-value-spacing {
  margin-right: 10px;
  margin-bottom: 0px;
}

.send-crypto-form {
    padding: 20px;
    font-size: 1.9rem;
    background-color: #123456;
    box-shadow: 0.8px 2px 2px 0.8px #fffefe54;
    margin-bottom: 20px;
    border-radius: 3px;
    max-width: 30vw;
    border-radius: 30px;
    color: #e7e7e7;
  }

.input {
  border: none;
  color: #fff;
  font-size: 2.8rem;
  font-weight: 600;
  line-height: 1rem;
  border-bottom: 1px solid #e7e7e7;
  background-color: #91918e;
  padding: 5px 15px;
}

.input:focus {
  transition: all 0.2s;
  border-bottom: 1px solid #fcd535;
  /* box-shadow: 0.8px 0.8px 0.8px 0.8px #8888889e; */
}

.input::selection {
  background: #91918e;
  color: #fff;
  //font-size: 1rem;
}

.input::placeholder {
  font-style: italic;
  color: #fff;
  font-size: 1.3rem;
}

.SafeToSend{
  color: #F7931A;
  position: fixed;
  top: 80% !important;
  left: 35%;
  font-size: 0.8vw;
  transform: translate(-50%, -50%);
}
.input-spacing {
  margin-bottom: 20px;
  width: 100%;
}

.bold {
  font-weight: 700;
}

input:focus {
  outline: #fff;
}

/* Your original CSS code here... */

/* For devices smaller than 600px */
@media only screen and (max-width: 600px) {
    .send-crypto-form {
    max-width: 80vw;
  }
  .send-text {
  position: flex-start;
  color: #c5c0c0;
  padding: 5px;
  max-width: 80vw;
  min-width: 80vw;
  //margin-left: 4.8vw;
  left: 50%;
  transform: translateX(-50%);
}
.css-Portfolio{
  position: fixed;
  top: 45% !important;
  left: 59%;
  word-spacing: 5%;
  transform: translate(-50%, -50%);
}
.css-formatted1{
  position: fixed;
  top: 50%;
  right: -37%;
  transform: translate(-50%, -50%);
}
.css-Portfoliobtc{
  position: fixed;
  top: 51%;
  left: 135%;
  transform: translate(-50%, -50%);

}
.css-liquidity{
  position: fixed;
  top: 40%  !important;
  left: 60%;
  padding-top: 30px;
  transform: translate(-50%, -50%);
}
.css-formatted2{
  position: fixed;
  top: 50%;
  right: -20%;
  padding-top: 25px;
  transform: translate(-50%, -50%);
}
.css-formatted3{
  position: fixed;
  top: 28%;
  right: -20.4%;
  padding-top: 20px;
  transform: translate(-50%, -50%);
}
.max-button{
  position: fixed;
  top: 29%;
  right: 4.4%;
  padding-top: 20px;
  transform: translate(-50%, -50%);
  font-size: 2vw;
  background-color: transparent !important;
  border: none;
} 
.css-liquiditybtc{
  position: fixed;
  top: 38%;
  left: 118.5%;
  padding-top: 32px;
  transform: translate(-50%, -50%);
}
.css-inscriptionbtc{
  position: fixed;
  top: 22%;
  left: 118.5%;
  padding-top: 25px;
  transform: translate(-50%, -50%);
}

.css-inscription{
  position: fixed;
  top: 69% !important;
  left: 57.5%;
  padding-bottom: 32px;
  transform: translate(-50%, -50%);
}

.SafeToSend{
  color: #F7931A;
  position: fixed;
  top: 78% !important;
  left: 50%;
  font-size: 2.4vw;
  transform: translate(-50%, -50%);
}

.send-text-2{
  position:flex-start;
  color: #c5c0c0;
  //padding: 25px;
  max-width: 100vw;
  min-width: 100vw;
 // margin-left: 6.8vw;
  left: 50%;
  transform: translateX(-50%);
}
.send-text-3{
  position:flex-start;
  color: #c5c0c0;
  padding-bottom: 50px;
  max-width: 100vw;
  min-width: 100vw;
  //margin-left: 7vw;
  left: 50%;
  transform: translateX(-50%);

}
img {
  max-width:25%; 
  min-width: 25%;
  padding-bottom: 10px;
}
.sendbutt {
  font-size: 6.3vw;
  margin: 3rem 0.4rem;
  background-color: #F7931A !important;
  border: none;
  color: #fff;
  border-radius: 14px;
  min-width: 30vw;
  max-width: 30vw;
}
}




</style>