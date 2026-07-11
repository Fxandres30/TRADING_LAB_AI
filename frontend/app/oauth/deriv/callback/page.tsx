"use client";

import { useSearchParams } from "next/navigation";
import { useEffect } from "react";

export default function Callback() {
    const params = useSearchParams();

    useEffect(() => {
        const code = params.get("code");
        const state = params.get("state");

        console.log(code);
        console.log(state);

        // llamar al backend aquí
    }, []);

    return <h1>Conectando con Deriv...</h1>;
}