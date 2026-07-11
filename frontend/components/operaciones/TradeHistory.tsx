"use client";

import { useEffect, useState } from "react";

import "./TradeHistory.css";

interface HistoryTrade{

    ticket:number;
    order:number;
    symbol:string;
    type:string;
    volume:number;
    price:number;
    profit:number;
    commission:number;
    swap:number;
    comment:string;
    time:number;

}

export default function TradeHistory(){

    const[history,setHistory]=useState<HistoryTrade[]>([]);
    const[loading,setLoading]=useState(true);

    async function cargar(){

        try{

            const res=await fetch(
                "http://127.0.0.1:8000/operations/history",
                {
                    cache:"no-store"
                }
            );

            const data=await res.json();

            setHistory(Array.isArray(data) ? data : []);

        }

        catch(error){

            console.error(error);

            setHistory([]);

        }

        finally{

            setLoading(false);

        }

    }

    useEffect(()=>{

        cargar();

    },[]);

    if(loading){

        return(

            <section className="tradeSection">

                <h2>📜 Historial</h2>

                <p>Cargando historial...</p>

            </section>

        );

    }

    return(

        <section className="tradeSection">

            <div className="sectionHeader">

                <h2>📜 Historial</h2>

                <span>{history.length} operaciones</span>

            </div>

            {

                history.length===0 ?

                (

                    <p className="empty">

                        No hay operaciones cerradas.

                    </p>

                )

                :

                (

                    <table className="historyTable">

                        <thead>

                            <tr>

                                <th>Ticket</th>
                                <th>Activo</th>
                                <th>Tipo</th>
                                <th>Lote</th>
                                <th>Precio</th>
                                <th>Profit</th>

                            </tr>

                        </thead>

                        <tbody>

                            {

                                history.map((trade)=>(

                                    <tr key={trade.ticket}>

                                        <td>{trade.ticket}</td>

                                        <td>{trade.symbol}</td>

                                        <td>

                                            <span
                                                className={
                                                    trade.type==="BUY"
                                                    ? "buy"
                                                    : "sell"
                                                }
                                            >

                                                {trade.type}

                                            </span>

                                        </td>

                                        <td>{trade.volume}</td>

                                        <td>{trade.price.toFixed(5)}</td>

                                        <td
                                            className={
                                                trade.profit>=0
                                                ? "profit"
                                                : "loss"
                                            }
                                        >

                                            ${trade.profit.toFixed(2)}

                                        </td>

                                    </tr>

                                ))

                            }

                        </tbody>

                    </table>

                )

            }

        </section>

    );

}