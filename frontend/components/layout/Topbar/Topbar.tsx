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
    Settings

} from "lucide-react";

export default function Topbar(){

    const [openAccount,setOpenAccount]=useState(false);

    return(

    

        <header className="topbar">

            {/* IZQUIERDA */}

            <div className="topbarLeft">

                <div>

                    <h1>

                        Trading Lab AI

                    </h1>

                    <span>

                        Quantitative Trading Platform

                    </span>

                </div>

            </div>

            {/* CENTRO */}

            <div className="topbarCenter">

    <div className="status online">
        <Activity size={15}/>
        BOT ONLINE
    </div>

    <button className="selector">
        <Wifi size={15}/>
        Broker
        <strong>Deriv</strong>
    </button>

    <button className="selector">
        <UserCircle2 size={15}/>
        Cuenta
        <strong>Demo USD</strong>
    </button>

    <button

    className="selector add"

    onClick={()=>setOpenAccount(true)}

>

    + Agregar Cuenta

</button>

    <div className="status">
        <DollarSign size={15}/>
        Balance $9,970
    </div>

    <div className="status">
        <ShieldCheck size={15}/>
        Riesgo 1%
    </div>

</div>

            {/* DERECHA */}

            <div className="topbarRight">

                <button>

                    <Bell size={18}/>

                </button>

                <button>

                    <Clock3 size={18}/>

                </button>

                <button>

                    <Settings size={18}/>

                </button>

                <div className="profile">

                    <UserCircle2 size={34}/>

                    <div>

                        <strong>

                            Andrés Felipe

                        </strong>

                        <small>

                            Quant Trader

                        </small>

                    </div>

                </div>

            </div>

            <AccountModal

    open={openAccount}

    onClose={()=>setOpenAccount(false)}

/>

        </header>

    );

}
