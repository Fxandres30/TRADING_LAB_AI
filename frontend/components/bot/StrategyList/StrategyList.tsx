"use client";

import { useEffect, useState } from "react";

import "./StrategyList.css";

import StrategyCard from "../StrategyCard/StrategyCard";

import { Strategy } from "../types";

import { getStrategies } from "../../../services/strategyService";

export default function StrategyList() {

    const [strategies, setStrategies] = useState<Strategy[]>([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        async function cargar() {

            try {

                const data = await getStrategies();

                setStrategies(data);

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);

            }

        }

        cargar();

    }, []);

    if (loading) {

        return <p>Cargando estrategias...</p>;

    }

    return (

        <div className="strategyList">

            <div className="strategyHeader">

                <h2>🧪 Laboratorio IA</h2>

                <span>{strategies.length} estrategias</span>

            </div>

            <div className="strategyGrid">

                {

                    strategies.map(strategy => (

                        <StrategyCard

                            key={strategy.id}

                            strategy={strategy}

                        />

                    ))

                }

            </div>

        </div>

    );

}