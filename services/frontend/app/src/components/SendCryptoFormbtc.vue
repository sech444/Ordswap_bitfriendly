<template>
  <div>
    <h3 class="section-title">SEND BITCOIN</h3>
    <div class="send-crypto-form">
      <div>
        <input
          type="text"
          ref="walletInput"
          @input="handleAddressChange"
          @focus="focusInput('walletInput')"
          v-model="addressInput"
          class="input input-spacing wallet-input"
          placeholder="Wallet Address"
        />
      </div>

      <div>
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

        <button @click="handleSendClick" class="button">SEND</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SendCryptoForm",
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

  },
  data() {
    return {
      amountInput: 0,
      addressInput: "",
    };
  },
  methods: {
    focusInput(ref) {
      this.$refs[ref].select();
    },

    resetForm() {
      this.$store.dispatch("setErrorMessage", {
        errorMessage: "",
      });

      this.amountInput = 0;
      this.addressInput = "";
    },

    validateForm() {
      if (!this.addressInput) {
        return "Please enter the correct address.";
      }

      if (!this.amountInput) {
        return "Please enter the correct amount.";
      }

      if (this.amountInput > this.$store.state.btcAvailable) {
        return "You dont have sufficent funds.";
      }

      return;
    },

    handleSendClick() {
      const validateResult = this.validateForm();

      if (validateResult) {
        this.$store.dispatch("setErrorMessage", {
          errorMessage: validateResult,
        });

        return;
      }

      this.createTransaction();
      this.resetForm();
    },

    createTransaction() {
      this.$store.dispatch("addTransaction", {
        amount: parseFloat(this.amountInput),
        address: this.addressInput,
        id: this.generateId(),
      });
    },

    generateId() {
      const transactionsNumber = this.$store.state.transactions.length;

      if (transactionsNumber < 1) {
        return 0;
      }

      return this.$store.state.transactions[transactionsNumber - 1].id + 1;
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
.button {
  background-color: #FFD700;
  border: none;
  color: #fff;
  font-weight: 300;
  font-size: 2rem;
  padding: 8px 23px;
  border-radius: 3px;
  outline: none;
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

.button-transaction-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 2rm;
}

.transaction-value-text {
  margin: 0;
  font-size: 2.0rem;
}

.transaction-value-spacing {
  margin-right: 10px;
  margin-bottom: 0px;
}

.send-crypto-form {
  padding: 20px;
  font-size: 1.9rem;
  background-color: black;
  box-shadow: 0.8px 2px 2px 0.8px #88888854;
  margin-bottom: 20px;
  border-radius: 3px;
  max-width: 30vw;
  border-radius: 30px;
  color: #e7e7e7;
}

.input {
  border: none;
  color: #838383;
  font-size: 1.9rem;
  font-weight: 600;
  line-height: 1rem;
  border-bottom: 1px solid #e7e7e7;
  padding: 5px 15px;
}

.input:focus {
  transition: all 0.2s;
  border-bottom: 1px solid #fcd535;
  /* box-shadow: 0.8px 0.8px 0.8px 0.8px #8888889e; */
}

.input::selection {
  background: #000;
  color: #fff;
}

.input::placeholder {
  font-style: italic;
  color: #000;
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

@media only screen and (max-width: 968px) {
  .send-crypto-form {
    max-width: 80vw;
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

</style>