"use client";

import "./PageCard.css";

interface Props{

    children:React.ReactNode;

}

export default function PageCard({

    children

}:Props){

    return(

        <section className="pageCard">

            {children}

        </section>

    );

}