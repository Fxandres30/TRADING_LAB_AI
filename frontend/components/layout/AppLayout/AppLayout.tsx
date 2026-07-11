"use client";

import "./AppLayout.css";

import Sidebar from "../Sidebar/Sidebar";
import Topbar from "../Topbar/Topbar";

export default function AppLayout({

    children

}:{

    children:React.ReactNode

}){

    return(

        <div className="layout">

            <Sidebar/>

            <section className="content">

                <Topbar/>

                <main className="pageContainer">

                    {children}

                </main>

            </section>

        </div>

    );

}