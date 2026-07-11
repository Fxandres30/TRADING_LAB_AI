"use client";

import "./Opportunities.css";

import OpportunitiesHeader from "./OpportunitiesHeader/OpportunitiesHeader";
import OpportunityStats from "./OpportunityStats/OpportunityStats";
import OpportunityFilters from "./OpportunityFilters/OpportunityFilters";
import OpportunitiesTable from "./OpportunitiesTable/OpportunitiesTable";

export default function Opportunities(){

    return(

        <section className="opportunities">

            <OpportunitiesHeader/>

            <OpportunityStats/>

            <OpportunityFilters/>

            <OpportunitiesTable/>

        </section>

    );

}