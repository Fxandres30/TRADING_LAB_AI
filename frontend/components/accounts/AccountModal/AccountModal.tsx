"use client";

import "./AccountModal.css";

import { useEffect, useState } from "react";

import { getAccounts } from "./services";

import { Account } from "./types";

import AccountDetectedList from "./AccountDetectedList";

import BrokerManualList from "./BrokerManualList";

type Props = {

    open: boolean;

    onClose: () => void;

};

export default function AccountModal({

    open,

    onClose,

}: Props) {

    const [accounts, setAccounts] = useState<Account[]>([]);

    useEffect(() => {

        if (!open) return;

        getAccounts()
            .then(setAccounts)
            .catch(() => setAccounts([]));

    }, [open]);

    // =====================================
    // CONECTAR CUENTA
    // =====================================

    const handleConnect = async (account: Account) => {

        console.log("Conectar:", account);

        // Aquí luego llamaremos al backend
        // await connectAccount(account.id);

        onClose();

    };

    if (!open) return null;

    return (

        <div className="accountOverlay">

            <div className="accountModal">

                <div className="modalHeader">

                    <div>

                        <h2>Conectar Broker</h2>

                        <p>

                            Selecciona una cuenta detectada o conecta un broker.

                        </p>

                    </div>

                    <button

                        className="close"

                        onClick={onClose}

                    >

                        ✕

                    </button>

                </div>

                <h3 className="sectionTitle">

                    Cuentas detectadas

                </h3>

                <div className="brokerList">

                    <AccountDetectedList
                        accounts={accounts}
                        onConnect={handleConnect}
                    />

                </div>

                <h3 className="sectionTitle">

                    Conectar manualmente

                </h3>

                <div className="brokerList">

                    <BrokerManualList />

                </div>

            </div>

        </div>

    );

}