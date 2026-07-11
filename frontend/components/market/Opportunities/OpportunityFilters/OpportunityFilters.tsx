"use client";

import "./OpportunityFilters.css";

export default function OpportunityFilters(){

    return(

        <div className="opportunity-filters">

            <button className="active">Todas</button>

            <button>EURUSD</button>

            <button>GBPUSD</button>

            <button>XAUUSD</button>

            <button>M15</button>

            <button>Smart Money</button>

        </div>

    );

}