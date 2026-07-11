"use client";

import "./DashboardCards.css";

import {
    Cpu,
    Wifi,
    Database,
    Shield,
    Activity,
    Landmark,
    CheckCircle,
    XCircle,
} from "lucide-react";

import useDashboard from "@/hooks/useDashboard";

import Card from "../Card/Card";

export default function DashboardCards() {

    const data = useDashboard();

    if (!data) return null;

    const broker = data.brokers?.Deriv;

    return (

        <section className="cards">

            <Card
                titulo="Engine"
                valor={data.running ? "Activo" : "Detenido"}
                icon={<Cpu size={20} />}
                color={data.running ? "green" : "red"}
            />

            <Card
                titulo="Broker"
                valor={broker?.broker ?? "N/D"}
                icon={<Landmark size={20} />}
                color="blue"
            />

            <Card
                titulo="Conectado"
                valor={broker?.connected ? "Sí" : "No"}
                icon={<Wifi size={20} />}
                color={broker?.connected ? "green" : "red"}
            />

            <Card
                titulo="Autorizado"
                valor={broker?.authorized ? "Sí" : "No"}
                icon={<Shield size={20} />}
                color={broker?.authorized ? "green" : "red"}
            />

            <Card
                titulo="Mercado"
                valor={data.market ? "Activo" : "Pendiente"}
                icon={<Activity size={20} />}
                color={data.market ? "green" : "orange"}
            />

            <Card
                titulo="Estrategias"
                valor={data.strategies ? "Activas" : "Pendiente"}
                icon={<CheckCircle size={20} />}
                color={data.strategies ? "green" : "orange"}
            />

            <Card
                titulo="Riesgo"
                valor={data.risk ? "Activo" : "Pendiente"}
                icon={<Shield size={20} />}
                color={data.risk ? "green" : "orange"}
            />

            <Card
                titulo="Base de Datos"
                valor={data.database ? "Conectada" : "Pendiente"}
                icon={<Database size={20} />}
                color={data.database ? "green" : "orange"}
            />

        </section>

    );

}