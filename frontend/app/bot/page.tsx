"use client";

import AppLayout from "@/components/layout/AppLayout/AppLayout";

import PageHeader from "@/components/ui/PageHeader/PageHeader";

import StrategyList from "@/components/bot/StrategyList/StrategyList";

export default function BotPage(){

    return(

        <AppLayout>

            <PageHeader

                title="Laboratorio de Estrategias"

                subtitle="Administra, configura y monitorea todas las estrategias."

            />

            <StrategyList/>

        </AppLayout>

    );

}