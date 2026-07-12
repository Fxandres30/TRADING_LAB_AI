import { API_URL } from "./api";

export async function api<T>(
    endpoint: string,
    options: RequestInit = {}
): Promise<T> {

    const response = await fetch(
        `${API_URL}${endpoint}`,
        {
            cache: "no-store",
            headers: {
                "Content-Type": "application/json",
                ...(options.headers ?? {})
            },
            ...options
        }
    );

    if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
    }

    return response.json();

}