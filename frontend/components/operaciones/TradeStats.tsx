"use client";

import { useEffect, useState } from "react";

import "./TradeStats.css";

interface Stats{

    operaciones:number;

    ganadas:number;

    perdidas:number;

    profit:number;

    balance:number;

    equity:number;

}

export default function TradeStats(){

    const [stats,setStats]=useState<Stats>({

        operaciones:0,

        ganadas:0,

        perdidas:0,

        profit:0,

        balance:0,

        equity:0

    });

    let cargando = false;

async function cargar() {

    if (cargando) return;

    cargando = true;

    try {

        const res = await fetch(
            "http://127.0.0.1:8000/operations/stats",
            {
                cache: "no-store"
            }
        );

        if (!res.ok) {
            throw new Error(`HTTP ${res.status}`);
        }

        const data = await res.json();

        setStats(data);

    } catch (err) {

        console.error("ERROR FETCH:", err);

    } finally {

        cargando = false;

    }

}

    useEffect(() => {

    let activo = true;

    async function loop() {

        while (activo) {

            await cargar();

            await new Promise(resolve => setTimeout(resolve, 2000));

        }

    }

    loop();

    return () => {
        activo = false;
    };

}, []);

    return(

        <div className="statsGrid">

            <div className="statCard">

                <span>Operaciones</span>

                <h2>{stats.operaciones}</h2>

            </div>

            <div className="statCard">

                <span>Ganadas</span>

                <h2 className="green">

                    {stats.ganadas}

                </h2>

            </div>

            <div className="statCard">

                <span>Perdidas</span>

                <h2 className="red">

                    {stats.perdidas}

                </h2>

            </div>

            <div className="statCard">

                <span>Profit</span>

                <h2 className={stats.profit>=0?"green":"red"}>

                    ${stats.profit.toFixed(2)}

                </h2>

            </div>

            <div className="statCard">

                <span>Balance</span>

                <h2>

                    ${stats.balance.toFixed(2)}

                </h2>

            </div>

            <div className="statCard">

                <span>Equity</span>

                <h2>

                    ${stats.equity.toFixed(2)}

                </h2>

            </div>

        </div>

    );

}