"use client";

import "./PageHeader.css";

interface Props{

    title:string;

    subtitle:string;

}

export default function PageHeader({

    title,

    subtitle

}:Props){

    return(

        <header className="pageHeader">

            <div>

                <h1>

                    {title}

                </h1>

                <p>

                    {subtitle}

                </p>

            </div>

        </header>

    );

}