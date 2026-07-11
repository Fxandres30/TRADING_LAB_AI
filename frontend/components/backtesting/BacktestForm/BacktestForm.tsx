"use client";

import "./BacktestForm.css";

import { Play } from "lucide-react";
import { useEffect, useState } from "react";

import { getStrategies } from "@/services/strategyService";
import { Strategy } from "@/components/bot/types";

interface BacktestResult {
    resultado: {
        stats: {
            total_trades: number;
            wins: number;
            losses: number;
            win_rate: number;
            net_profit: number;
            balance_final: number;
        };
    };
}

export default function BacktestForm() {

    const [strategies, setStrategies] = useState<Strategy[]>([]);
    const [loading, setLoading] = useState(true);

    const [ejecutando, setEjecutando] = useState(false);

    const [resultado, setResultado] = useState<BacktestResult | null>(null);

    const [error, setError] = useState("");

    const [form, setForm] = useState({
        estrategia: "",
        simbolo: "EURUSD",
        timeframe: "M1",
        periodo: "2y",
        capital: 10000,
        riesgo: 1
    });

    useEffect(() => {
        cargar();
    }, []);

    async function cargar() {

        try {

            const data = await getStrategies();

            setStrategies(data);

            if (data.length > 0) {

                setForm(prev => ({
                    ...prev,
                    estrategia: data[0].codigo
                }));

            }

        } catch {

            setError("No fue posible cargar las estrategias.");

        } finally {

            setLoading(false);

        }

    }

    function change(
        e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
    ) {

        const { name, value } = e.target;

        setForm(prev => ({
            ...prev,
            [name]:
                name === "capital" || name === "riesgo"
                    ? Number(value)
                    : value
        }));

    }

    async function ejecutar() {

        try {

            setEjecutando(true);
            setResultado(null);
            setError("");

            const response = await fetch(
                "http://127.0.0.1:8000/backtest",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(form)
                }
            );

            if (!response.ok) {

                throw new Error("Error ejecutando el backtest.");

            }

            const data = await response.json();

            setResultado(data);

        } catch (err: any) {

            console.error(err);

            setError(err.message || "Error inesperado.");

        } finally {

            setEjecutando(false);

        }

    }

    if (loading) {

        return <p>Cargando estrategias...</p>;

    }

    return (

        <section className="backtestForm">

            <div className="field">
                <label>Estrategia</label>

                <select
                    name="estrategia"
                    value={form.estrategia}
                    onChange={change}
                >

                    {strategies.map(strategy => (

                        <option
                            key={strategy.id}
                            value={strategy.codigo}
                        >
                            {strategy.nombre}
                        </option>

                    ))}

                </select>
            </div>

            <div className="field">
                <label>Símbolo</label>

                <select
                    name="simbolo"
                    value={form.simbolo}
                    onChange={change}
                >
                    <option value="EURUSD">EURUSD</option>
                    <option value="GBPUSD">GBPUSD</option>
                    <option value="USDJPY">USDJPY</option>
                    <option value="XAUUSD">XAUUSD</option>
                </select>

            </div>

            <div className="field">
                <label>Timeframe</label>

                <select
                    name="timeframe"
                    value={form.timeframe}
                    onChange={change}
                >
                    <option value="M1">M1</option>
                    <option value="M5">M5</option>
                    <option value="M15">M15</option>
                    <option value="H1">H1</option>
                </select>

            </div>

            <div className="field">
                <label>Periodo</label>

                <select
                    name="periodo"
                    value={form.periodo}
                    onChange={change}
                >
                    <option value="30d">30 días</option>
                    <option value="3m">3 meses</option>
                    <option value="6m">6 meses</option>
                    <option value="1y">1 año</option>
                    <option value="2y">2 años</option>
                </select>

            </div>

            <div className="field">
                <label>Capital</label>

                <input
                    type="number"
                    name="capital"
                    value={form.capital}
                    onChange={change}
                />

            </div>

            <div className="field">
                <label>Riesgo (%)</label>

                <input
                    type="number"
                    name="riesgo"
                    value={form.riesgo}
                    onChange={change}
                />

            </div>

            <button
                className="runButton"
                onClick={ejecutar}
                disabled={ejecutando}
            >

                <Play size={18} />

                {ejecutando
                    ? "Ejecutando..."
                    : "Ejecutar Backtest"}

            </button>

            {error && (

                <div className="errorBacktest">

                    {error}

                </div>

            )}

            {resultado && (

                <div className="resultadoBacktest">

                    <h3>📊 Resultado del Backtest</h3>

                    <div className="gridResultados">

                        <div>
                            <span>Trades</span>
                            <strong>{resultado.resultado.stats.total_trades}</strong>
                        </div>

                        <div>
                            <span>Wins</span>
                            <strong>{resultado.resultado.stats.wins}</strong>
                        </div>

                        <div>
                            <span>Losses</span>
                            <strong>{resultado.resultado.stats.losses}</strong>
                        </div>

                        <div>
                            <span>Win Rate</span>
                            <strong>
                                {resultado.resultado.stats.win_rate.toFixed(2)}%
                            </strong>
                        </div>

                        <div>
                            <span>Profit</span>
                            <strong>
                                ${resultado.resultado.stats.net_profit.toFixed(2)}
                            </strong>
                        </div>

                        <div>
                            <span>Balance Final</span>
                            <strong>
                                ${resultado.resultado.stats.balance_final.toFixed(2)}
                            </strong>
                        </div>

                    </div>

                </div>

            )}

        </section>

    );

}