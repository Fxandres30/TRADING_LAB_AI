"use client";

import { Suspense, useEffect } from "react";
import { useSearchParams } from "next/navigation";

function CallbackContent() {
    const params = useSearchParams();

    useEffect(() => {
        const code = params.get("code");
        const state = params.get("state");

        console.log("Code:", code);
        console.log("State:", state);

        // TODO:
        // Llamar al backend
        // https://api.inversionesefaat.com/api/oauth/deriv/callback
    }, [params]);

    return <h1>Conectando con Deriv...</h1>;
}

export default function CallbackPage() {
    return (
        <Suspense fallback={<h1>Conectando...</h1>}>
            <CallbackContent />
        </Suspense>
    );
}