"use client";

import "./ScoreCard.css";

export default function ScoreCard() {

    return (

        <section className="scoreCard">

            <span className="title">

                SCORE INDEX

            </span>

            <div className="scoreContent">

                <div className="left">

                    <div className="scoreTop">

                        <h2>82</h2>

                        <span>/100</span>

                    </div>

                    <div className="progressBar">

                        <div className="progressFill"/>

                    </div>
                </div>

                <div className="circle">

                    82

                </div>

            </div>

            <div className="stats">

                <div className="stat">
                    <small>Win Rate</small>
                    <strong>82%</strong>
                </div>

                <div className="stat">
                    <small>Risk / Reward</small>
                    <strong>2.1</strong>
                </div>

                <div className="stat">
                    <small>Profit Factor</small>
                    <strong>1.84</strong>
                </div>

                <div className="stat">
                    <small>Drawdown</small>
                    <strong>4%</strong>
                </div>

                <div className="stat">
                    <small>Trades</small>
                    <strong>215</strong>
                </div>

            </div>

        </section>

    );

}