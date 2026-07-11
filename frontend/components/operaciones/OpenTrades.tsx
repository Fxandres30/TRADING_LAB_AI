"use client";

import { useEffect, useState } from "react";
import "./OpenTrades.css";

interface Trade {
    ticket: number;
    symbol: string;
    type: string;
    volume: number;
    price_open: number;
    price_current: number;
    profit: number;
    sl: number;
    tp: number;
}

export default function OpenTrades() {

    const [trades, setTrades] = useState<Trade[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    async function cargar() {

        try {

            const res = await fetch(
                "http://127.0.0.1:8000/operations/open",
                { cache: "no-store" }
            );

            if (!res.ok)
                throw new Error();

            const data = await res.json();

            setTrades(data);
            setError("");

        } catch {

            setTrades([]);
            setError("No fue posible conectar con el servidor.");

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        cargar();

        const id = setInterval(cargar, 2000);

        return () => clearInterval(id);

    }, []);

    if (loading)
        return (
            <section className="tradeSection">
                <div className="sectionHeader">
                    <div>
                        <h2>Operaciones Abiertas</h2>
                        <span>Sincronizando...</span>
                    </div>
                </div>
            </section>
        );

    if (error)
        return (
            <section className="tradeSection">
                <div className="sectionHeader">
                    <div>
                        <h2>Operaciones Abiertas</h2>
                        <span>{error}</span>
                    </div>
                </div>
            </section>
        );

    return (

        <section className="tradeSection">

            <div className="sectionHeader">

                <div>

                    <h2>Operaciones Abiertas</h2>

                    <span>{trades.length} posiciones activas</span>

                </div>

                <div className="status">

                    <span className="liveDot"></span>

                    Actualización 2s

                </div>

            </div>

            <div className="tableWrapper">

                <table className="tradesTable">

                    <thead>

                        <tr>

                            <th>Ticket</th>
                            <th>Activo</th>
                            <th>Tipo</th>
                            <th>Lote</th>
                            <th>Entrada</th>
                            <th>Actual</th>
                            <th>SL</th>
                            <th>TP</th>
                            <th>P/L</th>

                        </tr>

                    </thead>

                    <tbody>

                        {

                            trades.length === 0 ?

                                <tr>

                                    <td colSpan={9} className="empty">

                                        No hay operaciones abiertas

                                    </td>

                                </tr>

                                :

                                trades.map((trade) => (

                                    <tr key={trade.ticket}>

                                        <td>{trade.ticket}</td>

                                        <td>

                                            <strong>{trade.symbol}</strong>

                                        </td>

                                        <td>

                                            <span
                                                className={
                                                    trade.type === "BUY"
                                                        ? "badge buy"
                                                        : "badge sell"
                                                }
                                            >

                                                {trade.type}

                                            </span>

                                        </td>

                                        <td>{trade.volume}</td>

                                        <td>{trade.price_open.toFixed(5)}</td>

                                        <td>{trade.price_current.toFixed(5)}</td>

                                        <td>{trade.sl.toFixed(5)}</td>

                                        <td>{trade.tp.toFixed(5)}</td>

                                        <td
                                            className={
                                                trade.profit >= 0
                                                    ? "profit"
                                                    : "loss"
                                            }
                                        >

                                            {trade.profit >= 0 ? "+" : ""}

                                            {trade.profit.toFixed(2)}

                                        </td>

                                    </tr>

                                ))

                        }

                    </tbody>

                </table>

            </div>

        </section>

    );

}