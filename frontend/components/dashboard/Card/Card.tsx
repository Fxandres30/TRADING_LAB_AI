"use client";

import "./Card.css";

import { ReactNode } from "react";

interface Props{

    titulo:string;

    valor:string|number;

    icon:ReactNode;

    color:string;

}

export default function Card({

    titulo,

    valor,

    icon,

    color

}:Props){

    return(

        <article className="card">

            <div className={`cardIcon ${color}`}>

                {icon}

            </div>

            <span className="cardTitle">

                {titulo}

            </span>

            <strong className="cardValue">

                {valor}

            </strong>

        </article>

    );

}