"use client";

import "./AccountModal.css";

const API =
    process.env.NEXT_PUBLIC_API_URL ??
    "http://127.0.0.1:8000/api";

type Props = {

    open: boolean;

    onClose: () => void;

};

function connectBroker(broker: string) {

    switch (broker) {

        case "deriv":

            window.location.href =
                `${API}/oauth/deriv/login`;

            break;

        default:

            alert("Broker no disponible");

    }

}

export default function AccountModal({

    open,

    onClose,

}: Props) {

    if (!open) return null;

    return (

        <div className="accountOverlay">

            <div className="accountModal">

                <div className="modalHeader">

                    <div>

                        <h2>

                            Conectar Broker

                        </h2>

                        <p>

                            Agrega una cuenta de trading para comenzar.

                        </p>

                    </div>

                    <button
                        className="close"
                        onClick={onClose}
                    >

                        ✕

                    </button>

                </div>

                <div className="brokerList">

                    {/* DERIV */}

                    <button
                        className="brokerCard"
                        onClick={() => connectBroker("deriv")}
                    >

                        <img
                            src="/brokers/deriv.svg"
                            alt="Deriv"
                        />

                        <div className="brokerInfo">

                            <strong>

                                Deriv

                            </strong>

                            <span>

                                CFDs · Forex · Options · Multipliers

                            </span>

                        </div>

                        <div className="brokerAction">

                            Conectar →

                        </div>

                    </button>

                </div>

            </div>

        </div>

    );

}