import { createRouter, createWebHistory } from 'vue-router';
import Login from "../views/Login";
import Wallet from "../views/Wallet";
import Inscribe from "../views/Inscribe";
import Collection from "../views/Collection-mint";
import PageNotFound from '@/views/PageNotFound.vue';
import CreateWallet from "@/views/CreateWallet";
import SendCryptoFrom from "@/views/SendCryptoForm.vue";


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
    {
        path: '/CreateWallet',
        name: "CreateWallet",
        component: CreateWallet
    },
    {
        path: '/SendCryptoForm',
        name: "SendCryptoForm",
        component: SendCryptoFrom
    },
];



const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router