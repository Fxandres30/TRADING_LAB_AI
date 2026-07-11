"use client";

import "./Dashboard.css";

import ProfileCard from "./ProfileCard/ProfileCard";
import ScoreCard from "./ScoreCard/ScoreCard";

import BotControls from "../bot/BotControls/BotControls";

import DashboardCards from "./DashboardCards/DashboardCards";
import TradesTable from "../trades/TradesTable/TradesTable";

export default function Dashboard(){

    return(

        <main className="dashboard">

            <section className="dashboardTop">

                <ProfileCard/>

                <ScoreCard/>

                <BotControls/>

            </section>

            <section className="dashboardCards">

                <DashboardCards/>

            </section>

            <section className="dashboardBottom">

                <TradesTable/>

            </section>

        </main>

    );

}