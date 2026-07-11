"use client";

import "./OpportunitiesHeader.css";

export default function OpportunitiesHeader() {

    return (

        <div className="opportunities-header">

            <div>

                <h2>Oportunidades</h2>

                <p>Señales detectadas por el motor de Trading Lab AI</p>

            </div>

            <div className="total-signals">

                <span>12</span>

                <small>Señales</small>

            </div>

        </div>

    );

}