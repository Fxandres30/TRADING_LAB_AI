"use client";

import { useEffect, useRef } from "react";

import { ChartManager } from "./ChartManager";

export default function CandlestickChart() {

    const containerRef = useRef<HTMLDivElement>(null);

useEffect(() => {

    if (!containerRef.current) return;

    const chart = new ChartManager(containerRef.current);

    chart.loadHistory(

        "EURUSD",

        "M15"

    );

    const resize = () => {

        if (!containerRef.current) return;

        chart.resize(

            containerRef.current.clientWidth,

            containerRef.current.clientHeight

        );

    };

    resize();

    window.addEventListener("resize", resize);

    return () => {

        window.removeEventListener("resize", resize);

        chart.destroy();

    };

}, []);

    return (

        <div

            ref={containerRef}

            style={{

                width: "100%",

                height: "100%",

            }}

        />

    );

}