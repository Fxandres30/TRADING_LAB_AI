"use client";

import "./Toolbar.css";

import BrokerSelector from "./BrokerSelector/BrokerSelector";
import SymbolSelector from "./SymbolSelector/SymbolSelector";
import TimeframeSelector from "./TimeframeSelector/TimeframeSelector";
import ConnectionStatus from "./ConnectionStatus/ConnectionStatus";
import MarketStatus from "./MarketStatus/MarketStatus";

export default function Toolbar() {
    return (
        <section className="toolbar">

            <div className="toolbar-left">
                <BrokerSelector />
                <SymbolSelector />
                <TimeframeSelector />
            </div>

            <div className="toolbar-right">
                <MarketStatus />
                <ConnectionStatus />
            </div>

        </section>
    );
}