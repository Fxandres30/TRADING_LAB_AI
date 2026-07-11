"use client";

import "./ChartFooter.css";

export default function ChartFooter() {

    return (

        <footer className="chart-footer">

            <div>
                <small>Volumen</small>
                <strong>1.24M</strong>
            </div>

            <div>
                <small>Sesión</small>
                <strong>Londres</strong>
            </div>

            <div>
                <small>Hora</small>
                <strong>23:48:15</strong>
            </div>

            <div>
                <small>Estado</small>
                <strong className="online">En Vivo</strong>
            </div>

        </footer>

    );

}