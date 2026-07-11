"use client";

import "./OperationsDashboard.css";

import TradeStats from "./TradeStats";
import OpenTrades from "./OpenTrades";
import TradeHistory from "./TradeHistory";

export default function OperationsDashboard() {

    return (

        <div className="operationsDashboard">

            <TradeStats />

            <OpenTrades />

            <div className="bottomGrid">

                <TradeHistory />

            </div>

        </div>

    );

}