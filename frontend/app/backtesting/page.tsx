"use client";

import AppLayout from "@/components/layout/AppLayout/AppLayout";

import PageHeader from "@/components/ui/PageHeader/PageHeader";

import BacktestForm from "@/components/backtesting/BacktestForm/BacktestForm";
import MetricsGrid from "@/components/backtesting/MetricsGrid/MetricsGrid";
import EquityChart from "@/components/backtesting/EquityChart/EquityChart";
import AIAnalyzer from "@/components/backtesting/AIAnalyzer/AIAnalyzer";

export default function BacktestingPage(){

    return(

        <AppLayout>

            <PageHeader
                title="Backtesting Lab"
                subtitle="Prueba, optimiza y analiza estrategias con IA."
            />

            <BacktestForm/>

            <MetricsGrid/>

            <EquityChart/>

            <AIAnalyzer/>

        </AppLayout>

    );

}