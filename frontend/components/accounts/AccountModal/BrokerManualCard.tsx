import { connectBroker } from "./services";

type Props = {

    id: string;

    icon: string;

    name: string;

    description: string;

};

export default function BrokerManualCard({

    id,

    icon,

    name,

    description,

}: Props) {

    return (

        <button

            className="brokerCard"

            onClick={() => connectBroker(id)}

        >

            <img

                src={icon}

                alt={name}

            />

            <div className="brokerInfo">

                <strong>{name}</strong>

                <span>{description}</span>

            </div>

            <div className="brokerAction">

                Conectar →

            </div>

        </button>

    );

}