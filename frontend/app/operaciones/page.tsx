"use client";

import AppLayout from "@/components/layout/AppLayout/AppLayout";

import PageHeader from "@/components/ui/PageHeader/PageHeader";

import OperationsDashboard from "@/components/operaciones/OperationsDashboard";

export default function Operaciones(){

    return(

        <AppLayout>

            <PageHeader

                title="Operaciones"

                subtitle="Operaciones abiertas e historial"

            />

            <OperationsDashboard/>

        </AppLayout>

    );

}