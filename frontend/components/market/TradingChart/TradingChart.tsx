"use client";

import "./TradingChart.css";

import ChartHeader from "./ChartHeader/ChartHeader";
import ChartCanvas from "./ChartCanvas/ChartCanvas";
import ChartFooter from "./ChartFooter/ChartFooter";

export default function TradingChart() {

    return (

        <section className="trading-chart">

            <ChartHeader />

            <ChartCanvas />

            <ChartFooter />

        </section>

    );

}