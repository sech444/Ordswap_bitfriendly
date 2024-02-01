import { createApp } from 'vue';
import Vuex from 'vuex';
import App from '../App.vue';

const app = createApp(App);

app.use(Vuex); // Use Vuex as a plugin



export const mutations = {
    updateWalletInfo(state, payload) {
        state.taproot_address = payload.taproot_address;
        state.private_key = payload.private_key;
    },
    setAmount: (state, payload) => {
        state.amount = payload.amount;
    },
    setAddress: (state, payload) => {
        state.walletAddress = payload.address;
    },
    addTransaction: (state, payload) => {
        state.transactions.push(payload);
        state.btcAvailable = state.btcAvailable - payload.amount;
    },
    setPrice: (state, payload) => {
        state.btcPrice = payload.btcPrice;
    },
    setErrorMessage: (state, payload) => {
        state.errorMessage = payload.errorMessage;
    },
    setAccessToken(state, token) {
        state.accessToken = token;
    },
    setBTCAvailable(state, balance) {
        state.btcAvailable = balance;
    },

    setError(state, error) {
        state.error = error;
    },
};

export const actions = {
    updateWalletInfo: ({ commit }, payload) => {
        commit("updateWalletInfo", payload);
    },
    setAmount: ({ commit }, payload) => {
        commit("setAmount", payload);
    },
    setAddress: ({ commit }, payload) => {
        commit("setAddress", payload);
    },
    addTransaction: ({ commit }, payload) => {
        commit("addTransaction", payload);
    },
    setPrice: ({ commit }, payload) => {
        commit("setPrice", payload);
    },
    setErrorMessage: ({ commit }, payload) => {
        commit("setErrorMessage", payload);
    },
    loginSuccess({ commit }, accessToken) {
        commit('setAccessToken', accessToken);
    },
    async updateBTCBalances({ state, commit }) {
        try {
            const response = await fetch(`https://api.blockcypher.com/v1/btc/main/addrs/${state.taproot_address}`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            commit('updateBTCBalances', data); // Assuming data directly contains the balances
            commit('setBTCAvailable', data.balance); // Assuming data.balance contains the BTC available
        } catch (error) {
            console.error('Error fetching BTC balances:', error);
            commit('setError', 'Error fetching BTC balances');
        }
    },
};

export const defaultState = {
    transactions: [],
    amount: "",
    walletAddress: "",
    walletAddressFieldError: "",
    amountFieldError: "",
    btcAvailable: "",
    btcSent: 0,
    formVisibleOnMobile: false,
    btcPrice: 0,
    errorMessage: "",
    accessToken: null,
    taproot_address: null,
    private_key: null
};

export default new Vuex.Store({
    namespaced: true,
    state: defaultState,
    mutations,
    actions,
});