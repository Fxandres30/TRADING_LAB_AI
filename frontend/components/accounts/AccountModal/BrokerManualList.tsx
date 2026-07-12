import BrokerManualCard from "./BrokerManualCard";

const brokers = [

    {

        id: "deriv",

        name: "Deriv",

        description: "OAuth Oficial",

        icon: "/brokers/deriv.svg"

    },

    {

        id: "mt5",

        name: "MetaTrader 5",

        description: "Login Manual",

        icon: "/brokers/mt5.svg"

    },

    {

        id: "binance",

        name: "Binance",

        description: "API Key",

        icon: "/brokers/binance.svg"

    }

];

export default function BrokerManualList() {

    return (

        <>

            {brokers.map(broker => (

                <BrokerManualCard

                    key={broker.id}

                    {...broker}

                />

            ))}

        </>

    );

}