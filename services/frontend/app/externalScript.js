const bip39 = require('bip39');
const HDKey = require('hdkey');
const Buffer = require('buffer/').Buffer; // or use a polyfill if necessary

function generateKeys() {
    const mnemonic = bip39.generateMnemonic();
    let phrase = mnemonic;
    let seedBuffer = bip39.mnemonicToSeedSync(phrase);

    const seed = seedBuffer; //'a0c42a9c3ac6abf2ba6a9946ae83af18f51bf1c9fa7dacc4c92513cc4dd015834341c775dcd4c0fac73547c5662d81a9e9361a0aac604a73a321bd9103bce8af';
    const hdkey = HDKey.fromMasterSeed(Buffer.from(seed, 'hex'));

    const privateExtendedKey = hdkey.privateExtendedKey;
    const publicExtendedKey = hdkey.publicExtendedKey;

    return {
        phrase,
        privateExtendedKey,
        publicExtendedKey
    };
}

module.exports = generateKeys();