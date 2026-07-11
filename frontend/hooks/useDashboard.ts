import {useEffect,useState} from "react";
import {obtenerDashboard} from "@/services/dashboardService";

export default function useDashboard(){

    const[data,setData]=useState<any>(null);

    useEffect(()=>{

        async function cargar(){

            setData(await obtenerDashboard());

        }

        cargar();

        const id=setInterval(cargar,1000);

        return()=>clearInterval(id);

    },[]);

    return data;

}
