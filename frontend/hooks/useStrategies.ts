"use client";

import { useEffect, useState } from "react";
import { Strategy } from "@/components/bot/types";
import { getStrategies } from "@/services/strategyService";

export default function useStrategies(){

    const [strategies,setStrategies] = useState<Strategy[]>([]);
    const [loading,setLoading] = useState(true);

    useEffect(()=>{

        async function cargar(){

            try{

                const data = await getStrategies();

                setStrategies(data);

            }finally{

                setLoading(false);

            }

        }

        cargar();

    },[]);

    return{

        strategies,

        loading

    };

}