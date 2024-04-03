import { createRouter, createWebHistory } from 'vue-router';
import Login from "../views/Login";
import Wallet from "../views/Wallet";
import Inscribe from "../views/Inscribe";
import Collection from "../views/Collection-mint";
import PageNotFound from '@/views/PageNotFound.vue';
// import CreateWallet from "@/views/CreateWallet";
import Restorewallet from "@/views/Restorewallet";
import SendCryptoFrom from "@/views/SendCryptoForm.vue";
import Createpassword from "@/views/Createpassword.vue";
import Passworldpass from "@/views/Passworldpass.vue";
import SecretPhraseDisplay from "@/views/SecretPhraseDisplay.vue";


const routes = [{
        path: '/',
        name: "home",
        component: Login
    },
    {
        path: "/wallet",
        name: "wallet",
        component: Wallet
    },
    {
        path: "/inscribe",
        name: "inscribe",
        component: Inscribe
    },
    {
        path: "/Collection-mint",
        name: "collection",
        component: Collection
    },
    {
        path: '/:catchAll(.*)*',
        name: "PageNotFound",
        component: PageNotFound,
    },
    // {
    //     path: '/CreateWallet',
    //     name: "CreateWallet",
    //     component: CreateWallet
    // },
    {
        path: '/SendCryptoFrom',
        name: "SendCryptoFrom",
        component: SendCryptoFrom
    },
    {
        path: '/Restorewallet',
        name: "Restorewallet",
        component: Restorewallet
    },
    {
        path: '/Restorewallet',
        name: "Restorewallet",
        component: Restorewallet
    },
    {
        path: '/Createpassword',
        name: "Createpassword",
        component: Createpassword
    },
    {
        path: '/secret-phrase-display',
        name: "SecretPhraseDisplay",
        component: SecretPhraseDisplay
    },
    {
        path: '/Passworldpass',
        name: "Passworldpass",
        component: Passworldpass
    },


];



const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router