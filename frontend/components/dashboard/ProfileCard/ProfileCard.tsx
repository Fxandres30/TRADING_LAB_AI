"use client";

import "./ProfileCard.css";

import {

    Award,
    TrendingUp,
    Wallet,
    BarChart3,
    Activity,
    Trophy

} from "lucide-react";

export default function ProfileCard(){

    return(

        <section className="profileCard">

            <div className="profileGradient"/>

            <div className="avatar">

                AF

            </div>

            <h2>

                Andrés Felipe Mercado

            </h2>

          <p>

                Quantitative Trader

            </p>

      {/* 
<div className="profileStats">

    <div>
        <TrendingUp size={17}/>
        <strong>82%</strong>
        <small>Win Rate</small>
    </div>

    <div>
        <Wallet size={17}/>
        <strong>$2,480</strong>
        <small>Profit</small>
    </div>

    <div>
        <Activity size={17}/>
        <strong>215</strong>
        <small>Trades</small>
    </div>

</div>
*/}

            <div className="profileBottom">

                <div>

                    <BarChart3 size={16}/>

                    <span>Balance</span>

                    <strong>$9,970</strong>

                </div>

                <div>

                    <Award size={16}/>

                    <span>Equity</span>

                    <strong>$9,968</strong>

                </div>

                <div>

                    <Trophy size={16}/>

                    <span>Score</span>

                    <strong>82</strong>

                </div>

            </div>

        </section>

    );

}