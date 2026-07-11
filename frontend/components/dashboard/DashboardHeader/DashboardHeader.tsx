"use client";

import "./DashboardHeader.css";

import {

    Activity,
    ShieldCheck,
    Wallet,
    Cpu

} from "lucide-react";

export default function DashboardHeader(){

    return(

        <section className="dashboardHeader">

            <div>

                <span className="miniTitle">

                    TRADING LAB AI

                </span>

                <h1>

                    Quantitative Trading Dashboard

                </h1>

                <p>

                    Monitoreo en tiempo real del laboratorio de estrategias.

                </p>

            </div>

            <div className="headerStats">

                <div>

                    <Activity/>

                    <span>BOT ONLINE</span>

                </div>

                <div>

                    <Wallet/>

                    <span>$9,970</span>

                </div>

                <div>

                    <ShieldCheck/>

                    <span>Risk 1%</span>

                </div>

                <div>

                    <Cpu/>

                    <span>5 IA</span>

                </div>

            </div>

        </section>

    );

}