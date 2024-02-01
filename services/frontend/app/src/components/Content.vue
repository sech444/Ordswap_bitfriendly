<template>
  <div class="">
    <div class="content-container">
      <div class="row">
        <div class="">
          <SendCryptoFormbtc/>
          <SpendingStatusWidget/>
          <PriceTrackerWidget/>
        </div>
        <!-- <div class="txList">
          <TransactionList/>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import SendCryptoFormbtc from "./SendCryptoFormbtc";
import TransactionList from "./TransactionList";
import PriceTrackerWidget from "./PriceTrackerWidget";
import SpendingStatusWidget from "./SpendingStatusWidget";

export default {
  name: "Content",
  components: {
    SendCryptoFormbtc,
    TransactionList,
    PriceTrackerWidget,
    SpendingStatusWidget
  }
};
</script>

<style lang="scss" scoped>
h3 {
  color: #5d7087;
}

@media only screen and (max-width: 1700px) {
  .txList{
    display: block;

  }
}
</style>


