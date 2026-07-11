"use client";

import "./ConnectionStatus.css";

export default function ConnectionStatus() {
    return (
        <div className="connection-status">

            <span className="status-dot"></span>

            <div>
                <small>Estado</small>
                <strong>Conectado</strong>
            </div>

        </div>
    );
}