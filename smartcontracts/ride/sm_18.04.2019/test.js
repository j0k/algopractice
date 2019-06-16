const wid0Seed   = "mushroom congress reduce nuclear search puzzle mesh coach tackle across process promote"
const wid1Seed   = "help grace turkey embark expect supply track holiday wasp hub injury empty"
const wid2Seed   = env.accounts[2]
// shiver action fault evidence napkin hollow critic stairs knee piece toast tail

const wid0Addr = address(wid0Seed)
const wid0PubKey = publicKey(wid0Seed)

const wid1Addr = address(wid1Seed)
const wid1PubKey = publicKey(wid1Seed)

const wid2Addr = address(wid2Seed)
const wid2PubKey = publicKey(wid2Seed)

describe('Wallet test suite', () => {
    it('deploys dapp script', async function(){
        const ttx = setScript({ script: compile(file("accountScript_1.ride")), fee:2000000}, wid0Seed)
        await broadcast(ttx)
        await waitForTx(ttx.id)
    })

    it('add user', async function(){
        const ttx = invokeScript({
            dappAddress: wid0Addr,
            call:{function:"addUser",args:[{type: "string", value: "_c++_"}, {type: "string", value: wid1Addr}]}},
            wid0Seed
            )
        await broadcast(ttx)
        await waitForTx(ttx.id)
    })

    it('add user super', async function(){
        const ttx = invokeScript({
            dappAddress: wid0Addr,
            call:{function:"addUser",args:[{type: "string", value: "_super_"}, {type: "string", value: wid1Addr}]}},
            wid0Seed
            )
        await broadcast(ttx)
        await waitForTx(ttx.id)
    })

    it('add 10 random users', async function(){
        for (var i = 0; i< 100; i++){
            var randPref = String(Math.random())
            const ttx = invokeScript({
                dappAddress: wid0Addr,
                call:{function:"addUserWithValue",args:[{type: "string", value: randPref}, {type: "string", value: wid1Addr}, {type:"integer", value:i}]}},
                wid0Seed
                )
            await broadcast(ttx)
            await waitForTx(ttx.id)
            console.log(i)
        }
    })

    it('funds user_1 account', async function(){
        const ttx = transfer({ amount: 100000000, recipient: wid1Addr , fee:5000000}, wid0Seed)
        await broadcast(ttx)
        await waitForTx(ttx.id)
    })

    it('sendWaves', async function(){
        const ttx = invokeScript({
            dappAddress: wid0Addr,
            call:{function:"sendWaves", args:[{type: "string", value: "3Msp3NwoP2r2D7sbiv8tsqq5LYnqHUYVCWX"}, {type: "integer", value: 50000}]}},
            wid1Seed
            )
        await broadcast(ttx)
        await waitForTx(ttx.id)
    })

})
