"use client";

import "./Sidebar.css";

import Link from "next/link";
import { usePathname } from "next/navigation";

import {

    LayoutDashboard,
    LineChart,
    Bot,
    Wallet,
    FlaskConical,
    BrainCircuit,
    Newspaper,
    ShieldCheck,
    Settings,
    Activity

} from "lucide-react";

const items = [

    {
        titulo:"Dashboard",
        href:"/",
        icon:LayoutDashboard
    },

    {
        titulo:"Mercado",
        href:"/mercado",
        icon:LineChart
    },

    {
        titulo:"Estrategias",
        href:"/estrategias",
        icon:BrainCircuit
    },

    {
        titulo:"Bot",
        href:"/bot",
        icon:Bot
    },

    {
        titulo:"Operaciones",
        href:"/operaciones",
        icon:Wallet
    },

    {
        titulo:"Backtesting",
        href:"/backtesting",
        icon:FlaskConical
    },

    {
        titulo:"Riesgo",
        href:"/riesgo",
        icon:ShieldCheck
    },

    {
        titulo:"Noticias",
        href:"/noticias",
        icon:Newspaper
    },

    {
        titulo:"Configuración",
        href:"/configuracion",
        icon:Settings
    }

];

export default function Sidebar(){

    const pathname=usePathname();

    return(

        <aside className="sidebar">

            <div>

                <div className="logo">

                    <div className="logoIcon">

                        TL

                    </div>

                    <div>

                        <h2>Trading Lab AI</h2>

                        <span>Quant Trading Platform</span>

                    </div>

                </div>

                <nav className="menu">

                    {

                        items.map((item)=>{

                            const Icon=item.icon;

                            return(

                                <Link

                                    key={item.titulo}

                                    href={item.href}

                                    className={`menuItem ${pathname===item.href?"active":""}`}

                                >

                                    <Icon size={20}/>

                                    <span>{item.titulo}</span>

                                </Link>

                            )

                        })

                    }

                </nav>

            </div>

            <div className="sidebarBottom">

                <div className="statusCard">

                    <div className="statusTitle">

                        <Activity size={16}/>

                        <span>BOT ONLINE</span>

                    </div>

                    <div className="statusRow">

                        <small>Broker</small>

                        <strong>Deriv Demo</strong>

                    </div>

                    <div className="statusRow">

                        <small>Mercado</small>

                        <strong>EURUSD</strong>

                    </div>

                    <div className="statusRow">

                        <small>Timeframe</small>

                        <strong>M1</strong>

                    </div>

                </div>

                <span className="version">

                    Version 2.0

                </span>

            </div>

        </aside>

    );

}