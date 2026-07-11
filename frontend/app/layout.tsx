import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";

import "./globals.css";

const geistSans = Geist({

    variable:"--font-geist-sans",

    subsets:["latin"]

});

const geistMono = Geist_Mono({

    variable:"--font-geist-mono",

    subsets:["latin"]

});

export const metadata={

    title:"Trading Lab AI",

    description:"Professional Quant Trading Platform"

};

export default function RootLayout({

    children

}:{

    children:React.ReactNode

}){

    return(

        <html
            lang="es"
            className={`${geistSans.variable} ${geistMono.variable}`}
        >

            <body>

                {children}

            </body>

        </html>

    )

}