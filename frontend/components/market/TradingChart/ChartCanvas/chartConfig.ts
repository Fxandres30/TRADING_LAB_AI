import { DeepPartial, ChartOptions } from "lightweight-charts";

export const chartOptions: DeepPartial<ChartOptions> = {

    layout: {

        background: {

            color: "#ffffff",

        },

        textColor: "#475569",

    },

    grid: {

        vertLines: {

            color: "#eef2f7",

        },

        horzLines: {

            color: "#eef2f7",

        },

    },

    rightPriceScale: {

        borderColor: "#e2e8f0",

    },

    timeScale: {

        borderColor: "#e2e8f0",

        timeVisible: true,

        secondsVisible: false,

    },

    crosshair: {

        mode: 1,

    },

};