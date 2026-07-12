import { Account } from "./types";

import "./AccountDetectedCard.css";

type Props = {
    account: Account;
    onConnect: (account: Account) => void;
};

export default function AccountDetectedCard({
    account,
    onConnect,
}: Props) {

    return (

        <div className="brokerCard">

            <div className="brokerHeader">

                <div>

                    <h3>{account.company}</h3>

                    <span className="brokerBadge">
                        {account.broker.toUpperCase()}
                    </span>

                </div>

                <div
                    className={
                        account.connected
                            ? "status connected"
                            : "status disconnected"
                    }
                >
                    {account.connected ? "● Conectado" : "● Desconectado"}
                </div>

            </div>

            <div className="brokerBody">

                <div className="info">
                    <label>Propietario</label>
                    <span>{account.name}</span>
                </div>

                <div className="info">
                    <label>Cuenta</label>
                    <span>{account.login}</span>
                </div>

                <div className="info">
                    <label>Servidor</label>
                    <span>{account.server}</span>
                </div>

                <div className="info">
                    <label>Moneda</label>
                    <span>{account.currency}</span>
                </div>

                <div className="info">
                    <label>Balance</label>
                    <span>
                        {account.balance.toLocaleString()} {account.currency}
                    </span>
                </div>

                <div className="info">
                    <label>Equity</label>
                    <span>
                        {account.equity.toLocaleString()} {account.currency}
                    </span>
                </div>

            </div>

            <div className="brokerFooter">

                <button
                    className="connectButton"
                    onClick={() => onConnect(account)}
                >
                    Conectar
                </button>

            </div>

        </div>

    );

}