"use client";

import "./TradingChart.css";

import {useEffect,useRef} from "react";

import {
    createChart,
    ColorType
} from "lightweight-charts";

export default function TradingChart(){

    const ref=useRef<HTMLDivElement>(null);

    useEffect(()=>{

        if(!ref.current) return;

        const chart=createChart(ref.current,{

            width:ref.current.clientWidth,

            height:500,

            layout:{

                background:{
                    type:ColorType.Solid,
                    color:"#131722"
                },

                textColor:"#d1d4dc"

            },

            grid:{

                vertLines:{
                    color:"#1f2937"
                },

                horzLines:{
                    color:"#1f2937"
                }

            },

            crosshair:{

                mode:1

            },

            rightPriceScale:{

                borderColor:"#374151"

            },

            timeScale:{

                borderColor:"#374151"

            }

        });

        const candles=chart.addCandlestickSeries({

            upColor:"#22c55e",

            downColor:"#ef4444",

            borderVisible:false,

            wickUpColor:"#22c55e",

            wickDownColor:"#ef4444"

        });

        candles.setData([

            {

                time:"2026-07-01",

                open:1.1400,

                high:1.1430,

                low:1.1390,

                close:1.1420

            },

            {

                time:"2026-07-02",

                open:1.1420,

                high:1.1440,

                low:1.1410,

                close:1.1435

            },

            {

                time:"2026-07-03",

                open:1.1435,

                high:1.1450,

                low:1.1425,

                close:1.1442

            }

        ]);

        chart.timeScale().fitContent();

        const resize=()=>{

            chart.applyOptions({

                width:ref.current!.clientWidth

            });

        };

        window.addEventListener("resize",resize);

        return()=>{

            window.removeEventListener("resize",resize);

            chart.remove();

        }

    },[]);

    return(

        <div className="chartContainer">

            <div className="chartHeader">

                <div>

                    <h2>EUR/USD</h2>

                    <span>H1 • Deriv Demo</span>

                </div>

                <div className="live">

                    🟢 LIVE

                </div>

            </div>

            <div

                ref={ref}

                className="chart"

            />

        </div>

    )

}