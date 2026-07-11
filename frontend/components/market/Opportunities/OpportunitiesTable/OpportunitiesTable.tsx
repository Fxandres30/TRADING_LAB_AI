"use client";

import "./OpportunitiesTable.css";

export default function OpportunitiesTable(){

    return(

        <table className="opportunities-table">

            <thead>

                <tr>

                    <th>Activo</th>

                    <th>Señal</th>

                    <th>Confianza</th>

                    <th>Estrategia</th>

                    <th>TF</th>

                    <th>Estado</th>

                </tr>

            </thead>

            <tbody>

                <tr>

                    <td>EURUSD</td>

                    <td className="buy">BUY</td>

                    <td>92%</td>

                    <td>Smart Money</td>

                    <td>M15</td>

                    <td>Lista</td>

                </tr>

                <tr>

                    <td>GBPUSD</td>

                    <td className="sell">SELL</td>

                    <td>86%</td>

                    <td>EMA RSI</td>

                    <td>M5</td>

                    <td>Esperando</td>

                </tr>

                <tr>

                    <td>XAUUSD</td>

                    <td className="buy">BUY</td>

                    <td>88%</td>

                    <td>BOS</td>

                    <td>H1</td>

                    <td>Ejecutada</td>

                </tr>

            </tbody>

        </table>

    );

}