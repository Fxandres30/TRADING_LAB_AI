"use client";

import "./OpportunityStats.css";

export default function OpportunityStats(){

    return(

        <div className="opportunity-stats">

            <div className="stat-card">
                <span>BUY</span>
                <strong>8</strong>
            </div>

            <div className="stat-card">
                <span>SELL</span>
                <strong>4</strong>
            </div>

            <div className="stat-card">
                <span>Win Rate</span>
                <strong>86%</strong>
            </div>

            <div className="stat-card">
                <span>IA Score</span>
                <strong>91%</strong>
            </div>

        </div>

    );

}