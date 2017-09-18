как я хотел бы чтобы выглядила архитектура торговой платформы, в максимально свободном стиле

-------
Strategies, Strategie

ms = myStrategie

ms.kafka <- Kafka.subscribe(OPT['EXCH'] + '-' + OPT['PAIR'])
ms.ws <- Exchange(OPT['EXCH']).websocket.subscribe()
ms.command = Exchange(OPT['EXCH']).rest


ms {
    fun analyze(){
        self.{asks,bids} = ms.kafks.{get('asks'), get('bids')}
       ... analyzing
    }

    fun place_order(){
        ...
    }

    fun execute(){
        :: def return
        :: ask:price[].len > 0
        price = ask.price[].max()
        ms.command.place_order(4500, 0.5);
    }

    fun workflow(){
        .asks = !kafka.asks
        .bids = !kafka.bids
    }
}

fun main {
    ms.workflow() on timer(1000ms).run(){
       on.onlyOneTask = True
    }
}
