const isBrowser = typeof window !== "undefined";

const isLocal =
    isBrowser &&
    (
        window.location.hostname === "localhost" ||
        window.location.hostname === "127.0.0.1"
    );

export const API =
    process.env.NEXT_PUBLIC_API_URL ??
    (
        isLocal
            ? "http://127.0.0.1:8000"
            : "https://api.inversionesefaat.com"
    );

export const API_URL = `${API}/api`;