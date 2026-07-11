"use client";

import { Suspense, useEffect } from "react";
import { useSearchParams, useRouter } from "next/navigation";

function CallbackContent() {
    const params = useSearchParams();
    const router = useRouter();

    useEffect(() => {
        const code = params.get("code");
        const state = params.get("state") ?? "";

        if (!code) {
            console.error("No llegó el código OAuth");
            return;
        }

        async function conectar() {
            try {
                const res = await fetch(
                    `${process.env.NEXT_PUBLIC_API_URL}/api/oauth/deriv/callback`,
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            code,
                            state,
                        }),
                    }
                );

                const data = await res.json();

                console.log(data);

                router.replace("/dashboard");
            } catch (e) {
                console.error(e);
            }
        }

        conectar();
    }, [params, router]);

    return (
        <div
            style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                fontSize: 22,
            }}
        >
            🔄 Conectando con Deriv...
        </div>
    );
}

export default function Page() {
    return (
        <Suspense fallback={<div>Cargando...</div>}>
            <CallbackContent />
        </Suspense>
    );
}