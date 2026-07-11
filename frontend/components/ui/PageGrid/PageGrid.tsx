"use client";

import "./PageGrid.css";

interface Props{

    children:React.ReactNode;

}

export default function PageGrid({

    children

}:Props){

    return(

        <div className="pageGrid">

            {children}

        </div>

    );

}