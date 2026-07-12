"use client";

import "./Topbar.css";

import { useState } from "react";

import AccountModal from "@/components/accounts/AccountModal/AccountModal";

import {

    Activity,
    Bell,
    Clock3,
    Wifi,
    ShieldCheck,
    DollarSign,
    UserCircle2,
    Settings,
    Wallet,
    Layers3,

} from "lucide-react";

export default function Topbar() {

    const [openAccount, setOpenAccount] = useState(false);

    // =====================================================
    // TEMPORAL
    // Después vendrá desde el backend
    // =====================================================

    const dashboard = {

        broker: "MetaTrader 5",

        account: "Deriv-Demo",

        accounts: 3,

        balance: 110954.22,

        equity: 110954.22,

        risk: "1%",

        bot: true,

        user: "Andrés Felipe"

    };

    return (

        <>

            <header className="topbar">

                {/* ====================================== */}
                {/* CENTRO */}
                {/* ====================================== */}

                <div className="topbarCenter">

                    <div className={`status ${dashboard.bot ? "online" : ""}`}>

                        <Activity size={15} />

                        {dashboard.bot ? "BOT ONLINE" : "BOT OFFLINE"}

                    </div>

                    <div className="selector">

                        <Wifi size={15} />

                        <span>

                            Broker

                        </span>

                        <strong>

                            {dashboard.broker}

                        </strong>

                    </div>

                    <div className="selector">

                        <UserCircle2 size={15} />

                        <span>

                            Cuenta

                        </span>

                        <strong>

                            {dashboard.account}

                        </strong>

                    </div>

                    <div className="selector">

                        <Layers3 size={15} />

                        <span>

                            Cuentas

                        </span>

                        <strong>

                            {dashboard.accounts}

                        </strong>

                    </div>

                    <button

                        className="selector add"

                        onClick={() => setOpenAccount(true)}

                    >

                        + Agregar Cuenta

                    </button>

                    <div className="status">

                        <Wallet size={15} />

                        <span>

                            Balance

                        </span>

                        <strong>

                            {dashboard.balance.toLocaleString("en-US", {

                                minimumFractionDigits: 2,

                                maximumFractionDigits: 2,

                            })} USD

                        </strong>

                    </div>

                    <div className="status">

                        <DollarSign size={15} />

                        <span>

                            Equity

                        </span>

                        <strong>

                            {dashboard.equity.toLocaleString("en-US", {

                                minimumFractionDigits: 2,

                                maximumFractionDigits: 2,

                            })} USD

                        </strong>

                    </div>

                    <div className="status">

                        <ShieldCheck size={15} />

                        <span>

                            Riesgo

                        </span>

                        <strong>

                            {dashboard.risk}

                        </strong>

                    </div>

                </div>

                {/* ====================================== */}
                {/* DERECHA */}
                {/* ====================================== */}

                <div className="topbarRight">

                    <button>

                        <Bell size={18} />

                    </button>

                    <button>

                        <Clock3 size={18} />

                    </button>

                    <button>

                        <Settings size={18} />

                    </button>

                    <div className="profile">

                        <UserCircle2 size={34} />

                        <div>

                            <strong>

                                {dashboard.user}

                            </strong>

                            <small>

                                Quant Trader

                            </small>

                        </div>

                    </div>

                </div>

            </header>

            <AccountModal

                open={openAccount}

                onClose={() => setOpenAccount(false)}

            />

        </>

    );

}