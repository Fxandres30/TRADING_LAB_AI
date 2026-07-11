"use client";

import "./StrategyCard.css";
import { Strategy } from "../types";

import { useState } from "react";

interface Props {
    strategy: Strategy;
}

export default function StrategyCard({ strategy }: Props) {

    async function toggleStrategy() {

    try {

        const res = await fetch(

            `http://127.0.0.1:8000/strategies/${strategy.codigo}`,

            {

                method: "PATCH",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    activa: !strategy.activa

                })

            }

        );

        if (!res.ok) {

            throw new Error(await res.text());

        }

        window.location.reload();

    }

    catch (e) {

        console.error(e);

    }

}

const [open, setOpen] = useState(false);

return (

<div className="strategyCard">

    <div
        className="strategyHeader"
        onClick={() => setOpen(!open)}
    >

        <div>

            <h3>{strategy.nombre}</h3>

            <p>{strategy.descripcion}</p>

        </div>

        <div className="strategyHeaderRight">

            <label
                className="switch"
                onClick={(e)=>e.stopPropagation()}
            >

                <input
                    type="checkbox"
                    checked={strategy.activa}
                    onChange={toggleStrategy}
                />

                <span className="slider"></span>

            </label>

            <button className="expandButton">

                {open ? "▲" : "▼"}

            </button>

        </div>

    </div>

    {open && (

    <>

        <div className="strategyActions">

            <button className="iconButton">⚙</button>

            <button className="iconButton">📊</button>

            <button className="iconButton">🧪</button>

        </div>

        <div className="statsGrid">

            <Stat titulo="🎯 Win Rate" valor={`${strategy.stats?.win_rate ?? 0}%`} />

            <Stat titulo="💰 Rentabilidad" valor={`${strategy.stats?.rentabilidad ?? 0}%`} />

            <Stat titulo="📦 Operaciones" valor={strategy.stats?.operaciones ?? 0} />

            <Stat titulo="⭐ Profit Factor" valor={strategy.stats?.profit_factor ?? 0} />

            <Stat titulo="📉 Drawdown" valor={`${strategy.stats?.drawdown ?? 0}%`} />

            <Stat titulo="🟢 Ganadas" valor={strategy.stats?.ganadas ?? 0} />

            <Stat titulo="🔴 Perdidas" valor={strategy.stats?.perdidas ?? 0} />

            <Stat titulo="🏆 Mayor Ganancia" valor={`$${strategy.stats?.mayor_ganancia ?? 0}`} />

            <Stat titulo="💥 Mayor Pérdida" valor={`$${strategy.stats?.mayor_perdida ?? 0}`} />

            <Stat titulo="🔥 Racha Win" valor={strategy.stats?.racha_ganadora ?? 0} />

            <Stat titulo="❄️ Racha Loss" valor={strategy.stats?.racha_perdedora ?? 0} />

            <Stat titulo="⏱ Tiempo Prom." valor={strategy.stats?.tiempo_promedio ?? "0s"} />

            <Stat titulo="⚡ Más rápida" valor={strategy.stats?.tiempo_minimo ?? "0s"} />

            <Stat titulo="🐢 Más lenta" valor={strategy.stats?.tiempo_maximo ?? "0s"} />

            <Stat titulo="🧠 Score IA" valor={`${strategy.stats?.score ?? 0}/100`} />

        </div>

        <div className="strategyBottom">

            <span>{strategy.categoria}</span>

            <span>v{strategy.version}</span>

        </div>

    </>

    )}

</div>

);
}

interface StatProps {

    titulo: string;

    valor: string | number;

}

function Stat({ titulo, valor }: StatProps) {

    return (

        <div className="stat">

            <span>{titulo}</span>

            <strong>{valor}</strong>

        </div>

    );

}