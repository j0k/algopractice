{-# STDLIB_VERSION 3 #-}
{-# CONTENT_TYPE DAPP #-}
{-# SCRIPT_TYPE ACCOUNT #-}

#
# it's not SCALA, it's RIDE.
# but let be scala for syntax coloring
#

let accCreator = this.bytes.toBase58String()
func pref(pr:String, s:String) = pr+s

func inDB(addr:String, mod:String) = {
    match getInteger(this, mod+addr){
        case a:Int => a>0
        case _     => false
    }
}


@Callable(i)
func addU(mod:String, addr:String) = {
    let caller = i.caller.bytes.toBase58String()

    if (inDB(caller, mod) || caller == accCreator)
    then (
        let data = DataEntry(mod+addr, 1)
        WriteSet([data])
    )
    else throw("Can't do that.")
}


# on the next step we can create DB of our own modifiers
