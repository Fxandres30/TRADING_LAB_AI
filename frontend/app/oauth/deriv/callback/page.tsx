"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function DerivCallbackPage() {

    const router = useRouter();

    useEffect(() => {

        console.log("======================================");
        console.log("✅ CALLBACK FRONTEND");
        console.log("======================================");
        console.log("El usuario llegó al callback del Frontend.");
        console.log("Con la Opción A este callback no procesa el OAuth.");
        console.log("El Backend ya debe haber realizado:");
        console.log("• Intercambio del código");
        console.log("• Obtención del Access Token");
        console.log("• Autorización del Broker");
        console.log("• Selección de la cuenta");
        console.log("======================================");

        const timer = setTimeout(() => {

            router.replace("/dashboard");

        }, 1500);

        return () => clearTimeout(timer);

    }, [router]);

    return (

        <div
            style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                gap: 20,
            }}
        >

            <h2>✅ Broker conectado</h2>

            <p>

                Redirigiendo al Dashboard...

            </p>

        </div>

    );

}