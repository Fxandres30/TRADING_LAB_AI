"use client";

import "./ChartHeader.css";

export default function ChartHeader() {

    return (

        <header className="chart-header">

            <div className="chart-symbol">

                <h2>EURUSD</h2>

                <span>Forex • M15</span>

            </div>

            <div className="chart-stats">

                <div className="chart-box">
                    <small>Bid</small>
                    <strong>1.08450</strong>
                </div>

                <div className="chart-box">
                    <small>Ask</small>
                    <strong>1.08454</strong>
                </div>

                <div className="chart-box">
                    <small>Spread</small>
                    <strong>0.4</strong>
                </div>

            </div>

        </header>

    );

}