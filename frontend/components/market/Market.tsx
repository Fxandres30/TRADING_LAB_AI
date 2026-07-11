"use client";

import "./Market.css";

import Toolbar from "./Toolbar/Toolbar";
import TradingChart from "./TradingChart/TradingChart";
import MarketSidebar from "./MarketSidebar/MarketSidebar";
import Opportunities from "./Opportunities/Opportunities";

export default function Market() {

    return (

        <section className="market">

            <Toolbar />

            <div className="market-layout">

                <div className="market-main">

                    <TradingChart />

                    <Opportunities />

                </div>

                <MarketSidebar />

            </div>

        </section>

    );

}