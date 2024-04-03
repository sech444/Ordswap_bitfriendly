<template>
  <div class="transactions-container ">
    <h3 class="section-title">Transactions</h3>
    <div class="transactions-item-containter" >
      <p v-if="transactions.length  < 1">No transactions</p>

      <ul
        class=""
        v-for="transaction in transactions"
        :key="transaction.id"
        v-else
      >
        <li class="transactions-item">
          <p>
            Amount:
            <span class="bold">{{ transaction.amount }} BTC</span>
          </p>
          <p>
            To:
            <span class="bold">{{ transaction.address }}</span>
          </p>
          <p class="transaction-type bold">Sent</p>
        </li>
      </ul>
      <!-- {{testUsers}} -->
    </div>
  </div>
</template>

<script>
export default {
  name: "TransactionList",
  data() {
    return {
      transactions: this.$store.state.transactions
    };
  }
};
</script>

<style lang="scss" scoped>
.transactions-item {
  padding: 1.2rem;
  background: #999;
  font-size: 2.3rem;
  min-width: 60rem;
  font-weight: 600;
  color: #000;
  
}

.transactions-item p .bold {
  font-weight: 600;
}

.transaction-type {
  position: absolute;
  right: 0px;
  top: 0px;
  text-transform: uppercase;
  font-size: 1rem;
  padding: 5px;
  background: #5d7087;
  color: #ffffff;
  font-size: 1.3rem;
  
}

.transactions-item-list {
  padding: 0;
  margin: 0;
  border-right: 5px;
  border-top: 2px;
  border-left: 1px;
  border-bottom: 1px;
  border-color: #e7e7e7;
  border-style: solid;
  list-style: none;
  color: #fff;
}

.transactions-container {
  max-width: 40vw;
  position: relative;
  top: 20rem;
}

.transactions-item-list:first-child {
  border: 1px solid #e7e7e7;
}
.right-div {
    position: absolute;
    right: 40%;
    //top: 0;
}

.left-div {
    position: absolute;
    left: 10px;
    top: 40px;
    
}

@media only screen and (max-width: 768px) {
  .transactions-container {
    position: absolute;
    top: auto;
    z-index: 10;
    max-width: 80vw;
    margin: 0 20px -50px;
   transform: translate(0, -50%);
   
  }
 
 
}
</style>
